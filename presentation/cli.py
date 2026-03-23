def run_cli(use_case):
    import sys

    if len(sys.argv) != 2:
        print("Usage: python main.py <file>")
        return

    file_path = sys.argv[1]
    result = use_case.execute(file_path)

    print(f"[+] File: {file_path}")
    print(f"[+] Detected Type: {result.file_type}")

    if result.is_suspicious:
        print("[!] WARNING: Suspicious file detected!")
        print(f"    Expected: {result.expected_type}")