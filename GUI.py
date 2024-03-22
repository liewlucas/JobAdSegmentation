# Import recipe generation function and other required libraries 
from cgitb import text
import tkinter as tk
from tkinter import ttk
from transformers import FlaxAutoModelForSeq2SeqLM
from transformers import AutoTokenizer
import pandas as pd 
import random
import nltk
from nltk.translate.meteor_score import meteor_score


def on_exit_click():
    root.quit()

# Create the GUI
root = tk.Tk()
root.title('Job Advertisement Extraction')
root.configure(bg='white')

# Create a rounded style for the buttons
s = ttk.Style()
s.configure('Rounded.TButton', borderwidth=0, focuscolor='white', focusthickness=0, font=('Helvetica', 12))

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(expand=True, fill='both')

input_label = ttk.Label(main_frame, text='Enter Job Advertisements Here:')
input_label.pack(pady=5)

# Use a Text widget for the multi-line input
input_text = tk.Text(main_frame, wrap=tk.WORD, width=30, height=15)
input_text.pack(pady=5)

output_label = ttk.Label(main_frame, text='Extracted Relevant Job Skills goes Below: ')
output_label.pack(pady=2)

output_text = tk.Text(main_frame, wrap=tk.WORD, width=80, height=10, state="disabled")
output_text.pack(pady=5)

score_label = ttk.Label(main_frame, text='Testing: ')
score_label.pack(pady=2)

# Centering the buttons in a new frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=10)

ok_button = ttk.Button(button_frame, text='Extract Keywords', style='Rounded.TButton')
ok_button.pack(side=tk.LEFT, padx=5)

exit_button = ttk.Button(button_frame, text='Exit', style='Rounded.TButton', command=on_exit_click)
exit_button.pack(side=tk.RIGHT, padx=5)

# Set the background color using the style option
s.configure('Rounded.TButton', background='#87CEEB', foreground='dark blue')

root.mainloop()
