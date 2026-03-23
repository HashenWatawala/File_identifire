import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QTabWidget, 
                             QTextEdit, QFileDialog, QFrame)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QFont, QPalette, QColor

HACKER_STYLE = """
QMainWindow {
    background-color: #0d0d0d;
}
QTabWidget::pane {
    border: 1px solid #00ff00;
    background: #1a1a1a;
}
QTabBar::tab {
    background: #262626;
    color: #00ff00;
    padding: 10px;
    border: 1px solid #333;
}
QTabBar::tab:selected {
    background: #1a1a1a;
    border-bottom: 2px solid #00ff00;
}
QWidget {
    color: #00ff00;
    font-family: 'Courier New', monospace;
}
QTextEdit {
    background-color: #000;
    border: 1px solid #00ff00;
    color: #00ff00;
}
QPushButton {
    background-color: #004400;
    border: 1px solid #00ff00;
    padding: 8px;
    border-radius: 4px;
}
QPushButton:hover {
    background-color: #006600;
}
QLabel#DropZone {
    border: 2px dashed #00ff00;
    border-radius: 10px;
    padding: 40px;
    font-size: 18px;
}
"""

class DropZone(QLabel):
    fileDropped = pyqtSignal(str)

    def __init__(self):
        super().__init__("Drag & Drop File Here to Scan")
        self.setObjectName("DropZone")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.setStyleSheet("border-color: #ffffff; color: #ffffff;")

    def dragLeaveEvent(self, event):
        self.setStyleSheet("")

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            self.fileDropped.emit(file_path)
        self.setStyleSheet("")

class ModernGui(QMainWindow):
    def __init__(self, use_case):
        super().__init__()
        self.use_case = use_case
        self.setWindowTitle("CyberScan - File Identifier Pro")
        self.resize(800, 600)
        self.setStyleSheet(HACKER_STYLE)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Header
        header = QLabel("EXTREME FILE ANALYZER [V2.0]")
        header.setFont(QFont("Courier New", 24, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        # Drag & Drop Zone
        self.drop_zone = DropZone()
        self.drop_zone.fileDropped.connect(self.run_scan)
        layout.addWidget(self.drop_zone)

        # Select File Button
        btn_layout = QHBoxLayout()
        self.select_btn = QPushButton("SELECT FILE MANUALLY")
        self.select_btn.clicked.connect(self.manual_select)
        btn_layout.addStretch()
        btn_layout.addWidget(self.select_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        # Tabs
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # Tab 1: File Info
        self.info_tab = QTextEdit()
        self.info_tab.setReadOnly(True)
        self.tabs.addTab(self.info_tab, "FILE INFO")

        # Tab 2: Security Report
        self.security_tab = QTextEdit()
        self.security_tab.setReadOnly(True)
        self.tabs.addTab(self.security_tab, "SECURITY REPORT")

        # Tab 3: VirusTotal
        self.vt_tab = QTextEdit()
        self.vt_tab.setReadOnly(True)
        self.tabs.addTab(self.vt_tab, "VIRUSTOTAL RESULTS")

    def manual_select(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Scan")
        if file_path:
            self.run_scan(file_path)

    def run_scan(self, file_path):
        result = self.use_case.execute(file_path)
        self.display_result(result)

    def display_result(self, result):
        # Update Info Tab
        info = f"""[>] FILE: {os.path.basename(result.file_path)}
[>] PATH: {result.file_path}
[>] SIZE: {result.file_size} bytes
[>] TYPE: {result.file_type}
[>] MD5:  {result.md5}
[>] SHA256: {result.sha256}
"""
        self.info_tab.setText(info)

        # Update Security Tab
        sec = "[#] SCAN REPORT [#]\n"
        if result.is_suspicious:
            sec += "\n[!!!] WARNING: SUSPICIOUS FILE DETECTED [!!!]\n"
            if result.expected_type:
                sec += f"[!] TYPE MISMATCH: File claims to be {result.expected_type}\n"
            
            if result.yara_matches:
                sec += "[!] YARA MATCHES FOUND:\n"
                for match in result.yara_matches:
                    sec += f"    - {match}\n"
            
            if result.vt_report and result.vt_report.get("malicious", 0) > 0:
                sec += f"[!] VIRUSTOTAL: {result.vt_report['malicious']} engines flagged this file!\n"
        else:
            sec += "\n[+] No common threats detected.\n"
        
        self.security_tab.setText(sec)

        # Update VirusTotal Tab
        vt_text = "[#] VIRUSTOTAL ANALYSIS [#]\n\n"
        if result.vt_report:
            vt_text += f"Status: COMPLETED\n"
            vt_text += f"Malicious: {result.vt_report['malicious']}\n"
            vt_text += f"Suspicious: {result.vt_report['suspicious']}\n"
            vt_text += f"Undetected: {result.vt_report['undetected']}\n"
            vt_text += f"Harmless: {result.vt_report['harmless']}\n"
            vt_text += f"Total Engines: {result.vt_report['total']}\n"
            
            if result.vt_report['malicious'] > 0:
                vt_text += "\n[!] HIGH RISK DETECTED BY MULTIPLE ENGINES"
        else:
            vt_text += "[!] No analysis found for this hash on VirusTotal.\n"
            vt_text += "[?] You may need to upload the file to VirusTotal manually or check your connection."
        
        self.vt_tab.setText(vt_text)
        
        # Switch to info tab
        self.tabs.setCurrentIndex(0)

def run_gui(use_case):
    app = QApplication(sys.argv)
    window = ModernGui(use_case)
    window.show()
    sys.exit(app.exec())
