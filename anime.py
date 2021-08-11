
"""Play animations on Vector
Play an animation using a trigger, and then another animation by name.
"""

import anki_vector


with anki_vector.Robot() as robot:
    print("List all animation names:")
    anim_names = robot.anim.anim_list
    for anim_name in anim_names:
        print(anim_name)