from infrastructure.file_reader import LocalFileReader
from infrastructure.signature_repository import InMemorySignatureRepository
from infrastructure.extension_mapper import ExtensionMapper

from domain.services import FileSecurityService
from application.use_cases import IdentifyFileTypeUseCase

from presentation.gui import run_gui
# from presentation.cli import run_cli

def main():
    file_reader = LocalFileReader()
    signature_repo = InMemorySignatureRepository()
    extension_mapper = ExtensionMapper()

    security_service = FileSecurityService(extension_mapper)

    use_case = IdentifyFileTypeUseCase(
        file_reader,
        signature_repo,
        security_service
    )

    # Choose interface
    run_gui(use_case)
    # run_cli(use_case)

if __name__ == "__main__":
    main()