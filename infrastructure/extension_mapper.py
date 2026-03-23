class ExtensionMapper:
    def __init__(self):
        self.mapping = {
            ".png": "PNG Image",
            ".jpg": "JPEG Image",
            ".jpeg": "JPEG Image",
            ".pdf": "PDF Document",
            ".zip": "ZIP Archive",
            ".exe": "EXE File",
            ".gif": "GIF Image",
        }

    def get_expected_type(self, extension):
        return self.mapping.get(extension, None)