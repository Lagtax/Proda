import matplotlib.pyplot as plt
import numpy
from sklearn import metrics
from PIL import Image

def show():



    from pathlib import Path


    from tkinter import Tk, Toplevel, Canvas, Entry, Text, Button, PhotoImage

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Tkinter designer\CM\build\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Toplevel()

    window.geometry("1300x768")
    window.configure(bg="#181818")

    canvas = Canvas(
        window,
        bg="#181818",
        height=768,
        width=1300,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        650.0,
        33.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file="C:/Users/moham/Desktop/PRODA NEW/CMSVC.png")
    image_2 = canvas.create_image(
        311.0,
        261.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file="C:/Users/moham/Desktop/PRODA NEW/CMGNB.png")
    image_3 = canvas.create_image(
        918.0,
        598.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file="C:/Users/moham/Desktop/PRODA NEW/CMXGB.png")
    image_4 = canvas.create_image(
        311.0,
        598.0,
        image=image_image_4
    )


    window.resizable(False, False)
    window.mainloop()

