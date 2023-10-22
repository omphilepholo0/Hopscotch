let currentSquare = 0
input.onButtonPressed(Button.A, function () {
    let playerTurn = 0
    let GameInProgress = 0
    if (GameInProgress && playerTurn) {
        currentSquare = 1
    } else {
        if (currentSquare >= 5) {
            currentSquare = 0
            basic.showString("P1 Win")
        }
    }
})
function hop () {
	
}
