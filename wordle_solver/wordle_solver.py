import difflib

word_lst = []
with open('wordle-answers-alphabetical.txt') as f:
    for line in f:
        word_lst.append(line.strip())

incorrect_letters = []
wrong_pos_letters = {}
correct_letters = {}
multiples = {}


def best_word(list_of_words):
    freq = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    
    for word in list_of_words:
        for letter in word:
            freq[letter] += 1
            
    freq = sorted(freq.items(), key=lambda x:x[1])
    freq.reverse()
    
    best_letters = []
    for i in freq[:5]:
        best_letters.append(i[0])
        
    print('Best Letters:', best_letters)
    best = ''.join(best_letters)
    if len(list_of_words) == 1:
        return list_of_words[0]
        
    best_match = difflib.get_close_matches(best, list_of_words, 1, cutoff=0)[0]

    return best_match


print(best_word(word_lst))
print(correct_letters)

info = input('Information: ').lower()

while info != 'solved':
    info = info.split()
    new = sorted([i[1] for i in info if (i[0] == 'g' or i[0] == 'y')])
    
    for i in (list(set(new))):
        amt = new.count(i)
        if amt > 1:
            multiples[i] = amt
            
    index = 0
    for i in info:
        if i[0] == 'g':
            if i[1] in incorrect_letters:
                incorrect_letters.remove(i[1])
            correct_letters[i[1]] = index
        elif i[0] == 'y':
            if i[1] in wrong_pos_letters:
                wrong_pos_letters[i[1]].append(index)
            else:
                wrong_pos_letters[i[1]] = [index]
        elif i[0] == 'b':
            if (i[1] not in wrong_pos_letters) and (i[1] not in correct_letters):
                incorrect_letters.append(i[1])

        index += 1
        
    available_words = []
    for word in word_lst:
        word_available = True
        for letter in word:
            if letter in incorrect_letters:
                word_available = False
        for letter in wrong_pos_letters:
            for i in wrong_pos_letters[letter]:
                if word[i] == letter:
                    word_available = False
            if letter not in word:
                word_available = False
        for letter in correct_letters:
            if word[correct_letters[letter]] != letter:
                word_available = False
        for letter in multiples:
            if word.count(letter) < multiples[letter]:
                word_available = False

        if word_available == True:
            available_words.append(word)

    final_word = best_word(available_words)
    print(final_word)
    print(available_words)
    info = input('Information: ')

