from infrastructure.file_reader import LocalFileReader
from infrastructure.signature_repository import InMemorySignatureRepository
from infrastructure.extension_mapper import ExtensionMapper
from infrastructure.yara_scanner import YaraScanner
from infrastructure.vt_scanner import VirusTotalScanner

from domain.services import FileSecurityService
from application.use_cases import IdentifyFileTypeUseCase

from presentation.gui_pyqt import run_gui
import os
from dotenv import load_dotenv

def main():
    # Load Environment Variables
    load_dotenv()
    
    file_reader = LocalFileReader()
    signature_repo = InMemorySignatureRepository()
    extension_mapper = ExtensionMapper()
    
    # Initialize YARA Scanner
    base_dir = os.path.dirname(os.path.abspath(__file__))
    yara_rules_dir = os.path.join(base_dir, "infrastructure", "yara_rules")
    yara_scanner = YaraScanner(yara_rules_dir)

    # Initialize VirusTotal Scanner
    vt_api_key = os.getenv("VT_API_KEY")
    vt_scanner = VirusTotalScanner(vt_api_key)

    security_service = FileSecurityService(extension_mapper)

    use_case = IdentifyFileTypeUseCase(
        file_reader,
        signature_repo,
        security_service,
        yara_scanner,
        vt_scanner
    )

    run_gui(use_case)

if __name__ == "__main__":
    main()