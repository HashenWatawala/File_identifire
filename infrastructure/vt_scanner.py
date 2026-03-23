import requests
import time

class VirusTotalScanner:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.virustotal.com/api/v3"
        self.headers = {
            "x-apikey": self.api_key
        }

    def scan_file(self, file_path):
        if not self.api_key or "your_key" in self.api_key:
            return {"error": "API Key not configured"}

        # 1. Upload file for scanning
        with open(file_path, "rb") as f:
            files = {"file": (file_path, f)}
            response = requests.post(f"{self.base_url}/files", headers=self.headers, files=files)
        
        if response.status_code != 200:
            return {"error": f"Upload failed: {response.status_code}"}
        
        analysis_id = response.json()["data"]["id"]
        
        # 2. Poll for results (simple version)
        # Note: In a real app, this should be async or handled via a callback
        # For this demonstration, we'll wait a bit or just return the analysis link
        return {
            "analysis_id": analysis_id,
            "link": f"https://www.virustotal.com/gui/file-analysis/{analysis_id}/detection"
        }

    def get_report(self, file_hash):
        if not self.api_key:
            return None

        response = requests.get(f"{self.base_url}/files/{file_hash}", headers=self.headers)
        if response.status_code == 200:
            data = response.json()["data"]["attributes"]
            return {
                "malicious": data["last_analysis_stats"]["malicious"],
                "suspicious": data["last_analysis_stats"]["suspicious"],
                "undetected": data["last_analysis_stats"]["undetected"],
                "harmless": data["last_analysis_stats"]["harmless"],
                "total": sum(data["last_analysis_stats"].values())
            }
        return None
