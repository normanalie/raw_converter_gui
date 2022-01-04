#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    A mass RAW images converter to jpeg or png.
    This converter use tkinter for GUI, rawpy to open RAW and make a Numpy array, imageio and PIL to write the image on disk.
"""

import os
import tkinter as tk
from tkinter import filedialog

import converter

__author__ = "Norman Alié"
__license__ = "GPL"
__version__ = "0.2"
__maintainer__ = "Norman Alié"
__email__ = "mail@normanalie.Fr"
__status__ = "Dev"


window = tk.Tk()
errors = tk.StringVar()
infos = tk.StringVar()

input_files = ""
output_path = ""

def browse_input():
    global input_files
    initialdir = os.getcwd()

    input_files = filedialog.askopenfilenames(
        initialdir=initialdir,
        title="Select one or multiples RAW images",
        filetypes=(
            ('RAW Images', converter.raw_extensions),
            ('All files', '*.*')
        )
    )

def browse_output():
    global output_path
    initialdir = os.getcwd()

    output_path = filedialog.askdirectory(
        initialdir=initialdir,
        title="Select destination folder"
    )

def convert():
    if not input_files:
        errors.set(errors.get() + "Please select input file\n")
    if not output_path:
        errors.set(errors.get() + "Please select output folder\n")
    
    errors.set("")
    infos.set("")

    for file in input_files:
        filename = os.path.split(file)[1]
        filename = os.path.splitext(filename)[0]
        output_file = os.path.join(output_path, filename + "." + output_format.get())
        try:
            converter.convert(file, output_file)
        except ValueError as e:
            errors.set(errors.get() + f"Error converting {filename}: \n {e} \n")
        except Exception as e:
            errors.set(errors.get() + f"Unexpected error converting {filename}: \n {e} \n")
        else:
            infos.set(infos.get() + f"{filename} converted ! \n")
        window.update()


window.title("RAW Converter")
window.geometry("900x500")

errorLabel = tk.Label(window, textvariable=errors, fg="red")
errorLabel.pack()

infoLabel = tk.Label(window, textvariable=infos, fg="green")
infoLabel.pack()

label = tk.Label(window, text="Select input file(s)")
label.pack(pady=(20, 10), fill="x")

button = tk.Button(window, text="Open...", command=browse_input)
button.pack(ipady=5, ipadx=8)

label = tk.Label(window, text="Select output format")
label.pack(pady=(50, 10), fill="x")

output_format = tk.StringVar(window, "jpeg")
radioA = tk.Radiobutton(window, text=".jpeg",  variable=output_format, value="jpeg")
radioB = tk.Radiobutton(window, text=".png", variable=output_format, value="png")
radioA.pack(ipady=5, ipadx=8)
radioB.pack(ipady=5, ipadx=8)

label = tk.Label(window, text="Select output folder")
label.pack(pady=(50, 10))

button = tk.Button(window, text="Browse...", command=browse_output)
button.pack(ipady=5, ipadx=8)

button = tk.Button(window, text="Convert !", command=convert)
button.pack(pady=(50, 0), ipady=8, ipadx=12)

window.mainloop()