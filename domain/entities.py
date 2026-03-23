class FileSignature:
    def __init__(self, offset, magic_bytes, file_type):
        self.offset = offset
        self.magic_bytes = magic_bytes
        self.file_type = file_type