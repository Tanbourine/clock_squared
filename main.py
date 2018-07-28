""" Main application for clock GUI"""
try:
    # python 3.x
    import tkinter as tk
    # from tkinter import ttk

except ImportError:
    # python 2.x
    import Tkinter as tk
    print("Running on Python 2, might have issues")

import time
from datetime import datetime
import digit_gui as dg
import clock_config as cc
import colon_gui as cg


# pylint: disable = too-many-ancestors, too-many-instance-attributes, invalid-name

class MainApplication(tk.Frame):

    """ master app """

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        """ configure gui settings """
        self.master.title("Clocks on Clocks")
        self.master.resizable(width=True, height=True)

    def create_widgets(self):
        """ initalizes widgets """

        self.digit_1 = dg.DigitGUI(self.master)
        self.digit_1.grid(row=0, column=0)

        self.digit_2 = dg.DigitGUI(self.master)
        self.digit_2.grid(row=0, column=1)

        self.digit_3 = dg.DigitGUI(self.master)
        self.digit_3.grid(row=0, column=3)

        self.digit_4 = dg.DigitGUI(self.master)
        self.digit_4.grid(row=0, column=4)

        self.colons = cg.ColonGUI(self.master)
        self.colons.grid(row=0, column=2)

        digit_array = [self.digit_1, self.digit_2, self.digit_3, self.digit_4]
##
##        for digit in digit_array:
##            for i in range(6):
##                digit.clock_gui_array[i].dot_color = "#660000"
##                digit.clock_gui_array[i].bg_color = "black"
##                digit.clock_gui_array[i].hand_color = "white"
##                digit.clock_gui_array[i].reset_face(-90, 90)

        # create quit app button
        tk.Button(
            self.master, text='Quit', command=self.quit_app).grid(
                row=100, column=0, columnspan=4)

    def quit_app(self):
        """ closes screen """
        self.master.destroy()


def t_bound(t1, t2, bound=0.1):
    """ stopwatch """
    delta_time = time.time() - t1
    return bool(delta_time > t2 and delta_time < (t2 + bound))


def time_to_config(num_array):
    """ takes time array and spits out config """
    # pylint: disable = unused-variable
    output_config = [0, 0, 0, 0]
    assert len(num_array) == 4
    for pos, digit in enumerate(num_array):
        for number in range(10):
            if digit == '1':
                output_config[pos] = cc.NUMBER_1
            elif digit == '2':
                output_config[pos] = cc.NUMBER_2
            elif digit == '3':
                output_config[pos] = cc.NUMBER_3
            elif digit == '4':
                output_config[pos] = cc.NUMBER_4
            elif digit == '5':
                output_config[pos] = cc.NUMBER_5
            elif digit == '6':
                output_config[pos] = cc.NUMBER_6
            elif digit == '7':
                output_config[pos] = cc.NUMBER_7
            elif digit == '8':
                output_config[pos] = cc.NUMBER_8
            elif digit == '9':
                output_config[pos] = cc.NUMBER_9
            elif digit == '0':
                output_config[pos] = cc.NUMBER_0

    return output_config


def get_time():
    """ formats time array """
    current_time = []
    unformatted_time = datetime.now().time()
    current_time.append(str(unformatted_time)[0:1])
    current_time.append(str(unformatted_time)[1:2])
    current_time.append(str(unformatted_time)[3:4])
    current_time.append(str(unformatted_time)[4:5])

    return current_time, "The time is >>> " + str(unformatted_time)[0:8]


def main():
    """ main function """
    # pylint: disable = too-many-locals, too-many-statements
    root = tk.Tk()
    app = MainApplication(root)

    auto_mode = True
    move_time = 2000
    prev_time = time.time()
    update_gui_time = time.time()
    refresh_rate = 100

    app.digit_1.set_goal(cc.HOME_POS, move_time)
    app.digit_2.set_goal(cc.HOME_POS, move_time)
    app.digit_3.set_goal(cc.HOME_POS, move_time)
    app.digit_4.set_goal(cc.HOME_POS, move_time)
    app.colons.set_goal(cc.COLON_CONFIG, move_time)
    while True:

        # show current time on clocks
        if auto_mode is True:
            current_time, unformatted_time = get_time()
            output_config = time_to_config(current_time)

        else:
            if app.digit_1.digit_complete and app.digit_2.digit_complete and \
                    app.digit_3.digit_complete and app.digit_4.digit_complete:
            # if app.digit_1.digit_complete and time.time() - prev_time > move_time / 1000 + 0.25:
                user_input = input("Enter 4 numbers to display >>> ")
                disp_config = []
                for num in user_input:
                    disp_config.append(num)

                output_config = time_to_config(disp_config)
                print(output_config)

        if app.digit_1.digit_complete and (time.time() - prev_time) > move_time / 1000 + 0.25:
            app.digit_1.set_goal(output_config[0], move_time)
            app.digit_2.set_goal(output_config[1], move_time)
            app.digit_3.set_goal(output_config[2], move_time)
            app.digit_4.set_goal(output_config[3], move_time)
            prev_time = time.time()
            print(unformatted_time)

        if (time.time() - update_gui_time) > refresh_rate / 1000:
            app.digit_1.draw()
            app.digit_2.draw()
            app.digit_3.draw()
            app.digit_4.draw()
            app.colons.draw()
            app.update_idletasks()
            app.update()


if __name__ == "__main__":
    main()
