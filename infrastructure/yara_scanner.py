import yara
import os

class YaraScanner:
    def __init__(self, rules_dir):
        self.rules_dir = rules_dir
        self.rules = self._load_rules()

    def _load_rules(self):
        rule_files = {}
        if not os.path.exists(self.rules_dir):
            os.makedirs(self.rules_dir)
            # Create a dummy rule for demonstration
            dummy_rule = "rule ExampleRule { strings: $a = \"malware\" condition: $a }"
            with open(os.path.join(self.rules_dir, "dummy.yar"), "w") as f:
                f.write(dummy_rule)

        for filename in os.listdir(self.rules_dir):
            if filename.endswith(".yar") or filename.endswith(".yara"):
                rule_files[filename] = os.path.join(self.rules_dir, filename)

        if not rule_files:
            return None

        try:
            return yara.compile(filepaths=rule_files)
        except Exception as e:
            print(f"Error compiling YARA rules: {e}")
            return None

    def scan(self, file_path):
        if not self.rules:
            return []

        try:
            matches = self.rules.match(file_path)
            return [str(match) for match in matches]
        except Exception as e:
            print(f"Error scanning with YARA: {e}")
            return []
