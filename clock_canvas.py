

""" GUI for a single face """

try:
    # python 3.x
    import tkinter as tk
    # from tkinter import ttk

except ImportError:
    # python 2.x
    import Tkinter as tk
    print("Running on Python 2, might have issues")

import math
import time
import clock_config as cconfig


class ClockCanvas(tk.Frame):
    # pylint: disable = too-many-instance-attributes, too-many-ancestors

    """ canvas for an individual clock """

    def __init__(self, master, canvas_width, hand1_angle=0, hand2_angle=0):
        tk.Frame.__init__(self, master)

        self.master = master
        self.canvas_width = canvas_width
        self.canvas_height = canvas_width
        self.clock_radius = cconfig.CLOCK_RADIUS_RATIO * self.canvas_width
        self.hand_radius = cconfig.HAND_RADIUS_RATIO * self.clock_radius
        self.hand_width = cconfig.HAND_WIDTH
        self.dot_radius = cconfig.DOT_RADIUS

        self.face_color = cconfig.FACE_COLOR
        self.hand_color = cconfig.HAND_COLOR
        self.dot_color = cconfig.DOT_COLOR
        self.bg_color = cconfig.BG_COLOR
        self.off_color = cconfig.OFF_COLOR

        self.middle_x = self.canvas_width / 2
        self.middle_y = self.canvas_height / 2

        self.initialize_canvas()
        hand1_angle = 0
        hand2_angle = 90
        self.initialize_clockface(hand1_angle, hand2_angle)

    def initialize_canvas(self):
        """ initialize canvas for clock to be drawn """

        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height,
                                borderwidth=0, bg=self.bg_color)
        self.canvas.grid(row=0, column=0)

    def initialize_clockface(self, hand1_angle, hand2_angle):
        """ draws clock with initial hand positions """
        # create clockface
        self._create_circle(self.middle_x, self.middle_y, self.clock_radius, fill=self.face_color)

        # create dot
        self._create_circle(self.middle_x, self.middle_y, self.dot_radius, fill=self.dot_color)

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

        # self.canvas.delete(self.hand1)
        # self.canvas.delete(self.hand2)

        h1_x_pos, h1_y_pos = self.angle_to_coord(hand1_angle)
        h2_x_pos, h2_y_pos = self.angle_to_coord(hand2_angle)

        # create hand 1
        #self.canvas.delete(self.hand1)
        
        self.canvas.delete(self.hand1)
        if hand1_angle >= cconfig.OFF_ANGLE - cconfig.ANGLE_TOLERANCE and hand1_angle <= \
                cconfig.OFF_ANGLE + cconfig.ANGLE_TOLERANCE:
            self.hand1 = self.canvas.create_line(self.middle_x, self.middle_y,
                                                 self.middle_x + h1_x_pos, self.middle_y - h1_y_pos,
                                                 width=self.hand_width, fill=self.off_color)

        else:

            self.hand1 = self.canvas.create_line(self.middle_x, self.middle_y,
                                                 self.middle_x + h1_x_pos, self.middle_y - h1_y_pos,
                                                 width=self.hand_width, fill=self.hand_color)

        # create hand 2
        self.canvas.delete(self.hand2)
        
        if hand2_angle >= cconfig.OFF_ANGLE - cconfig.ANGLE_TOLERANCE and hand2_angle <= \
                cconfig.OFF_ANGLE + cconfig.ANGLE_TOLERANCE:
            self.hand2 = self.canvas.create_line(self.middle_x, self.middle_y,
                                                 self.middle_x + h2_x_pos, self.middle_y - h2_y_pos,
                                                 width=self.hand_width, fill=self.off_color)
        else:
            self.hand2 = self.canvas.create_line(self.middle_x, self.middle_y,
                                                 self.middle_x + h2_x_pos, self.middle_y - h2_y_pos,
                                                 width=self.hand_width, fill=self.hand_color)

    def reset_face(self, hand1_angle, hand2_angle):
        """ re-initialize face after changing settings """
        self.initialize_canvas()
        self.initialize_clockface(hand1_angle, hand2_angle)

    def angle_to_coord(self, angle):
        """ determines x, y position for a given angle """
        # cos(angle) = y/hyp
        # sin(angle) = x/hyp
        x_pos = self.hand_radius * math.sin(math.radians(angle))
        y_pos = self.hand_radius * math.cos(math.radians(angle))


        return x_pos, y_pos

    def _create_circle(self, x, y, r, **kwargs):
        # pylint: disable = invalid-name
        """ draw a circle easily """
        self.canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)

def main():
    root = tk.Tk()
    app = ClockCanvas(root, cconfig.CLOCK_SIZE)
    app.pack()

    for j in range(3):
        for i in range(90,150):
            app.draw_hands(i, -i)
            time.sleep(.05)
            app.update()

if __name__ == '__main__':
    main()
