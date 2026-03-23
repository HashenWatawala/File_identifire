import hashlib
import os
from application.dto import FileAnalysisResult

class IdentifyFileTypeUseCase:
    def __init__(self, file_reader, signature_repo, security_service, yara_scanner=None, vt_scanner=None):
        self.file_reader = file_reader
        self.signature_repo = signature_repo
        self.security_service = security_service
        self.yara_scanner = yara_scanner
        self.vt_scanner = vt_scanner

    def execute(self, file_path: str):
        # 1. Basic File Info
        file_size = os.path.getsize(file_path)
        
        # 2. Hash Calculation
        md5_hash = hashlib.md5()
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    md5_hash.update(byte_block)
                    sha256_hash.update(byte_block)
        except Exception as e:
            print(f"Error calculating hashes: {e}")

        # 3. Signature Matching
        file_data = self.file_reader.read_bytes(file_path, 20)
        signatures = self.signature_repo.get_signatures()
        detected_type = "Unknown File Type"

        for sig in signatures:
            start = sig.offset
            end = start + len(sig.magic_bytes)
            if file_data[start:end] == sig.magic_bytes:
                detected_type = sig.file_type
                break

        # 4. Malware & Mismatch Detection
        is_suspicious, expected_type = self.security_service.check_mismatch(
            file_path, detected_type
        )

        # 5. YARA Scanning
        yara_matches = []
        if self.yara_scanner:
            yara_matches = self.yara_scanner.scan(file_path)
            if yara_matches:
                is_suspicious = True

        # 6. VirusTotal Check (Hash based)
        vt_report = None
        if self.vt_scanner:
            vt_report = self.vt_scanner.get_report(sha256_hash.hexdigest())
            if vt_report and vt_report.get("malicious", 0) > 0:
                is_suspicious = True

        return FileAnalysisResult(
            file_path=file_path,
            file_type=detected_type,
            is_suspicious=is_suspicious,
            expected_type=expected_type,
            yara_matches=yara_matches,
            md5=md5_hash.hexdigest(),
            sha256=sha256_hash.hexdigest(),
            file_size=file_size,
            vt_report=vt_report
        )