""" Class for a single clock hand
"""
import time


class ClockHand():

    """ Class for a single clock hand """
    # pylint: disable = too-many-instance-attributes

    def __init__(self, init_pos):
        self.angle = init_pos
        self.destination = init_pos
        self.delta_angle = 0
        self.step_size = 0
        self.pause_time = 0
        self.scan_rate = 100
        self.iterations = 0
        self.angle_tolerance = .1  # degrees
        self.motion_complete = False

    def set_goal(self, destination, motion_time):
        """ sets the parameters for the upcoming move
        """

        assert (motion_time % self.scan_rate) < 1, "Scan Rate must divide evenly into motion_time"

        # reset goal flag
        self.motion_complete = False

        # change in angle between starting and ending position
        self.destination = destination
        self.delta_angle = self.destination - self.angle

        # determine step size
        self.step_size = self.delta_angle / motion_time * self.scan_rate

    def goto_pos(self):
        """ moves to preset parameters from set_goal()
        """

        self.delta_angle = self.destination - self.angle

        if (time.time() - self.pause_time) * 1000 >= self.scan_rate and self.motion_complete is False:
            self.pause_time = time.time()

            if abs(self.delta_angle) < self.angle_tolerance:
                self.angle = self.destination
                self.motion_complete = True

            elif self.angle < self.destination:           # moving clockwise
                if (self.angle + self.step_size) <= self.destination:
                    self.angle += self.step_size
                    self.iterations += 1

            elif self.angle > self.destination:         # moving counter-clockwise
                if (self.angle + self.step_size) >= self.destination:
                    self.angle += self.step_size
                    self.iterations += 1


def main():
    """ main function that runs when this script is run directly """
    hand1 = ClockHand(0)
    hand2 = ClockHand(90)

    destination_1 = 90
    destination_2 = 0
    move_time = 1000

    hand1.set_goal(destination_1, move_time)
    hand2.set_goal(destination_2, move_time)

    while hand1.motion_complete is False or hand2.motion_complete is False:
        if hand1.motion_complete is False:
            hand1.goto_pos()
            print("Hand 1 >>> ", hand1.angle)

        if hand2.motion_complete is False:
            hand2.goto_pos()
            print("Hand 2 >>> ", hand2.angle)
        time.sleep(.05)

    print("success!")
    # print(hand1.angle)
    # print(hand2.angle)

if __name__ == "__main__":
    main()
