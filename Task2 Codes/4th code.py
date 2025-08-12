from PIL import Image, ImageDraw
from tkinter import Tk, filedialog
import os

def blackout_left_quarter(image):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width // 4, height), fill="black")
    return image

# Hide Tkinter main window
Tk().withdraw()

# Ask user to choose an image
file_path = filedialog.askopenfilename(
    title="Select an image to edit",
    filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
)

if file_path:
    img = Image.open(file_path).convert("RGB")
    edited_img = blackout_left_quarter(img)

    # Save the edited image
    save_path = filedialog.asksaveasfilename(
        title="Choose where to save your new image",
        defaultextension=".jpg",
        filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
    )
    if save_path:
        edited_img.save(save_path)
        print(f"Your modified image has been saved at: {save_path}")
        os.startfile(save_path)
    else:
        print("Saving process was canceled.")
else:
    print("No image was selected. Exiting program.")
