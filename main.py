import tkinter as tk
from tkinter import ttk


class NumButton(ttk.Button):
    def __init__(self, master, numer, kalkulator):
        super().__init__(master, text=str(numer), command=lambda: kalkulator.click_num_btn(numer))


class OperButton(ttk.Button):
    def __init__(self, master, symbol, kalkulator):
        super().__init__(master, text=str(symbol), command=lambda: kalkulator.click_oper_btn(symbol))


class Operacja:
    def __init__(self):
        self.oper = None

    def set(self, symbol):
        if symbol != "=":
            self.oper = symbol

    def clear(self):
        self.oper = None

    def oblicz(self, zmn1, zmn2):
        x = None
        if self.oper == "+":
            x = zmn1 + zmn2
        elif self.oper == "-":
            x = zmn1 - zmn2
        elif self.oper == "*":
            x = zmn1 * zmn2
        elif self.oper == "/":
            x = zmn1 // zmn2
        return int(x)

    def drop(self):
        return self.oper


class Zmienna:
    def __init__(self):
        self.zmn = None

    def set(self, zmienna):
        self.zmn = int(zmienna)

    def clear(self):
        self.zmn = None

    def add(self, var):
        x = str(self.zmn) + str(var)
        self.set(x)

    def drop(self):
        return self.zmn


class Kalkulator:
    def __init__(self):
        self.zmn1 = Zmienna()
        self.zmn2 = Zmienna()
        self.oper = Operacja()
        self.suma = None
        self.root = None
        self.root_frame = None
        self.display_text = None

    def ustawienia_programu(self):
        self.root.title("Banalny Kalkulator")  # ustawia tytuł programu
        self.root.resizable(False, False)  # możliwosć zmiany rozmiarów okna myszką
        self.root.attributes('-alpha', 0.9)  # przezroczystość okna 0.0 - przezroczyste
        self.root.attributes('-topmost', 1)  # okno na wierzchu innych okien
        self.root.iconbitmap("./icon.ico")  # ustawia ikone programu
        self.root.eval('tk::PlaceWindow . center')  # sutawia okno na środek ekranu

    def click_num_btn(self, x):
        if self.oper.drop() is None:
            if self.zmn1.drop() is None:
                self.zmn1.set(x)
                self.suma = None
            elif self.zmn1.drop() is not None:
                self.zmn1.add(x)
            self.display_text.set(self.zmn1.drop())
        elif self.oper.drop() is not None:
            if self.zmn2.drop() is None:
                self.zmn2.set(x)
            elif self.zmn2.drop() is not None:
                self.zmn2.add(x)
            self.display_text.set(self.zmn2.drop())

    def wykonaj_obliczenia(self):
        self.suma = self.oper.oblicz(self.zmn1.drop(), self.zmn2.drop())
        self.zmn1.clear()
        self.zmn2.clear()
        self.oper.clear()
        self.display_text.set(self.suma)

    def click_oper_btn(self, symbol):
        if symbol != "=":  # Czy NIE JEST to znak równości
            if self.zmn1.drop() is None:  # ZMN1 = None
                if self.suma is None:
                    pass
                elif self.suma is not None:
                    self.zmn1.set(self.suma)
                    self.oper.set(symbol)
            elif self.zmn1.drop() is not None:  # ZMN1 != None
                if self.zmn2.drop() is None:
                    self.oper.set(symbol)
                elif self.zmn2.drop() is not None:
                    self.wykonaj_obliczenia()
                    self.zmn1.set(self.suma)
                    self.oper.set(symbol)
        elif symbol == "=":  # Czy JEST to znak równości
            if self.zmn1.drop() is not None and self.zmn2.drop() is not None:
                self.wykonaj_obliczenia()

    def stworz_wyswietlacz(self):
        display_frame = ttk.Frame(self.root_frame)
        display_frame.grid(column=0, row=0, sticky="NEWS")
        display = tk.Label(display_frame, anchor="e", textvariable=self.display_text, font=("Arial", 20))
        display.pack(ipady=20, fill="both")

    def stworz_klawisze_cyfr(self, keyboard_frame, pad, ipad):
        NumButton(keyboard_frame, 1, self).grid(column=0, row=2, padx=pad, pady=pad, ipady=ipad)
        NumButton(keyboard_frame, 2, self).grid(column=1, row=2, padx=pad, pady=pad, ipady=ipad)
        NumButton(keyboard_frame, 3, self).grid(column=2, row=2, padx=pad, pady=pad, ipady=ipad)
        NumButton(keyboard_frame, 4, self).grid(column=0, row=1, padx=pad, pady=pad, ipady=ipad)
        NumButton(keyboard_frame, 5, self).grid(column=1, row=1, padx=pad, pady=pad, ipady=ipad)
        NumButton(keyboard_frame, 6, self).grid(column=2, row=1, padx=pad, pady=pad, ipady=ipad)
        NumButton(keyboard_frame, 7, self).grid(column=0, row=0, padx=pad, pady=pad, ipady=ipad)
        NumButton(keyboard_frame, 8, self).grid(column=1, row=0, padx=pad, pady=pad, ipady=ipad)
        NumButton(keyboard_frame, 9, self).grid(column=2, row=0, padx=pad, pady=pad, ipady=ipad)
        NumButton(keyboard_frame, 0, self).grid(column=0, row=3, padx=pad, pady=pad, ipady=ipad, columnspan=2,
                                                sticky="NSWE")

    def stworz_klawisze_operacji(self, keyboard_frame, pad, ipad):
        OperButton(keyboard_frame, "+", self).grid(column=3, row=2, padx=pad, pady=pad, ipady=ipad)
        OperButton(keyboard_frame, "-", self).grid(column=3, row=3, padx=pad, pady=pad, ipady=ipad)
        OperButton(keyboard_frame, "*", self).grid(column=3, row=0, padx=pad, pady=pad, ipady=ipad)
        OperButton(keyboard_frame, "/", self).grid(column=3, row=1, padx=pad, pady=pad, ipady=ipad)
        OperButton(keyboard_frame, "=", self).grid(column=2, row=3, padx=pad, pady=pad, ipady=ipad)

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