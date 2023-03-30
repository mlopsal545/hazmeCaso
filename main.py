def on_forever():
    if input.button_is_pressed(Button.B) or input.is_gesture(Gesture.FREE_FALL):
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
basic.forever(on_forever)
