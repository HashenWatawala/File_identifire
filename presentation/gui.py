import tkinter as tk
from tkinter import filedialog

def run_gui(use_case):
    def select_file():
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        result = use_case.execute(file_path)

        output = f"Detected: {result.file_type}\n"

        if result.is_suspicious:
            output += "\n[!] Suspicious File!\n"
            output += f"Expected: {result.expected_type}"

        label.config(text=output)

    root = tk.Tk()
    root.title("File Type Identifier")

    root.geometry("400x200")

    btn = tk.Button(root, text="Select File", command=select_file)
    btn.pack(pady=20)

    label = tk.Label(root, text="Result will appear here", wraplength=350)
    label.pack(pady=20)

    root.mainloop()