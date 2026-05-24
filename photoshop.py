# from textwrap import fill
# from turtle import left, right
# from click import option
import tkinter as tk


def setup_gui(root):

    root.title("Photoshop")
    root.geometry("1000x600")

    # configure wheigts of rows and collumns
    """
    i = 0
    for i in range(8):
        root.rowconfigure(i, weight=1)
    h = 0
    for h in range(4):
        root.columnconfigure(h, weight=1)
    """

    # creating frames
    options_frame = tk.LabelFrame(master=root, text="options", bg="lightgrey")
    options_frame.pack(side="left", fill="y")

    button_frame = tk.LabelFrame(master=options_frame, text="buttons", bg="#A9A9A9")
    button_frame.pack(expand=True)

    slider_frame = tk.LabelFrame(master=options_frame, text="slider", bg="#A9A9A9")
    slider_frame.pack(expand=True)

    picture_frame = tk.Frame(master=root, bg="lightgrey")
    picture_frame.pack(side="right", fill="both")

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
    )
    reset.grid(column=1, columnspan=2, row=0, padx=5, pady=5)

    bl_wh = tk.Button(
        master=button_frame,
        text="black/white",
        width=13,
        highlightthickness=0,
    )
    bl_wh.grid(column=0, columnspan=2, row=1, padx=5, pady=5)

    invert = tk.Button(
        master=button_frame,
        text="invert",
        width=13,
        highlightthickness=0,
    )
    invert.grid(column=2, columnspan=2, row=1, padx=5, pady=5)

    save = tk.Button(
        master=button_frame,
        text="save",
        width=16,
        highlightthickness=0,
    )
    save.grid(column=0, columnspan=4, row=7, padx=5, pady=5)

    load = tk.Button(
        master=button_frame,
        text="load",
        width=16,
        highlightthickness=0,
    )
    load.grid(column=0, columnspan=4, row=8, padx=5, pady=5)

    # creating sliders
    Blur = tk.Scale(
        master=slider_frame,
        from_=0,
        to=100,
        orient=tk.HORIZONTAL,
        length=250,
        troughcolor="#333333",
    )
    Blur.grid(column=1, columnspan=3, row=2, padx=5, pady=5)

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
    )
    red.grid(column=1, columnspan=3, row=3, padx=5, pady=5)

    green = tk.Scale(
        master=slider_frame,
        from_=0,
        to=255,
        orient=tk.HORIZONTAL,
        length=250,
        bg="green",
        fg="black",
        activebackground="#88E788",
        highlightthickness=0,
        troughcolor="#333333",
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
