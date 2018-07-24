""" Template for GUIs"""
try:
    # python 3.x
    import tkinter as tk
    # from tkinter import ttk

except ImportError:
    # python 2.x
    import Tkinter as tk


class MainApplication(tk.Frame):

    """ master app """
    # pylint: disable = too-many-ancestors, too-many-instance-attributes, invalid-name

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        """ configure gui settings """
        self.master.title("Your Title Here")
        # self.master.geometry("280x800")
        self.master.resizable(width=True, height=True)

    def create_menus(self):
        """ creating dropdown menus """
        main_menu = tk.Menu(self.master)

        # options menu
        file_menu = tk.Menu(main_menu, tearoff=0)

        main_menu.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=main_menu)

    def _create_circle(self, x, y, r, **kwargs):
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)
    # tk.Canvas.create_circle = _create_circle

    def create_widgets(self):
        """ initalizes widgets """
        canvas_width = 600
        canvas_height = canvas_width
        middle_x = canvas_width / 2
        middle_y = canvas_height / 2
        rect_width = 10
        rect_height = 175

        self.canvas = tk.Canvas(self.master, width=canvas_width, height=canvas_height,
                                borderwidth=0, bg="black")
        self.canvas.grid(row=0, column=0)
        self._create_circle(middle_x, middle_y, 200, fill="white")

        self.canvas.create_rectangle(
            middle_x - rect_width, middle_y, middle_x + rect_width, middle_y + rect_height, fill="black")

        # create quit app button
        tk.Button(
            self.master, text='Quit', command=self.quit_app).grid(
                row=100, column=0)

    def quit_app(self):
        """ closes screen """
        self.master.destroy()


def main():
    """ main function """
    # pylint: disable =
    root = tk.Tk()
    app = MainApplication(root)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.minsize(200, 800)

    # app.pack(fill='both')

    app.mainloop()


if __name__ == "__main__":
    main()
