var drums = document.querySelectorAll('.drum')

for (let i = 0; i < drums.length; i++) {
    drums[i].addEventListener('click', function () {
        var value = drums[i].innerHTML
        clicked(value)
        makeSound(value)
    })

}
document.addEventListener('keydown', function (event) {
    clicked(event.key)
    makeSound(event.key)
})

function clicked(value) {
    switch (value) {
        case 'w':
            var tom1 = new Audio('sounds/tom-1.mp3')
            tom1.play()
            break;
        case 'a':
            var tom2 = new Audio('sounds/tom-2.mp3')
            tom2.play()
            break;
        case 's':
            var tom3 = new Audio('sounds/tom-3.mp3')
            tom3.play()
            break;
        case 'd':
            var tom4 = new Audio('sounds/tom-4.mp3')
            tom4.play()
            break;
        case 'j':
            var snare = new Audio('sounds/snare.mp3')
            snare.play()
            break;
        case 'k':
            var kickbass = new Audio('sounds/kick-bass.mp3')
            kickbass.play()
            break;
        case 'l':
            var crash = new Audio('sounds/crash.mp3')
            crash.play()
            break;
        default: console.log('Something went wrong')
    }
}

function makeSound(letter) {
    for (let i = 0; i < drums.length; i++) {
        if (drums[i].innerHTML === letter) {
            drums[i].classList.add('pressed')
            setTimeout(function() {
                drums[i].classList.remove('pressed')
            }, 100)
        }
    }
}