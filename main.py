import tkinter as tk
from tkinter import ttk


class Kalkulator:
    def __init__(self):
        self.zmn1 = None
        self.zmn2 = None
        self.oper = None
        self.suma = None
        self.root = None
        self.root_frame = None
        self.display_text = None

    def ustaw_glowne_okno_na_srodek_ekranu(self):
        """Ustawia środek okna na środek ekranu."""
        screen_width, screen_height = self.pobierz_wymiary_ekranu()
        center_x, center_y = self.ustaw_srodek_ekranu_dla_okna(screen_width, screen_height)
        self.root.geometry(f'{300}x{300}+{center_x}+{center_y}')

    def pobierz_wymiary_ekranu(self):
        """Pobiera wymiary ekranu i zwraca WIDTH, HEIGHT"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        return screen_width, screen_height

    def ustaw_srodek_ekranu_dla_okna(self, screen_width, screen_height):
        """Oblicza punkt środka ekranu dla programu, zwraza X, Y"""
        center_x = int(screen_width / 2 - self.root.winfo_width() / 2)
        center_y = int(screen_height / 2 - self.root.winfo_height() / 2)
        return center_x, center_y

    def ustawienia_programu(self):  # NA PRZYSZŁOŚĆ
        self.root.title("Banalny Kalkulator")  # ustawia tytuł programu
        self.root.resizable(False, False)  # możliwosć zmiany rozmiarów okna myszką
        self.root.attributes('-alpha', 0.9)  # przezroczystość okna 0.0 - przezroczyste
        self.root.attributes('-topmost', 1)  # okno na wierzchu innych okien
        self.root.iconbitmap("./icon.ico")  # ustawia ikone programu
        self.root.eval('tk::PlaceWindow . center')  # sutawia okno na środek ekranu

    def click_num_btn(self, x):
        self.display_text.set(x)

    def stworz_wyswietlacz(self):
        display_frame = ttk.Frame(self.root_frame)
        display_frame.grid(column=0, row=0, sticky="NEWS")
        display = tk.Label(display_frame, anchor="e", textvariable=self.display_text, font=("Arial", 20))
        display.pack(ipady=20, fill="both")

    def stworz_klawisze_cyfr(self, keyboard_frame, pad, ipad):
        ttk.Button(keyboard_frame, text="1", command=lambda: self.click_num_btn(1))\
            .grid(column=0, row=2, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="2", command=lambda: self.click_num_btn(2))\
            .grid(column=1, row=2, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="3", command=lambda: self.click_num_btn(3))\
            .grid(column=2, row=2, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="4", command=lambda: self.click_num_btn(4))\
            .grid(column=0, row=1, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="5", command=lambda: self.click_num_btn(5))\
            .grid(column=1, row=1, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="6", command=lambda: self.click_num_btn(6))\
            .grid(column=2, row=1, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="7", command=lambda: self.click_num_btn(7))\
            .grid(column=0, row=0, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="8", command=lambda: self.click_num_btn(8))\
            .grid(column=1, row=0, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="9", command=lambda: self.click_num_btn(9))\
            .grid(column=2, row=0, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="0", command=lambda: self.click_num_btn(0))\
            .grid(column=0, row=3, padx=pad, pady=pad, ipady=ipad, columnspan=2, sticky="NSWE")

    def stworz_klawisze_operacji(self, keyboard_frame, pad, ipad):
        ttk.Button(keyboard_frame, text="*").grid(column=3, row=0, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="/").grid(column=3, row=1, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="+").grid(column=3, row=2, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="-").grid(column=3, row=3, padx=pad, pady=pad, ipady=ipad)
        ttk.Button(keyboard_frame, text="=").grid(column=2, row=3, padx=pad, pady=pad, ipady=ipad)

    def stworz_klawiature(self):
        pad, ipad = 2, 15
        keyboard_frame = tk.Frame(self.root_frame, bd=8)
        keyboard_frame.grid(column=0, row=1, sticky="e")
        keyboard_frame.columnconfigure(0, weight=1)
        keyboard_frame.rowconfigure(0, weight=1)
        keyboard_frame.grid_propagate(True)
        self.stworz_klawisze_cyfr(keyboard_frame, pad, ipad)
        self.stworz_klawisze_operacji(keyboard_frame, pad, ipad)

    def stworz_glowne_okno(self):
        self.root = tk.Tk()
        self.display_text = tk.StringVar()
        self.root_frame = tk.Frame(self.root)
        self.root_frame.pack()
        self.ustawienia_programu()
        self.stworz_wyswietlacz()
        self.stworz_klawiature()

    def uruchom(self):
        self.stworz_glowne_okno()
        self.root.mainloop()


if __name__ == "__main__":
    Kalkulator().uruchom()
