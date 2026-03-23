class FileAnalysisResult:
    def __init__(self, file_path, file_type, is_suspicious, expected_type=None, yara_matches=None, md5=None, sha256=None, file_size=0, vt_report=None):
        self.file_path = file_path
        self.file_type = file_type
        self.is_suspicious = is_suspicious
        self.expected_type = expected_type
        self.yara_matches = yara_matches or []
        self.md5 = md5
        self.sha256 = sha256
        self.file_size = file_size
        self.vt_report = vt_report
        
    def __str__(self):
        return f"FileAnalysisResult(file_path={self.file_path}, file_type={self.file_type}, is_suspicious={self.is_suspicious})"