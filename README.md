# **RAW Converter (with GUI)**

### **A mass RAW images converter using Python and Tkinter**


## Execute:
Require **python 3** and **pip** installed. It' recommended to work in a virtualenv.  

Move to the project directory: `cd <path-to-folder>/raw_converter_gui-main/`  
Install packages: `pip install -r requirements.txt`  
Run: `py main.py`
## Build with pyinstaller:
### **If you are in a virtualenv:**
Move to the project directory: `cd <path-to-folder>/raw_converter_gui-main/`  
Activate you venv: `./venv/Scripts/activate`  
Install packages: `pip install -r requirements.txt`  
Deactivate your venv: `deactivate`  
Install pyinstaller: `pip install pyinstaller`  
Build the exe: `pyinstaller --onefile --windowed --paths "venv/Lib/site-packages"  main.py`

### **If you are not in a venv:**
Move to the project directory: `cd <path-to-folder>/raw_converter_gui-main/`  
Install packages: `pip install -r requirements.txt`  
Install pyinstaller: `pip install pyinstaller`  
Build the exe: `pyinstaller --onefile --windowed main.py`