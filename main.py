def on_button_pressed_a2():
   basic.show_leds("""
. . # . .
. # . # .
# # # # #
# . . . #
# . . . #
""")
input.on_button_pressed(Button.A, on_button_pressed_a2)
