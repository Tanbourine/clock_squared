""" GUI for colon """
try:
    # python 3.x
    import tkinter as tk
    # from tkinter import ttk

except ImportError:
    # python 2.x
    import Tkinter as tk

import time
import single_clock as sc
import clock_canvas as cgui
import clock_config as cconfig


# pylint: disable = too-many-ancestors, too-many-instance-attributes, invalid-name

class ColonGUI(tk.Frame):

    """ master app """

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.dest_config = cconfig.HOME_POS
        self.digit_complete = False
        self.clock_size = cconfig.CLOCK_SIZE

        self.create_widgets()
        self.initialize_clocks()

    def create_widgets(self):
        """ initalizes widgets """

        self.clock1_gui = cgui.ClockCanvas(self, self.clock_size)
        self.clock1_gui.grid(row=0, column=0)

        self.clock2_gui = cgui.ClockCanvas(self, self.clock_size)
        self.clock2_gui.grid(row=1, column=0)

        self.clock3_gui = cgui.ClockCanvas(self, self.clock_size)
        self.clock3_gui.grid(row=2, column=0)

        self.clock_gui_array = [self.clock1_gui, self.clock2_gui, self.clock3_gui]


    def quit_app(self):
        """ closes screen """
        self.master.destroy()

    def initialize_clocks(self):
        """ initializes all clocks """

        self.clock1_cmd = sc.SingleClock(-90, 90)
        self.clock2_cmd = sc.SingleClock(-90, 90)
        self.clock3_cmd = sc.SingleClock(-90, 90)

        self.clock_cmd_array = [self.clock1_cmd, self.clock2_cmd, self.clock3_cmd]

    def set_goal(self, dest_config, motion_time):
        """ set motion parameters given a destination config """
        self.dest_config = dest_config
        self.digit_complete = False

        for i, clock in enumerate(self.clock_cmd_array):
            clock.set_goal(dest_config[i][0], dest_config[i][1], motion_time)

    def draw(self):
        """ dynamically draws a picture with clocks given the config array
            config: [(a1, a2), (b1, b2), (c1, c2), (d1, d2), (e1, e2), (f1, f2)]
        """
        # pylint: disable = too-many-boolean-expressions, bad-indentation
        if self.clock1_cmd.motion_complete and self.clock2_cmd.motion_complete and \
                self.clock3_cmd.motion_complete:
                    self.digit_complete = True

        c1_a, c1_b = self.clock1_cmd.goto_pos()
        c2_a, c2_b = self.clock2_cmd.goto_pos()
        c3_a, c3_b = self.clock3_cmd.goto_pos()

        self.clock1_gui.draw_hands(c1_a, c1_b)
        self.clock2_gui.draw_hands(c2_a, c2_b)
        self.clock3_gui.draw_hands(c3_a, c3_b)




def timer(t1):
    """ stopwatch """
    return time.time() - t1


def main():
    """ main function """
    # pylint: disable = too-many-locals, too-many-statements
    root = tk.Tk()
    app = ColonGUI(root)
    app.pack()

    move_time = 1500
    app.set_goal([(-135, -135), (-135, -135), (-135, -135)], move_time)
    time_1 = time.time()
    while True:
        app.draw()
        app.update_idletasks()
        app.update()
        time.sleep(0.1)

      

if __name__ == "__main__":
    main()
