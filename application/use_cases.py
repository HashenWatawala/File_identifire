from application.dto import FileAnalysisResult

class IdentifyFileTypeUseCase:
    def __init__(self, file_reader, signature_repo, security_service):
        self.file_reader = file_reader
        self.signature_repo = signature_repo
        self.security_service = security_service

    def execute(self, file_path: str):
        file_data = self.file_reader.read_bytes(file_path, 20)
        signatures = self.signature_repo.get_signatures()

        detected_type = "Unknown File Type"

        for sig in signatures:
            start = sig.offset
            end = start + len(sig.magic_bytes)

            if file_data[start:end] == sig.magic_bytes:
                detected_type = sig.file_type
                break

        # Malware detection
        is_suspicious, expected_type = self.security_service.check_mismatch(
            file_path, detected_type
        )

        return FileAnalysisResult(
            detected_type,
            is_suspicious,
            expected_type
        )