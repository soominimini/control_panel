
"""Tell Vector to drive on and off the charger.
"""

import anki_vector


if __name__ == '__main__':
    with anki_vector.Robot() as robot:
        print("Drive Vector onto charger...")
        robot.behavior.drive_on_charger()