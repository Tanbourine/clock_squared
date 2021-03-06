""" stores all formations for clocks """

import main as main_app

HOME_POS = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
NUMBER_1 = [(-135, -135), (-180, -180), (-135, -135), (0, -180), (-135, -135), (0, 0)]
NUMBER_1_LEFT = [(-135, -135), (-180, -180), (-135, -135), (0, -180), (-135, -135), (0, 0)]
NUMBER_1_RIGHT = [(-180, -180), (-135, -135), (0, -180), (-135, -135), (0, 0), (-135, -135)]
NUMBER_2 = [(90, 90), (-90, 180), (180, 90), (-90, 0), (0, 90), (-90, -90)]
NUMBER_3 = [(90, 90), (-90, 180), (90, 90), (0, 180), (90, 90), (-90, 0)]
NUMBER_4 = [(180, 180), (180, 180), (0, 90), (0, 180), (-135, -135), (0, 1)]
NUMBER_5 = [(90, 180), (-90, -90), (0, 90), (-90, 180), (90, 90), (-90, 0)]
NUMBER_6 = [(90, 180), (-90, -90), (0, 180), (-90, 180), (0, 90), (-90, 0)]
NUMBER_7 = [(90, 90), (-90, 180), (-135, -135), (0, 180), (-135, -135), (0, 0)]
NUMBER_8 = [(90, 180), (180, -90), (0, 90), (0, -90), (0, 90), (-90, 0)]
NUMBER_9 = [(90, 180), (-90, 180), (0, 90), (0, 180), (90, 90), (-90, 0)]
NUMBER_0 = [(90, 180), (-90, 180), (0, 180), (0, 180), (0, 90), (-90, 0)]

COLON_CONFIG = [(-135, -135), (-135, -135), (-135, -135)]

CLOCK_SIZE = 75
FACE_COLOR = "#262626"
HAND_COLOR = "#626262"
DOT_COLOR = "#660000"
BG_COLOR = "#262626"
OFF_COLOR = "black"
OFF_ANGLE = -135

CLOCK_RADIUS_RATIO = 0.485
HAND_RADIUS_RATIO = 0.9
HAND_WIDTH = int(CLOCK_SIZE / 12)
DOT_RADIUS = 6
MOVE_TIME = 7500                # millis
GUI_UPDATE_TIME = 50            # millis
CMD_RATE = 100
ANGLE_TOLERANCE = 0.1


def main():
    """ main app to run main app"""
    main_app.main()


if __name__ == '__main__':
    main()
