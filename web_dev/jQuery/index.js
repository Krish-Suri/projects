$('textarea').on('input', calculate)

$('button').on('click', function() {
    $('textarea').val('')
    calculate()
})

function calculate() {
    var writing = $('textarea').val()

    let sentences = 0
    for (let i = 0; i<writing.length; i++) {
        if ((writing[i] === '.' && writing[i+1] !== '.') || writing[i] === '?' || writing[i] === '!') {
            sentences++
        }
    }
    if (writing === '') {
        $('.word').text('0')
        $('.sentences').text('0')
        $('.character_amount').text('0')
    } else {
        words = writing.split(' ').length
        $('.word').text(words)
        $('.sentences').text(sentences)
        $('.character_amount').text(writing.length)
    }
}