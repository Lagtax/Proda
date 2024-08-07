
from PIL import Image
def showres(pred,img_path):

    im = Image.open(img_path)
    im = im.resize((287,225))
    im.save("C:/Users/moham/Desktop/PRODA NEW/Res.png")
    from pathlib import Path

    from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Tkinter designer\New Result\build\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    if (pred == 0):
        res = "NON-DEFECTIVE"
        col = "#09FF4E"
    else:
        res = "DEFECTIVE"
        col = "#FF0927"
    window = Tk()

    window.geometry("1024x768")
    window.configure(bg="#181818")

    canvas = Canvas(
        window,
        bg="#181818",
        height=768,
        width=1024,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        580.0,
        68.0,
        1024.0,
        768.0,
        fill="#75D6FE",
        outline="")

    canvas.create_text(
        29.0,
        142.0,
        anchor="nw",
        text="THE PRODUCT IS PREDICTED TO BE",
        fill="#FFFFFF",
        font=("Inter", 25 * -1)
    )

    canvas.create_text(
        69.0,
        234.0,
        anchor="nw",
        text=res,
        fill=col,
        font=("Inter", 25 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        523.0,
        34.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=window.destroy,
        relief="flat"
    )
    button_1.place(
        x=707.0,
        y=644.0,
        width=254.0,
        height=70.0
    )

    image_image_2 = PhotoImage(
        file="C:/Users/moham/Desktop/PRODA NEW/Res.png")
    image_2 = canvas.create_image(
        817.0,
        271.0,
        image=image_image_2
    )
    window.resizable(False, False)
    window.mainloop()


