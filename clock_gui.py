""" Template for GUIs"""
try:
    # python 3.x
    import tkinter as tk
    # from tkinter import ttk

except ImportError:
    # python 2.x
    import Tkinter as tk

import math


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
        self.master.title("Clocks on Clocks")
        # self.master.geometry("280x800")
        self.master.resizable(width=True, height=True)

    def create_menus(self):
        """ creating dropdown menus """
        main_menu = tk.Menu(self.master)

        # options menu
        file_menu = tk.Menu(main_menu, tearoff=0)

        main_menu.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=main_menu)


    def create_widgets(self):
        """ initalizes widgets """

        self.clock1 = ClockCanvas(self.master,200)
        self.clock1.grid(row=0,column=0)

        self.clock2 = ClockCanvas(self.master,200)
        self.clock2.grid(row=0,column=1)

        self.clock3 = ClockCanvas(self.master,200)
        self.clock3.grid(row=1,column=0)

        self.clock4 = ClockCanvas(self.master,200)
        self.clock4.grid(row=1,column=1)

        self.clock5 = ClockCanvas(self.master,200)
        self.clock5.grid(row=2,column=0)

        self.clock6 = ClockCanvas(self.master,200)
        self.clock6.grid(row=2,column=1)

        # create quit app button
        tk.Button(
            self.master, text='Quit', command=self.quit_app).grid(
                row=100, column=0, columnspan=2)

    def quit_app(self):
        """ closes screen """
        self.master.destroy()


class ClockCanvas(tk.Frame):
    """ canvas for an individual clock """
    def __init__(self, master, canvas_width, hand1_angle=0, hand2_angle=0):
        tk.Frame.__init__(self, master, bg='#626262')

        self.master = master
        self.canvas_width = canvas_width
        self.canvas_height = canvas_width
        self.clock_radius = 0.45 * self.canvas_width 
        self.hand_radius = 0.8 * self.clock_radius
        self.hand_width = 8

        self.middle_x = self.canvas_width / 2
        self.middle_y = self.canvas_height / 2


        self.initialize_canvas()
        hand1_angle = 0
        hand2_angle = 90
        self.initialize_clockface(hand1_angle, hand2_angle)




    def initialize_canvas(self):
        """ initialize canvas for clock to be drawn """

        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height,
                                borderwidth=0, bg="black")
        self.canvas.grid(row=0, column=0)


    def initialize_clockface(self, hand1_angle, hand2_angle):
        """ draws clock with initial hand positions """
        self._create_circle(self.middle_x, self.middle_y, self.clock_radius, fill="white")
        self._create_circle(self.middle_x, self.middle_y, 18, fill="blue")

        h1_x_pos, h1_y_pos = self.angle_to_coord(hand1_angle)
        h2_x_pos, h2_y_pos = self.angle_to_coord(hand2_angle)


        self.hand1 = self.canvas.create_line(self.middle_x, self.middle_y, self.middle_x + h1_x_pos, self.middle_y - h1_y_pos, width=self.hand_width)

        self.hand2 = self.canvas.create_line(self.middle_x, self.middle_y, self.middle_x + h2_x_pos, self.middle_y - h2_y_pos, width=self.hand_width)

    def draw_hands(self, hand1_angle, hand2_angle):
        """draws clock hands"""

        self.canvas.delete(self.hand1)
        self.canvas.delete(self.hand2)

        h1_x_pos, h1_y_pos = self.angle_to_coord(hand1_angle)
        h2_x_pos, h2_y_pos = self.angle_to_coord(hand2_angle)


        self.hand1 = self.canvas.create_line(self.middle_x, self.middle_y,
                self.middle_x + h1_x_pos, self.middle_y - h1_y_pos, width=self.hand_width, fill="black")

        self.hand2 = self.canvas.create_line(self.middle_x, self.middle_y,
                self.middle_x + h2_x_pos, self.middle_y - h2_y_pos, width=self.hand_width, fill="red")

    def angle_to_coord(self, angle):
        """ determines x, y position for a given angle """
        # cos(angle) = y/hyp
        # sin(angle) = x/hyp
        x_pos = self.hand_radius * math.sin(math.radians(angle))
        y_pos = self.hand_radius * math.cos(math.radians(angle))

        return x_pos, y_pos






    def _create_circle(self, x, y, r, **kwargs):
        """ draw a circle easily """
        self.canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)




