class FileAnalysisResult:
    def __init__(self, file_type, is_suspicious, expected_type=None):
        self.file_type = file_type
        self.is_suspicious = is_suspicious
        self.expected_type = expected_type