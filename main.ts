basic.forever(function () {
    if (input.buttonIsPressed(Button.B) || input.isGesture(Gesture.ScreenUp)) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
