""" This class provides the back end calculations for a single clock
"""
import time
import clock_hand as ch


class SingleClock():

    """ Defines the hands for a single clock """

    def __init__(self, hand_1_angle, hand_2_angle):
        self.hand_1 = ch.ClockHand(hand_1_angle)
        self.hand_2 = ch.ClockHand(hand_2_angle)

    def evaluate_move(self, dest_1, dest_2, motion_time):
        """ evaluates motion parameters """

        # set motion parameters
        self.hand_1.evaluate_move(dest_1, motion_time)
        self.hand_2.evaluate_move(dest_2, motion_time)

    def goto_pos(self):
        """ goes to set angle positions for each hand """

        # start move
        self.hand_1.goto_angle()
        self.hand_2.goto_angle()

        print("Hand 1 >>> ", self.hand_1.angle)
        print("Hand 2 >>> ", self.hand_2.angle)
        print("\n")


def main():
    """ main function that runs when this script is individually run """
    clock = SingleClock(0, 90)

    scan_rate = 100
    motion_time = 1000
    dest1 = 90
    dest2 = -90

    clock.hand_1.scan_rate = scan_rate
    clock.hand_2.scan_rate = scan_rate

    clock.evaluate_move(dest1, dest2, motion_time)

    timer1 = time.time()

    while clock.hand_1.reached_goal is False or clock.hand_2.reached_goal is False:
        clock.goto_pos()
        time.sleep(scan_rate / 1000)

    print("Elapsed time >>> ", time.time() - timer1)


if __name__ == '__main__':
    main()
