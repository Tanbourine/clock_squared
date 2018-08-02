""" Class for a single clock hand
"""
import time
import clock_config as cconfig


class ClockHand():

    """ Class for a single clock hand """
    # pylint: disable = too-many-instance-attributes

    def __init__(self, init_pos):
        self.angle = init_pos
        self.destination = init_pos
        self.delta_angle = 0
        self.step_size = 0
        self.prev_time = 0
        self.scan_rate = cconfig.CMD_RATE
        self.iterations = 0
        self.angle_tolerance = cconfig.ANGLE_TOLERANCE  # degrees
        self.angle_error = 1000
        self.motion_complete = False

    def set_goal(self, destination, motion_time):
        """ sets the parameters for the upcoming move
        """

        # "Scan Rate must divide evenly into motion_time"
        assert (motion_time % self.scan_rate) == 0

        # reset goal flag
        self.motion_complete = False

        # change in angle between starting and ending position
        self.destination = destination
        self.delta_angle = self.destination - self.angle

        # determine step size
        self.step_size = round(self.delta_angle / motion_time * self.scan_rate, 3)

    def goto_pos(self):
        """ moves to preset parameters from set_goal()
        """
        # pylint: disable = line-too-long

        self.angle_error = self.destination - self.angle

        if (time.time() - self.prev_time) * 1000 >= self.scan_rate and self.motion_complete is False:
            self.prev_time = time.time()

            if abs(self.angle_error) <= self.angle_tolerance:
                self.angle = self.destination
                self.motion_complete = True
                # print("goal reached")

            elif self.angle < self.destination:           # moving clockwise
                if (self.angle + self.step_size) <= (self.destination + self.angle_tolerance):
                    self.angle += round(self.step_size, 3)
                    self.iterations += 1

            elif self.angle > self.destination:         # moving counter-clockwise
                if (self.angle + self.step_size) >= (self.destination - self.angle_tolerance):
                    self.angle += round(self.step_size, 3)
                    self.iterations += 1


def main():
    """ main function that runs when this script is run directly """
    hand1 = ClockHand(0)
    hand2 = ClockHand(90)

    destination_1 = 90
    destination_2 = 0
    move_time = 10000

    hand1.set_goal(destination_1, move_time)
    hand2.set_goal(destination_2, move_time)

    while hand1.motion_complete is False or hand2.motion_complete is False:
        if hand1.motion_complete is False:
            hand1.goto_pos()
            print("Hand 1 >>> ", hand1.angle)

        if hand2.motion_complete is False:
            hand2.goto_pos()
            print("Hand 2 >>> ", hand2.angle)
        # time.sleep(.5)
        time.sleep(.05)

    print("success!")
    # print(hand1.angle)
    # print(hand2.angle)


if __name__ == "__main__":
    main()
