import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw


# image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)

    # if file is selected
    if len(path):
        img = Image.open(path)
        # img = img.resize((200, 200))
        pic = ImageTk.PhotoImage(img)

        # re-sizing the app window in order to fit picture
        window.geometry("560x300")
        watermark_image = img.copy()
        draw = ImageDraw.Draw(watermark_image)
        # ("font type",font size)
        w, h = img.size
        x, y = int(w / 4), int(h / 4)
        if x > y:
            font_size = y
        elif y > x:
            font_size = x
        else:
            font_size = x

        font = ImageFont.truetype("arial.ttf", int(font_size / 6))

        # add Watermark
        # (0,0,0)-black color text
        draw.text((x, y), "Anything", fill=(0, 0, 0), font=font, anchor='ms')
        watermark_image.show()

    # if no file is selected, then we are displaying below message
    else:
        print("No file is Choosen !! Please choose a file.")


window = tk.Tk()
window.title("Image Watermarking App")
window.minsize(width=500, height=500)

welcome_label = tk.Label(text="Welcome to the Image Watermarking App", font=("Calibri", 20, "bold"))
welcome_label.grid(row=0, column=1)

new_label = tk.Label(text="Upload your image here:")
new_label.grid(row=1, column=1)

uploadButton = tk.Button(window, text="Locate Image", command=imageUploader)
uploadButton.grid(row=3, column=1)

window.mainloop()