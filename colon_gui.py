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
        self.clock2_gui.grid(row=0, column=1)

        self.clock3_gui = cgui.ClockCanvas(self, self.clock_size)
        self.clock3_gui.grid(row=1, column=0)

        self.clock4_gui = cgui.ClockCanvas(self, self.clock_size)
        self.clock4_gui.grid(row=1, column=1)

        self.clock5_gui = cgui.ClockCanvas(self, self.clock_size)
        self.clock5_gui.grid(row=2, column=0)

        self.clock6_gui = cgui.ClockCanvas(self, self.clock_size)
        self.clock6_gui.grid(row=2, column=1)

        self.clock_gui_array = [self.clock1_gui, self.clock2_gui, self.clock3_gui, self.clock4_gui,
                                self.clock5_gui, self.clock6_gui]


    def quit_app(self):
        """ closes screen """
        self.master.destroy()

    def initialize_clocks(self):
        """ initializes all clocks """

        self.clock1_cmd = sc.SingleClock(-90, 90)
        self.clock2_cmd = sc.SingleClock(-90, 90)
        self.clock3_cmd = sc.SingleClock(-90, 90)
        self.clock4_cmd = sc.SingleClock(-90, 90)
        self.clock5_cmd = sc.SingleClock(-90, 90)
        self.clock6_cmd = sc.SingleClock(-90, 90)

        self.clock_cmd_array = [self.clock1_cmd, self.clock2_cmd, self.clock3_cmd, self.clock4_cmd,
                                self.clock5_cmd, self.clock6_cmd]

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
                self.clock3_cmd.motion_complete and self.clock4_cmd.motion_complete and \
                self.clock5_cmd.motion_complete and self.clock6_cmd.motion_complete:
                    self.digit_complete = True

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
    app.set_goal(cconfig.HOME_POS, move_time)
    time_1 = time.time()
    quit_flag = False
    while quit_flag is False:
        app.draw()
        app.update_idletasks()
        app.update()

        if timer(time_1) > 2 and timer(time_1) < 2.01:
            app.set_goal(cconfig.NUMBER_1, move_time)

        if timer(time_1) > 5 and timer(time_1) < 5.01:
            app.set_goal(cconfig.NUMBER_2, move_time)

        if timer(time_1) > 8 and timer(time_1) < 8.01:
            app.set_goal(cconfig.NUMBER_3, move_time)

        if timer(time_1) > 11 and timer(time_1) < 11.01:
            app.set_goal(cconfig.NUMBER_4, move_time)

        if timer(time_1) > 14 and timer(time_1) < 14.01:
            app.set_goal(cconfig.NUMBER_5, move_time)

        if timer(time_1) > 17 and timer(time_1) < 17.01:
            app.set_goal(cconfig.NUMBER_6, move_time)

        if timer(time_1) > 20 and timer(time_1) < 20.01:
            app.set_goal(cconfig.NUMBER_7, move_time)

        if timer(time_1) > 23 and timer(time_1) < 23.01:
            app.set_goal(cconfig.NUMBER_8, move_time)

        if timer(time_1) > 26 and timer(time_1) < 26.01:
            app.set_goal(cconfig.NUMBER_9, move_time)

        if timer(time_1) > 29 and timer(time_1) < 29.01:
            app.set_goal(cconfig.NUMBER_0, move_time)

        if timer(time_1) > 31 and timer(time_1) < 31.5:

            quit_flag = True

    time.sleep(2)
    app.quit_app()


if __name__ == "__main__":
    main()
