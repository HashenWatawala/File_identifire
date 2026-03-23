from domain.interfaces import FileReader

class LocalFileReader(FileReader):
    def read_bytes(self, file_path: str, num_bytes: int) -> bytes:
        with open(file_path, "rb") as f:
            return f.read(num_bytes)