def main():
    """ main function """
    # pylint: disable =
    root = tk.Tk()
    app = MainApplication(root)

    # drawing 1
    # app.clock1.draw_hands(-135, -135)
    # app.clock2.draw_hands(0, -180)
    # app.clock3.draw_hands(-135, -135)
    # app.clock4.draw_hands(0, -180)
    # app.clock5.draw_hands(-135, -135)
    # app.clock6.draw_hands(0, -180)

    # drawing 2
    # app.clock1.draw_hands(90, 90)
    # app.clock2.draw_hands(-90, 180)
    # app.clock3.draw_hands(180, 90)
    # app.clock4.draw_hands(-90, 0)
    # app.clock5.draw_hands(0, 90)
    # app.clock6.draw_hands(-90, -90)

    # drawing 3
    # app.clock1.draw_hands(90, 90)
    # app.clock2.draw_hands(-90, 180)
    # app.clock3.draw_hands(90, 90)
    # app.clock4.draw_hands(-90, 0)
    # app.clock5.draw_hands(90, 90)
    # app.clock6.draw_hands(-90, 0)

    # drawing 4
    # app.clock1.draw_hands(180, 180)
    # app.clock2.draw_hands(180, 180)
    # app.clock3.draw_hands(0, 90)
    # app.clock4.draw_hands(0, 180)
    # app.clock5.draw_hands(-135, -135)
    # app.clock6.draw_hands(0, 180)

    # drawing 5
    # app.clock1.draw_hands(90, 180)
    # app.clock2.draw_hands(-90, -90)
    # app.clock3.draw_hands(0, 90)
    # app.clock4.draw_hands(-90, 180)
    # app.clock5.draw_hands(90, 90)
    # app.clock6.draw_hands(-90, 0)

    # drawing 6
    app.clock1.draw_hands(90, 180)
    app.clock2.draw_hands(-90, -90)
    app.clock3.draw_hands(0, 180)
    app.clock4.draw_hands(-90, 180)
    app.clock5.draw_hands(0, 90)
    app.clock6.draw_hands(-90, 0)

    # drawing 7
    # app.clock1.draw_hands(90, 90)
    # app.clock2.draw_hands(-90, -90)
    # app.clock3.draw_hands(-135, -135)
    # app.clock4.draw_hands(-90, 180)
    # app.clock5.draw_hands(90, 90)
    # app.clock6.draw_hands(-90, 0)

    # drawing 8
    # app.clock1.draw_hands(90, 180)
    # app.clock2.draw_hands(-90, 180)
    # app.clock3.draw_hands(0, 90)
    # app.clock4.draw_hands(-90, 0)
    # app.clock5.draw_hands(0, 90)
    # app.clock6.draw_hands(-90, 0)

    # drawing 9
    # app.clock1.draw_hands(90, 180)
    # app.clock2.draw_hands(-90, 180)
    # app.clock3.draw_hands(0, 90)
    # app.clock4.draw_hands(-90, 0)
    # app.clock5.draw_hands(90, 90)
    # app.clock6.draw_hands(-90, 0)

    # drawing 0
    # app.clock1.draw_hands(90, 180)
    # app.clock2.draw_hands(-90, 180)
    # app.clock3.draw_hands(0, 180)
    # app.clock4.draw_hands(0, 180)
    # app.clock5.draw_hands(0, 90)
    # app.clock6.draw_hands(-90, 0)

    app.mainloop()


if __name__ == "__main__":
    main()
