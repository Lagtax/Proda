def show():
    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Toplevel, Canvas, Entry, Text, Button, PhotoImage

    OUTPUT_PATH1 = Path(__file__).parent
    ASSETS_PATH1 = OUTPUT_PATH1 / Path(r"E:\Tkinter designer\TP1\build\assets\frame0")

    def relative_to_assets1(path: str) -> Path:
        return ASSETS_PATH1 / Path(path)

    window1 = Tk()

    window1.geometry("700x512")
    window1.configure(bg="#1E1E1E")

    canvas1 = Canvas(
        window1,
        bg="#1E1E1E",
        height=512,
        width=700,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas1.place(x=0, y=0)
    canvas1.create_text(
        146.0,
        77.0,
        anchor="nw",
        text="PROGRESS",
        fill="#FFFFFF",
        font=("Actor Regular", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets1("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=401.0,
        y=330.0,
        width=153.0,
        height=42.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets1("image_1.png"))
    image_1 = canvas1.create_image(
        350.0,
        134.0,
        image=image_image_1
    )
    window1.resizable(False, False)
    window1.mainloop()
