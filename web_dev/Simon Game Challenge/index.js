var colours = ['red','green','yellow','blue']
var gameOrder = []
var playerOrder = []
var gameOn = false
var level = 0

// this randomises a square
function chooseSquare() {
    var number = Math.floor(Math.random()*4)
    var colour = colours[number]
    gameOrder.push(colour)
    clickAction(colour)
}

function changeLevel() {
    level++
    $('#level-title').text('Level '+level)
}
// this makes the animation and noise
function clickAction(colour) {
    $('#'+colour).addClass('pressed');
    var audio = new Audio("sounds/" + colour + ".mp3");
    audio.play();
    setTimeout(function() {
        $('#'+colour).removeClass('pressed')
    }, 200)
}
// this function checks whether the last value inputted is correct, and whether the level is complete.
// if the level is complete, it resets the player order and chooses the next square for the next level
// if the guess is incorrect, it will play the wrong animation and restart the game

function checkCorrect() {
    if (playerOrder[playerOrder.length-1] === gameOrder[playerOrder.length-1]) {
        if (playerOrder.length === gameOrder.length) {
            changeLevel()
            setTimeout(chooseSquare, 1000)

            playerOrder = []
        }
    } else {
        gameOn = false

        $('#level-title').text('Game Over, Press Any Key to Restart')

        $('body').addClass('game-over');
        var audio = new Audio('sounds/wrong.mp3')
        audio.play()
        setTimeout(function() {
        $('body').removeClass('game-over')
        }, 200)

        gameOrder = []
        playerOrder = []
        level = 0
    }
}
// this will start the game
$(document).on('keydown', function() {
    if (gameOn === false) {
        chooseSquare()
        gameOn = true
        changeLevel()
    }
})
// this will select and do necessary actions on the chosen colour
$('.btn').on('click', function() {
    var chosenColour = $(this).attr('id')
    playerOrder.push(chosenColour)
    clickAction(chosenColour)
    checkCorrect()
})

