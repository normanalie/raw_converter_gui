#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    A mass RAW images converter to jpeg or png.
    This converter use tkinter for GUI, rawpy to open RAW and make a Numpy array, imageio and PIL to write the image on disk.
"""

import tkinter as tk

__author__ = "Norman Alié"
__license__ = "GPL"
__version__ = "0.2"
__maintainer__ = "Norman Alié"
__email__ = "mail@normanalie.Fr"
__status__ = "Dev"


def browse_input():
    pass

def browse_output():
    pass


window = tk.Tk()

label = tk.Label(window, text="Select input file(s)")
label.pack()

button = tk.Button(window, text="Open...", command=browse_input)
button.pack()

label = tk.Label(window, text="Select output format")
label.pack()

output_format = tk.StringVar(window, "jpeg")
radioA = tk.Radiobutton(window, text=".jpeg",  variable=output_format, value="jpeg")
radioB = tk.Radiobutton(window, text=".png", variable=output_format, value="png")
radioA.pack()
radioB.pack()

label = tk.Label(window, text="Select output folder")
label.pack()

button = tk.Button(window, text="Browse...", command=browse_output)
button.pack()

window.mainloop()