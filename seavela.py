import tkinter as tk
from tkinter import filedialog
import subprocess

class SikuliRunnerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("SikuliX Runner")

        # Create buttons for each SikuliX script
        script_names = ["npc_event.py", "npc_event", "npc_event.py", "npc_event.py" , "eldourado.py"]
        for script_name in script_names:
            button_text = "Run {}".format(script_name)
            button = tk.Button(master, text=button_text, command=lambda s=script_name: self.run_script(s))
            button.pack(pady=5)

    def run_script(self, script_name):
        # Run the selected SikuliX script using subprocess
        script_path = filedialog.askopenfilename(filetypes=[("Python Scripts", "*.py")])
        if script_path:
            subprocess.run(["python", script_path])
        else:
            print("Please choose a script first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SikuliRunnerApp(root)
    root.mainloop()
