# 🛡️ CyberScan - Advanced File Analysis Engine [V2.0]

CyberScan is a high-performance, industry-standard file identification and malware analysis tool. Built with **PyQt6**, it provides a "hacker-style" professional interface for rapid file triage, featuring signature matching, YARA rule integration, and live VirusTotal analysis.

<img width="999" height="786" alt="image" src="https://github.com/user-attachments/assets/ccb24d9b-ba07-4311-a744-254e48845870" />


## ✨ Core Features

*   **🚀 Instant Drag & Drop**: Simply drop any file into the analyzer for immediate multi-layered scanning.
*   **💻 Modern PyQt6 UI**: A sleek, dark "hacker-style" interface designed for cybersecurity professionals.
*   **🔍 Three-Tier Analysis**:
    *   **File Info**: Deep inspection of file signatures, magic bytes, and physical properties.
    *   **Security Report**: Real-time detection of extension mismatches and suspicious headers.
    *   **VT Integration**: Live hash-based analysis using the VirusTotal v3 API.
*   **🔥 Industrial YARA Support**: Scan files against community or custom YARA rules for high-fidelity threat detection.
*   **⚡ Cryptographic Hashing**: Automatic generation of MD5 and SHA256 hashes for every file.

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- [YARA](https://virustotal.github.io/yara/) (Required for `yara-python`)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/HashenWatawala/File_identifire.git
   cd File_identifire
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your API key:
   Create a `.env` file in the root directory and add your VirusTotal API key:
   ```env
   VT_API_KEY=your_virustotal_api_key_here
   ```

## 🚀 Usage

Launch the application using:
```bash
python main.py
```

### Drag & Drop Scanning
1. Open the CyberScan window.
2. Drag your target file into the dashed **"Drag & Drop"** zone.
3. Switch between tabs (**FILE INFO**, **SECURITY REPORT**, **VIRUSTOTAL**) to view detailed results.

## 📁 Project Structure

```text
File_identifire/
├── .env                # Private API Keys (Excluded by gitignore)
├── .gitignore          # Repository exclusions
├── main.py             # Application Entry Point
├── requirements.txt    # Python dependencies
├── application/        # Business Logic & Use Cases
├── domain/             # Core Entities & Services
├── infrastructure/     # External Integrations (YARA, VT, File IO)
│   ├── yara_rules/     # Custom .yar rule directory
│   └── ...
└── presentation/       # PyQt6 GUI Implementation
```

## 🛡️ Security Disclaimer

This tool is designed for educational and professional malware analysis. Always handle suspicious files in a secure, isolated sandbox environment.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
