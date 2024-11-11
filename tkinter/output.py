import tkinter as tk
from tkinter import filedialog

def ask_for_image():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select an image",filetypes=[("Image files","*.jpg;*.jpeg;*.png;*.gif,*.bmp")])
    return file_path

image_path = ask_for_image()
if image_path :
    print(f"Selected Image: {image_path}")
else:
    print("No image selected")