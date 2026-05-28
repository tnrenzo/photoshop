import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import ImageTk

from manipulation import EditedImage

PWD = Path(__file__).parent

def reset_image(image_obj: EditedImage) -> None:
    image_obj.image_copy = image_obj.original_image_array.copy() # copy() or else its a reference and breaks reset logic, same in manipulation.py

def update_previews(pic_label: tk.Label, image_obj: EditedImage) -> None:
    updated = ImageTk.PhotoImage(image_obj.return_final_as_pil_type())
    pic_label.config(image=updated)
    pic_label.image = updated

def on_slider_release(slider_label: tk.Label, image_obj: EditedImage):
        image_obj.save_edit_state()
        update_previews(slider_label, image_obj)



def setup_gui(root) -> None:
    root.title("Photoshop")
    root.geometry("1280x720") # 720p

    # loading pictures
    edited_image = EditedImage()
    edit_preview = None

    # we don't have an image path right now so we need a handler to help us
    def open_image_first_launch():
        nonlocal edited_image
        file_path = filedialog.askopenfilename(
            initialdir=PWD,
            title="Select image file",
            filetypes=[("Image Files", ("*.png", "*.jpg", "*.jpeg")), ("All Files", "*")]
        )
        if file_path:
            edited_image.open_image(file_path) # now load the real image
            edit_preview = ImageTk.PhotoImage(edited_image.return_final_as_pil_type())

    open_image_first_launch()

    def open_image(image_obj: EditedImage):
        nonlocal edited_image
        nonlocal edit_preview
        nonlocal pic1_label
        # get file path
        file_path = filedialog.askopenfilename(
            initialdir=PWD,
            title="Select image file",
            filetypes=[("Image Files", ("*.png", "*.jpg", "*.jpeg")), ("All Files", "*")]
        )
        if file_path:
            print(f"Opened: {file_path}")
            image_obj.open_image(file_path)
            edit_preview = ImageTk.PhotoImage(image_obj.return_final_as_pil_type())
            update_previews(pic1_label, edited_image)

    def save_image(image_obj: EditedImage):
        # get file path
        file_path = filedialog.asksaveasfilename(
            initialdir=PWD,
            title="Save Image",
            filetypes=[("Image Files", ("*.png", "*.jpg", "*.jpeg")), ("All Files", "*")]
        )
        if file_path:
            print(f"Saved to: {file_path}")
            image_obj.save_image(file_path)

    # creating frames
    options_frame = tk.LabelFrame(master=root, text="options", bg="lightgrey")
    options_frame.pack(side="left", fill="y")

    button_frame = tk.LabelFrame(master=options_frame, text="buttons", bg="#A9A9A9")
    button_frame.pack(expand=True)

    slider_frame = tk.LabelFrame(master=options_frame, text="slider", bg="#A9A9A9")
    slider_frame.pack(expand=True)

    picture_frame = tk.LabelFrame(master=root, text="pictures", bg="lightgrey")
    picture_frame.pack(side="right", fill="both")

    # show pictures
    pic1_label = tk.Label(picture_frame, image=edit_preview)
    pic1_label.image = edit_preview
    pic1_label.pack(side="top")

    # creating buttons
    undo = tk.Button(
        master=button_frame,
        text="<--",
        width=4,
        highlightthickness=0,
        command=lambda: (edited_image.undo_edit(), update_previews(pic1_label, edited_image))
    )
    undo.grid(column=0, columnspan=1, row=0, padx=5, pady=5)

    redo = tk.Button(
        master=button_frame,
        text="-->",
        width=4,
        highlightthickness=0,

        command=lambda: (edited_image.redo_edit(), update_previews(pic1_label, edited_image))
    )
    redo.grid(column=3, columnspan=1, row=0, padx=5, pady=5)

    reset = tk.Button(
        master=button_frame,
        text="reset",
        width=14,
        highlightthickness=0,
        command=lambda: (reset_image(edited_image), update_previews(pic1_label, edited_image))
    )
    reset.grid(column=1, columnspan=2, row=0, padx=5, pady=5)

    black_white = tk.Button(
        master=button_frame,
        text="black/white",
        width=13,
        highlightthickness=0,
        command=lambda: (edited_image.grayscale(), update_previews(pic1_label, edited_image))
    )
    black_white.grid(column=0, columnspan=2, row=1, padx=5, pady=5)

    invert = tk.Button(
        master=button_frame,
        text="invert",
        width=13,
        highlightthickness=0,
        command=lambda: (edited_image.invert(), update_previews(pic1_label, edited_image))
    )
    invert.grid(column=2, columnspan=2, row=1, padx=5, pady=5)

    save = tk.Button(
        master=button_frame,
        text="save",
        width=16,
        highlightthickness=0,
        command=lambda: save_image(edited_image)
    )
    save.grid(column=0, columnspan=4, row=7, padx=5, pady=5)

    load = tk.Button(
        master=button_frame,
        text="load",
        width=16,
        highlightthickness=0,
        command=lambda: open_image(edited_image)
    )
    load.grid(column=0, columnspan=4, row=8, padx=5, pady=5)

    # sliders
    blur = tk.Scale(
        master=slider_frame,
        from_=0,
        to=100,
        orient=tk.HORIZONTAL,
        length=250,
        troughcolor="#333333",
    )
    blur.bind("<ButtonRelease-1>", lambda e: (edited_image.gaussian_blur(sigma=blur.get(), size=int(blur.get()/2)), update_previews(pic1_label, edited_image)))
    blur.grid(column=1, columnspan=3, row=2, padx=5, pady=5)

    red = tk.Scale(
        master=slider_frame,
        from_=0,
        to=255,
        orient=tk.HORIZONTAL,
        length=250,
        bg="red",
        fg="black",
        activebackground="#FF7F7F",
        highlightthickness=0,
        troughcolor="#333333",
        command=lambda val: edited_image.set_red(rgb_value=int(val))
    )
    red.bind("<ButtonRelease-1>", lambda e: on_slider_release(pic1_label, edited_image))
    red.grid(column=1, columnspan=3, row=3, padx=5, pady=5)

    green = tk.Scale(
        master=slider_frame,
        from_=0,
        to=255,
        orient=tk.HORIZONTAL,
        length=250,
        bg="#4CBB17",
        fg="black",
        activebackground="#88E788",
        highlightthickness=0,
        troughcolor="#333333",
        command=lambda val: edited_image.set_green(rgb_value=int(val))
    )
    green.bind("<ButtonRelease-1>", lambda e: on_slider_release(pic1_label, edited_image))
    green.grid(column=1, columnspan=3, row=4, padx=5, pady=5)

    blue = tk.Scale(
        master=slider_frame,
        from_=0,
        to=255,
        orient=tk.HORIZONTAL,
        length=250,
        bg="blue",
        fg="black",
        activebackground="#90D5FF",
        highlightthickness=0,
        troughcolor="#333333",
        command=lambda val: edited_image.set_blue(rgb_value=int(val))
    )
    blue.bind("<ButtonRelease-1>", lambda e: on_slider_release(pic1_label, edited_image))
    blue.grid(column=1, columnspan=3, row=5, padx=5, pady=5)

    # creating text
    blur_label = tk.Label(master=slider_frame, text="Blur", bg="#A9A9A9")
    blur_label.grid(column=0, row=2, padx=5, pady=5)

    red_label = tk.Label(master=slider_frame, text="R", bg="#A9A9A9")
    red_label.grid(column=0, row=3, padx=5, pady=5)

    green_label = tk.Label(master=slider_frame, text="G", bg="#A9A9A9")
    green_label.grid(column=0, row=4, padx=5, pady=5)

    blue_label = tk.Label(master=slider_frame, text="B", bg="#A9A9A9")
    blue_label.grid(column=0, row=5, padx=5, pady=5)



def main():

    # tkinter setup
    root = tk.Tk()
    setup_gui(root)

    # run mainloop
    root.mainloop()


main()
