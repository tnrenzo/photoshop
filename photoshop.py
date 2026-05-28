import tkinter as tk
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

def setup_gui(root) -> None:
    root.title("Photoshop")
    root.geometry("1000x600")

    # loading pictures
    edited_image = EditedImage(image_path=f"{PWD}/images/apple.png")
    edit_preview = ImageTk.PhotoImage(edited_image.return_final_as_pil_type())

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
    back = tk.Button(
        master=button_frame,
        text="<--",
        width=4,
        highlightthickness=0,
    )
    back.grid(column=0, columnspan=1, row=0, padx=5, pady=5)

    forward = tk.Button(
        master=button_frame,
        text="-->",
        width=4,
        highlightthickness=0,
    )
    forward.grid(column=3, columnspan=1, row=0, padx=5, pady=5)

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

    # TODO
    save = tk.Button(
        master=button_frame,
        text="save",
        width=16,
        highlightthickness=0,
    )
    save.grid(column=0, columnspan=4, row=7, padx=5, pady=5)

    # TODO
    load = tk.Button(
        master=button_frame,
        text="load",
        width=16,
        highlightthickness=0,
    )
    load.grid(column=0, columnspan=4, row=8, padx=5, pady=5)

    # sliders

    # TODO: UI freezes when blurring with slider, add slider + confirm button
    # TODO: add some way to change blur size + sigma independently (2 sliders or formula?)
    blur = tk.Scale(
        master=slider_frame,
        from_=0,
        to=100,
        orient=tk.HORIZONTAL,
        length=250,
        troughcolor="#333333",
        command=lambda val: (edited_image.gaussian_blur(sigma=int(val)), update_previews(pic1_label, edited_image))
    )
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
        command=lambda val: (edited_image.set_red(rgb_value=int(val)), update_previews(pic1_label, edited_image))
    )
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
        command=lambda val: (edited_image.set_green(rgb_value=int(val)), update_previews(pic1_label, edited_image))

    )
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
        command=lambda val: (edited_image.set_blue(rgb_value=int(val)), update_previews(pic1_label, edited_image))

    )
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
