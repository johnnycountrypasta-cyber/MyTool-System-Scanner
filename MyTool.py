import configparser
import tkinter as tk
from tkinter import ttk
import platform
import psutil

# Load INI
config = configparser.ConfigParser()
config.read("MyTool.ini")

# Load Script
script_settings = {}
with open("MyTool.script", "r") as f:
    for line in f:
        if "=" in line:
            key, value = line.strip().split("=")
            script_settings[key] = value

# GUI
root = tk.Tk()
root.title("MyTool System Scanner")

tabs = ttk.Notebook(root)
tabs.pack(expand=True, fill="both")

def add_tab(name, text):
    frame = ttk.Frame(tabs)
    tabs.add(frame, text=name)
    label = tk.Label(frame, text=text, anchor="nw", justify="left")
    label.pack(fill="both", expand=True)

# CPU
if script_settings.get("SCAN_CPU") == "1":
    cpu_info = f"Processor: {platform.processor()}\nCores: {psutil.cpu_count(logical=False)}\nThreads: {psutil.cpu_count(logical=True)}"
    add_tab("CPU", cpu_info)

# RAM
if script_settings.get("SCAN_RAM") == "1":
    ram = psutil.virtual_memory()
    ram_info = f"Total RAM: {ram.total // (1024**3)} GB\nUsed: {ram.used // (1024**3)} GB"
    add_tab("RAM", ram_info)

# OS
if script_settings.get("SCAN_OS") == "1":
    os_info = f"System: {platform.system()}\nVersion: {platform.version()}"
    add_tab("OS", os_info)

root.mainloop()
