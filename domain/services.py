import os

class FileSecurityService:
    def __init__(self, extension_mapper):
        self.extension_mapper = extension_mapper

    def check_mismatch(self, file_path, detected_type):
        ext = os.path.splitext(file_path)[1].lower()
        expected_type = self.extension_mapper.get_expected_type(ext)

        if expected_type and expected_type != detected_type:
            return True, expected_type

        return False, expected_type