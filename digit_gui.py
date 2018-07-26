""" Template for GUIs"""
try:
    # python 3.x
    import tkinter as tk
    # from tkinter import ttk

except ImportError:
    # python 2.x
    import Tkinter as tk

import math
import time
import single_clock as sc


# pylint: disable = too-many-ancestors, too-many-instance-attributes, invalid-name

class MainApplication(tk.Frame):

    """ master app """

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.configure_gui()
        self.create_widgets()
        self.initialize_clocks()

    def configure_gui(self):
        """ configure gui settings """
        self.master.title("Clocks on Clocks")
        # self.master.geometry("280x800")
        self.master.resizable(width=True, height=True)

    def create_widgets(self):
        """ initalizes widgets """

        self.clock1_gui = ClockCanvas(self.master, 200)
        self.clock1_gui.grid(row=0, column=0)

        self.clock2_gui = ClockCanvas(self.master, 200)
        self.clock2_gui.grid(row=0, column=1)

        self.clock3_gui = ClockCanvas(self.master, 200)
        self.clock3_gui.grid(row=1, column=0)

        self.clock4_gui = ClockCanvas(self.master, 200)
        self.clock4_gui.grid(row=1, column=1)

        self.clock5_gui = ClockCanvas(self.master, 200)
        self.clock5_gui.grid(row=2, column=0)

        self.clock6_gui = ClockCanvas(self.master, 200)
        self.clock6_gui.grid(row=2, column=1)

        # create quit app button
        tk.Button(
            self.master, text='Quit', command=self.quit_app).grid(
                row=100, column=0, columnspan=2)

    def quit_app(self):
        """ closes screen """
        self.master.destroy()

    def initialize_clocks(self):
        """ initializes all clocks """
        self.clock1_cmd = sc.SingleClock(0, 90)
        self.clock2_cmd = sc.SingleClock(0, 90)
        self.clock3_cmd = sc.SingleClock(0, 90)
        self.clock4_cmd = sc.SingleClock(0, 90)
        self.clock5_cmd = sc.SingleClock(0, 90)
        self.clock6_cmd = sc.SingleClock(0, 90)

    def set_goal(self, dest_config, motion_time):
        """ set motion parameters given a destination config """
        self.clock1_cmd.set_goal(dest_config[0][0], dest_config[0][1], motion_time)
        self.clock2_cmd.set_goal(dest_config[1][0], dest_config[1][1], motion_time)
        self.clock3_cmd.set_goal(dest_config[2][0], dest_config[2][1], motion_time)
        self.clock4_cmd.set_goal(dest_config[3][0], dest_config[3][1], motion_time)
        self.clock5_cmd.set_goal(dest_config[4][0], dest_config[4][1], motion_time)
        self.clock6_cmd.set_goal(dest_config[5][0], dest_config[5][1], motion_time)

    def draw(self):
        """ dynamically draws a picture with clocks given the config array
            config: [(a1, a2), (b1, b2), (c1, c2), (d1, d2), (e1, e2), (f1, f2)]
        """
        c1_a, c1_b = self.clock1_cmd.goto_pos()
        c2_a, c2_b = self.clock2_cmd.goto_pos()
        c3_a, c3_b = self.clock3_cmd.goto_pos()
        c4_a, c4_b = self.clock4_cmd.goto_pos()
        c5_a, c5_b = self.clock5_cmd.goto_pos()
        c6_a, c6_b = self.clock6_cmd.goto_pos()

        self.clock1_gui.draw_hands(c1_a, c1_b)
        self.clock2_gui.draw_hands(c2_a, c2_b)
        self.clock3_gui.draw_hands(c3_a, c3_b)
        self.clock4_gui.draw_hands(c4_a, c4_b)
        self.clock5_gui.draw_hands(c5_a, c5_b)
        self.clock6_gui.draw_hands(c6_a, c6_b)

    def motion_complete(self):
        """ checks if all clocks have reached goal """
        return bool(self.clock1_cmd.hand_1.motion_complete and
                    self.clock1_cmd.hand_2.motion_complete
                    and self.clock1_cmd.hand_1.motion_complete and
                    self.clock1_cmd.hand_1.motion_complete
                    and self.clock1_cmd.hand_1.motion_complete and
                    self.clock1_cmd.hand_1.motion_complete)


