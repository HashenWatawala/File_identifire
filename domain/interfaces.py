from abc import ABC, abstractmethod

class FileReader(ABC):
    @abstractmethod
    def read_bytes(self, file_path: str, num_bytes: int) -> bytes:
        pass


class SignatureRepository(ABC):
    @abstractmethod
    def get_signatures(self):
        pass