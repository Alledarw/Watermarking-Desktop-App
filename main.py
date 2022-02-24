from tkinter import *
from PIL import Image, ImageTk, ImageGrab
from tkinter import font, filedialog


def exit_program():
    window.quit()


def getter(widget):
    # Choose save location
    result = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=[('PNG', '*.png')])

    # Screenshot window and crop canvas as an image
    # Need some tweaking to work better. Alternative use another method instead of ImageGrab
    x = window.winfo_rootx() + widget.winfo_x()
    new_x = x + 520
    y = window.winfo_rooty() + widget.winfo_y()
    new_y = y + 400
    x1 = new_y + window.winfo_width()
    y1 = new_x + window.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save(result)


def add_watermark():
    # Same process as is_pressed function
    global watermark_img

    filename = filedialog.askopenfilename(filetypes=[('Png Files', '*.png')])
    chosen_image = Image.open(filename)

    formatted_img = chosen_image.resize((150, 150))
    watermark_img = ImageTk.PhotoImage(formatted_img)

    # Setting X and Y to 400, 450 will create the watermark in the bottom right corner
    canvas.create_image(400, 450, image=watermark_img)


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
window.config(bg="#e0eef2")

# Canvas
canvas = Canvas(width=500, height=500, bg="#e0eef2")
canvas.config(highlightthickness=1, )
canvas.grid(row=0, column=0, columnspan=3)

# Placeholder image
img = PhotoImage(file="sticker_5.png")
placeholder = canvas.create_image(0, 0, image=img, anchor="nw")

# Buttons
new_image_button = Button(text="Add An Image", command=is_pressed)
new_image_button.config(padx=10, pady=10, width=15)
new_image_button.grid(row=3, column=0, sticky=W)

watermark_button = Button(text="Add a watermark", command=add_watermark)
watermark_button.config(padx=10, pady=10, width=15)
watermark_button.grid(row=2, column=0, sticky=W)

exit_button = Button(text="Exit application", command=exit_program)
exit_button.config(padx=10, pady=10, width=15)
exit_button.grid(row=3, column=2, sticky=E)

save_button = Button(text="Save", width=15, padx=10, pady=10, command=lambda: getter(canvas)).grid(row=2, column=2,
                                                                                                   sticky=E)

# Labels
# header = Label(text="Choose an image and add a label to it", bg="#e0eef2", padx=50, pady=50,
               #font=("Helvetica", 20, "bold")).grid(row=4, column=1)

window.mainloop()
