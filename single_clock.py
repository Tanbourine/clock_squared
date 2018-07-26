""" This class provides the back end calculations for a single clock
"""
import time
import clock_hand as ch



class SingleClock():

    """ Defines the hands for a single clock """

    def __init__(self, hand_1_angle, hand_2_angle):
        self.hand_1 = ch.ClockHand(hand_1_angle)
        self.hand_2 = ch.ClockHand(hand_2_angle)

        self.dest_1 = 0
        self.dest_2 = 0

        self.motion_complete = False


    def set_goal(self, dest_1, dest_2, motion_time):
        """ evaluates motion parameters """

        # save destination
        self.dest_1 = dest_1
        self.dest_2 = dest_2

        # motion complete flag to False
        self.motion_complete = False

        # set motion parameters
        self.hand_1.set_goal(dest_1, motion_time)
        self.hand_2.set_goal(dest_2, motion_time)


    def goto_pos(self):
        """ goes to set angle positions for each hand """

        if self.hand_1.angle == self.dest_1 and self.hand_2.angle == self.dest_2:
            self.motion_complete = True

        # start move
        self.hand_1.goto_pos()
        self.hand_2.goto_pos()

        # print("Hand 1 >>> ", self.hand_1.angle)
        # print("Hand 2 >>> ", self.hand_2.angle)
        # print("\n")

        return self.hand_1.angle, self.hand_2.angle


def main():
    """ main function that runs when this script is individually run """
    clock = SingleClock(0, 90)

    scan_rate = 100
    motion_time = 1000
    dest1 = 90
    dest2 = -90

    clock.hand_1.scan_rate = scan_rate
    clock.hand_2.scan_rate = scan_rate

    clock.set_goal(dest1, dest2, motion_time)

    timer1 = time.time()

    while clock.hand_1.motion_complete is False or clock.hand_2.motion_complete is False:
        clock.goto_pos()
        time.sleep(scan_rate / 1000)

    print("Elapsed time >>> ", time.time() - timer1)


if __name__ == '__main__':
    main()