class ClockCanvas(tk.Frame):

    """ canvas for an individual clock """

    def __init__(self, master, canvas_width, hand1_angle=0, hand2_angle=0):
        tk.Frame.__init__(self, master)

        self.master = master
        self.canvas_width = canvas_width
        self.canvas_height = canvas_width
        self.clock_radius = 0.45 * self.canvas_width
        self.hand_radius = 0.95 * self.clock_radius
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
        self._create_circle(self.middle_x, self.middle_y, 15, fill="blue")

        h1_x_pos, h1_y_pos = self.angle_to_coord(hand1_angle)
        h2_x_pos, h2_y_pos = self.angle_to_coord(hand2_angle)

        self.hand1 = self.canvas.create_line(
            self.middle_x, self.middle_y, self.middle_x + h1_x_pos,
            self.middle_y - h1_y_pos, width=self.hand_width)

        self.hand2 = self.canvas.create_line(
            self.middle_x, self.middle_y, self.middle_x + h2_x_pos,
            self.middle_y - h2_y_pos, width=self.hand_width)

    def draw_hands(self, hand1_angle, hand2_angle):
        """draws clock hands"""

        # pylint: disable = attribute-defined-outside-init

        self.canvas.delete(self.hand1)
        self.canvas.delete(self.hand2)

        h1_x_pos, h1_y_pos = self.angle_to_coord(hand1_angle)
        h2_x_pos, h2_y_pos = self.angle_to_coord(hand2_angle)

        self.hand1 = self.canvas.create_line(self.middle_x, self.middle_y,
                                             self.middle_x + h1_x_pos, self.middle_y - h1_y_pos,
                                             width=self.hand_width, fill="black")

        self.hand2 = self.canvas.create_line(self.middle_x, self.middle_y,
                                             self.middle_x + h2_x_pos, self.middle_y - h2_y_pos,
                                             width=self.hand_width, fill="black")

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


def timer(t1):
    """ stopwatch """
    return time.time() - t1


def main():
    """ main function """
    # pylint: disable = too-many-locals, too-many-statements
    root = tk.Tk()
    app = MainApplication(root)

    home_pos = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    number_1 = [(-135, -135), (-180, -180), (-135, -135), (0, -180), (-135, -135), (0, 0)]
    number_2 = [(90, 90), (-90, 180), (180, 90), (-90, 0), (0, 90), (-90, -90)]
    number_3 = [(90, 90), (-90, 180), (90, 90), (-90, 0), (90, 90), (-90, 0)]
    number_4 = [(180, 180), (180, 180), (0, 90), (0, 180), (-135, -135), (0, 1)]
    number_5 = [(90, 180), (-90, -90), (0, 90), (-90, 180), (90, 90), (-90, 0)]
    number_6 = [(90, 180), (-90, -90), (0, 180), (-90, 180), (0, 90), (-90, 0)]
    number_7 = [(90, 90), (-90, -90), (-135, -135), (0, 180), (-135, -135), (0, 0)]
    number_8 = [(90, 180), (-90, 180), (0, 90), (-90, 0), (0, 90), (-90, 0)]
    number_9 = [(90, 180), (-90, 180), (0, 90), (-90, 0), (90, 90), (-90, 0)]
    number_0 = [(90, 180), (-90, 180), (0, 180), (0, 180), (0, 90), (-90, 0)]

    move_time = 1500
    app.set_goal(home_pos, move_time)
    time_1 = time.time()
    quit_flag = False
    while quit_flag is False:
        app.draw()
        app.update_idletasks()
        app.update()

        if app.motion_complete() is True and timer(time_1) > 2 and timer(time_1) < 2.01:
            app.set_goal(number_1, move_time)
            print("goal reacheed")

        if app.motion_complete() is True and timer(time_1) > 5 and timer(time_1) < 5.01:
            app.set_goal(number_2, move_time)
            print("goal reacheed")

        if app.motion_complete() is True and timer(time_1) > 8 and timer(time_1) < 8.01:
            app.set_goal(number_3, move_time)
            print("goal reached")
        if app.motion_complete() is True and timer(time_1) > 11 and timer(time_1) < 11.01:
            app.set_goal(number_4, move_time)
            print("goal reached")
        if app.motion_complete() is True and timer(time_1) > 14 and timer(time_1) < 14.01:
            app.set_goal(number_5, move_time)
            print("goal reacheed")

        if app.motion_complete() is True and timer(time_1) > 17 and timer(time_1) < 17.01:
            app.set_goal(number_6, move_time)
            print("goal reached")
        if app.motion_complete() is True and timer(time_1) > 20 and timer(time_1) < 20.01:
            app.set_goal(number_7, move_time)
            print("goal reacheed")

        if app.motion_complete() is True and timer(time_1) > 23 and timer(time_1) < 23.01:
            app.set_goal(number_8, move_time)
            print("goal reached")
        if app.motion_complete() is True and timer(time_1) > 26 and timer(time_1) < 26.01:
            app.set_goal(number_9, move_time)
            print("goal reacheed")

        if app.motion_complete() is True and timer(time_1) > 29 and timer(time_1) < 29.01:
            app.set_goal(number_0, move_time)
            print("goal reacheed")

        if app.motion_complete() is True and timer(time_1) > 31 and timer(time_1) < 31.5:
            print("goal reached")
            quit_flag = True

    time.sleep(2)
    app.quit_app()


if __name__ == "__main__":
    main()
