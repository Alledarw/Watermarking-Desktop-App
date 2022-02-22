from tkinter import *
from PIL import Image, ImageTk
from tkinter import font, filedialog


def exit_program():
    window.quit()


def submit():
    pass


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
new_image_button = Button(text="Add An Image", command=is_pressed)
new_image_button.config(padx=10, pady=10, width=15)
new_image_button.grid(row=3, column=2)

exit_button = Button(text="Exit application", command=exit_program)
exit_button.config(padx=10, pady=10, width=15)
exit_button.grid(row=2, column=2)

submit_button = Button(text="Submit", width=15, padx=10, pady=10, command=submit).grid(row=5, column=1, sticky=W)

# Labels
header = Label(text="Choose an image and add a label to it", bg="#e0eef2", padx=50, pady=50,
               font=("Helvetica", 20, "bold")).grid(row=1, column=1)
Label(text="Add a text:", bg="#e0eef2", padx=10, pady=10, font=("Helvetica", 15)).grid(row=2, column=0, sticky=W)
Label(text="Add an X position:", bg="#e0eef2", padx=10, pady=10, font=("Helvetica", 15)).grid(row=3, column=0, sticky=W)
Label(text="Add an Y position:", bg="#e0eef2", padx=10, pady=10, font=("Helvetica", 15)).grid(row=4, column=0, sticky=W)

# Entries
# Keep Entry and grid on separate lines otherwise we cant get the input from the entry
watermark_text = Entry()
watermark_text.grid(row=2, column=1, sticky=W)

y_position = Entry()
y_position.grid(row=3, column=1, sticky=W)

x_position = Entry()
x_position.grid(row=4, column=1, sticky=W)

window.mainloop()
