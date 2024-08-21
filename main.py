import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk


def upload_image():
    global img_path, img_label
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if img_path:
        img = Image.open(img_path)  # Open the original image
        img.thumbnail((300, 300))  # Resize image to fit the display area
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img


def add_watermark():
    if not img_path:
        messagebox.showwarning("Warning", "Please upload an image first!")
        return

    # get user input

    watermark_text = watermark_entry.get()
    position_x = int(pos_x_entry.get())
    position_y = int(pos_y_entry.get())

    # Open the original image
    original = Image.open(img_path).convert("RGBA")

    # Make the image editable
    txt = Image.new('RGBA', original.size, (255, 255, 255, 0))

    # Choose a font and size
    font = ImageFont.truetype("arial.ttf", 40)

    # Initialize ImageDraw
    x = ImageDraw.Draw(txt)

    # Add text to image
    x.text((position_x, position_y), watermark_text, font=font, fill=(255, 255, 255, 128))

    # Combine original image with watermark
    watermarked = Image.alpha_composite(original, txt)

    # Convert back to RGB mode and save the result
    watermarked = watermarked.convert("RGB")

    save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"),
                                                        ("BMP files", "*.bmp")])
    if save_path:
        watermarked.save(save_path)
        messagebox.showinfo("Success", f"Watermarked image saved as {save_path}")


# Main window
window = tk.Tk()
window.title("Image Watermarker")

# Create grid layout
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Image Label

img_label = tk.Label(window)
img_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Upload Button
upload_btn = tk.Button(window, text="Upload Image", command=upload_image)
upload_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Watermark Text Entry
tk.Label(window, text="Watermark Text:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
watermark_entry = tk.Entry(window)
watermark_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Position X Entry
tk.Label(window, text="Position X:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
pos_x_entry = tk.Entry(window)
pos_x_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Position Y Entry
tk.Label(window, text="Position Y:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
pos_y_entry = tk.Entry(window)
pos_y_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Add Watermark Button
watermark_btn = tk.Button(window, text="Add Watermark", command=add_watermark)
watermark_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter loop
window.mainloop()
