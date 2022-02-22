from tkinter import *
from PIL import Image, ImageTk
from tkinter import font, filedialog


def is_pressed():

    # The variable photo is a local variable which gets garbage collected after the class is instantiated. Save a
    # reference to the photo. Just add global to the chosen_image definition and it will work
    global new_img

    # Let the user chose a picture by browsing local files. Only png.
    filename = filedialog.askopenfilename(filetypes=[('Png Files', '*.png')])
    chosen_image = Image.open(filename)

    # Resize to fit the canvas size
    formatted_img = chosen_image.resize((500, 500))

    # Make the formatted image as a PhotoImage so it will be displayed
    new_img = ImageTk.PhotoImage(formatted_img)
    canvas.itemconfig(placeholder, image=new_img)


# Window/root
window = Tk()
window.title("Watermark Desktop App")
window.config(padx=100, pady=100, bg="#e0eef2")

# Canvas
canvas = Canvas(width=500, height=500, bg="#e0eef2")
canvas.config(highlightthickness=1, )
canvas.grid(row=0, column=1)

# Placeholder image
img = PhotoImage(file="sticker_5.png")
placeholder = canvas.create_image(0, 0, image=img, anchor="nw")

# Buttons
upload_button = Button(text="Add An Image", command=is_pressed)
upload_button.config(padx=10, pady=10)
upload_button.grid(row=2, column=0)

exit_button = Button(text="Exit application", command=is_pressed)
exit_button.config(padx=10, pady=10)
exit_button.grid(row=2, column=2)

# Text
Label(text="Choose an image and add a label to it", bg="#e0eef2", padx=50, pady=50,
      font=("Helvetica", 20, "bold")).grid(row=1, column=1)

window.mainloop()
