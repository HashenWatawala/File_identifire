from domain.interfaces import SignatureRepository
from domain.entities import FileSignature

class InMemorySignatureRepository(SignatureRepository):
    def get_signatures(self):
        return [
            FileSignature(0, b"\x89PNG", "PNG Image"),
            FileSignature(0, b"\xFF\xD8\xFF", "JPEG Image"),
            FileSignature(0, b"\x25PDF", "PDF Document"),
            FileSignature(0, b"\x50\x4B\x03\x04", "ZIP Archive"),
            FileSignature(0, b"\x4D\x5A", "EXE File"),
            FileSignature(0, b"\x47\x49\x46\x38", "GIF Image"),
            FileSignature(0, b"\x7F\x45\x4C\x46", "ELF Executable"),
        ]