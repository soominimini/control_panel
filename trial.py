
import anki_vector


with anki_vector.Robot() as robot:
    robot.behavior.say_text("hi! i am vector")
    robot.anim.play_animation('anim_onboarding_reacttoface_happy_01_head_angle_20')
    robot.behavior.say_text("nice to meet you!")
