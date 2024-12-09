from random import shuffle
import pygame as pg
import pygame.display

pg.init()


GREEN = (11, 102, 33)
BLUE = (130,130,130)
DARKBLUE = (100,100,100)
WHITE = (255,255,255)
RED = (180,0,0)


window = pg.display.set_mode((1300,800))
window.fill(GREEN)
clock = pg.time.Clock()
class Button():
    def __init__(self,x,y,width,height,colour = (0,0,0), text = '', font = 'comicsans', fontsize = 60):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.font = font
        self.fontsize = fontsize

    def draw(self):
        pg.draw.rect(window, self.colour, pg.Rect(self.x, self.y, self.width, self.height))

        if self.text != '':
            font = pygame.font.SysFont(self.font, self.fontsize)
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self,position):
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True
        return False


two_player = Button(100,350,400,100, BLUE, 'Two Player', 'calibri')
one_player = Button(800,350,400,100, BLUE, 'Casino', 'calibri')
pg.display.update()

font = pg.font.SysFont('calibri', 50)
font2 = pg.font.SysFont('calibri', 33)
minimainfont = pg.font.SysFont('calibri',130)
mainfont = pg.font.SysFont('calibri', 200)

hitbutton = Button(1100,320,150,40, BLUE, 'HIT','calibri', 35)
passbutton = Button(1100,400,150,40, BLUE, 'STAND','calibri', 35)
sidebar = pg.Rect(1050,0,250,800)


def AI_hit(p2hand):
    if p2hand.hand_total() >= 17:
        return False
    else:
        return True


def draw(p1hand,p2hand, hand,p1score,p2score):
    window.fill(GREEN)
    pg.draw.rect(window, (0, 0, 0), sidebar)
    hitbutton.draw()
    passbutton.draw()
    num = 0
    for card in p1hand.cards:
        file = ((card.label + '_of_' + card.suit + '.png').lower())
        cardimg = pg.image.load('PNG-cards-1.3/' + file)
        cardimg = pg.transform.scale(cardimg, (150, 200))
        window.blit(cardimg, (100 + num, 550))
        num += 200

    num = 0
    for card in p2hand.cards:
        file = ((card.label + '_of_' + card.suit + '.png').lower())
        cardimg = pg.image.load('PNG-cards-1.3/' + file)
        cardimg = pg.transform.scale(cardimg, (150, 200))
        window.blit(cardimg, (100 + num, 20))
        num += 200
    p1total = font.render('Player 1: ' + str(p1hand.hand_total()), 1, (0, 0, 0))
    p2total = font.render('Player 2: ' + str(p2hand.hand_total()), 1, (0, 0, 0))
    window.blit(p1total, (50, 460))
    window.blit(p2total, (50, 240))
    p1wins = minimainfont.render(str(p1score), 1, WHITE)
    p2wins = minimainfont.render(str(p2score), 1, WHITE)
    p1 = font.render('P1 Wins:', 1, WHITE)
    p2 = font.render('P2 Wins:', 1, WHITE)
    window.blit(p1wins,(1150, 640))
    window.blit(p2wins, (1150, 140))
    window.blit(p1, (1080, 550))
    window.blit(p2, (1080, 50))
    if hand == p1hand:
        pg.draw.line(window,RED,(50,515),(320,515),width=4)
    else:
        pg.draw.line(window,RED,(50,300),(320,300),width=4)
def isOver(button,position):
    if position[0] > button.x and position[0] < button.x + button.width:
        if position[1] > button.y and position[1] < button.y + button.height:
            return True
    return False



class Card:
    def __init__(self, suit, value, label):
        self.suit = suit
        self.value = value
        self.label = label
    def __str__(self):
        return f'{self.label} of {self.suit}'

class Hand:
    def __init__(self):
        self.cards = []
    def __str__(self):
        return ', '.join([str(card) for card in self.cards])
    def add_card(self,card):
        self.cards.append(card)
    def hand_total(self):
        total = 0
        for card in self.cards:
            total += card.value
        pos = 0
        while total > 21 and pos < len(self.cards):
            if self.cards[pos].value == 11:
                self.cards[pos].value = 1
                total -= 10
            pos += 1
        return total
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        labels = ['Ace', '2', '3', '4', '5' ,'6' ,'7' , '8', '9', '10', 'Jack', 'Queen', 'King']
        cards = []
        for suit in suits:
            for label in labels:
                if label.isnumeric():
                    num = int(label)
                elif label == 'Ace':
                    num = 11
                else:
                    num = 10
                cards.append(Card(suit, num, label))
        self.cards = cards
    def __str__(self):
        return f'{len(self.cards)}'
    def shuffle(self):
        shuffle(self.cards)
        return self
    def deal(self):
        if len(self.cards) == 0:
            raise ValueError('No cards left in the deck')
        else:
            return self.cards.pop()

def program():
    run = True
    while run:
        clock.tick(60)
        pg.display.set_caption('Blackjack')

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                position = event.pos
                if two_player.isOver(position):
                    game(0,0)
                if one_player.isOver(position):
                    casino(0,0)

            if event.type == pg.MOUSEMOTION:
                position = event.pos
                if two_player.isOver(position):
                    two_player.colour = DARKBLUE
                else:
                    two_player.colour = BLUE
                if one_player.isOver(position):
                    one_player.colour = DARKBLUE
                else:
                    one_player.colour = BLUE

        one_player.draw()
        two_player.draw()

        pg.display.update()
def game(p1score,p2score):
    global font, font2, mainfont, minimainfont


    deck = Deck()
    deck.shuffle()

    p1hand = Hand()
    card = deck.deal()
    p1hand.add_card(card)
    card = deck.deal()
    p1hand.add_card(card)

    p2hand = Hand()
    card = deck.deal()
    p2hand.add_card(card)
    card = deck.deal()
    p2hand.add_card(card)

    hand = p1hand

    p1done = False
    p2done = False


    run = True
    while run:
        clock.tick(60)
        pg.display.set_caption('Blackjack')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                position = event.pos
                if hitbutton.isOver(position):
                    card = deck.deal()
                    hand.add_card(card)
                    if hand == p1hand and p2done == False:
                        hand = p2hand
                    elif hand == p2hand and p1done == False:
                        hand = p1hand
                if passbutton.isOver(position):
                    if hand == p1hand:
                        if p2done == False:
                            hand = p2hand
                        p1done = True
                    elif hand == p2hand:
                        if p1done == False:
                            hand = p1hand
                        p2done = True
                    pg.display.update()
            if event.type == pg.MOUSEMOTION:
                position = event.pos
                if hitbutton.isOver(position):
                    hitbutton.colour = DARKBLUE
                else:
                    hitbutton.colour = BLUE
                if passbutton.isOver(position):
                    passbutton.colour = DARKBLUE
                else:
                    passbutton.colour = BLUE



        if p1done == True and p2done == True:
            if p1hand.hand_total() > p2hand.hand_total():
                msg = 'Player 1 Wins'
                p1score += 1
            elif p2hand.hand_total() > p1hand.hand_total():
                msg = 'Player 2 Wins'
                p2score += 1
            else:
                msg = 'Tie'

            final = minimainfont.render(msg,1,WHITE)
            window.blit(final,(200,300))
            pg.display.update()
            pg.time.delay(5000)
            break

        draw(p1hand, p2hand,hand,p1score,p2score)

        if int(p1hand.hand_total()) > 21 or int(p2hand.hand_total()) > 21:
            if hand == p1hand:
                if p2done == False:
                    p1score += 1
                    hand = p2hand
                else:
                    p2score += 1

            elif hand == p2hand:
                if p1done == False:
                    p2score += 1
                    hand = p1hand
                else:
                    p1score += 1

            draw(p1hand, p2hand, hand, p1score, p2score)
            finished = mainfont.render('BUST',1,(150,0,0))
            window.blit(finished, (400,280))
            pg.display.update()
            pg.time.delay(5000)
            break
        pg.display.update()
    game(p1score,p2score)

def casino(p1score,p2score):
    global font, font2, mainfont, minimainfont

    window.fill(GREEN)
    deck = Deck()
    deck.shuffle()

    p1hand = Hand()
    card = deck.deal()
    p1hand.add_card(card)
    card = deck.deal()
    p1hand.add_card(card)

    p2hand = Hand()
    card = deck.deal()
    p2hand.add_card(card)

    hand = p1hand

    p1done = False
    p2done = False

    run = True
    while run:
        clock.tick(60)
        pg.display.set_caption('Blackjack')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                position = event.pos
                if hitbutton.isOver(position):
                    card = deck.deal()
                    hand.add_card(card)

                if passbutton.isOver(position):
                    if hand == p1hand:
                        p1done = True
                    while AI_hit(p2hand):
                        card = deck.deal()
                        p2hand.add_card(card)
                        hand = p2hand
                        draw(p1hand, p2hand, hand, p1score, p2score)
                        pg.display.update()
                        pg.time.delay(1000)
                    if p2hand.hand_total() <= 21:
                        p2done = True
                    pg.display.update()
            if event.type == pg.MOUSEMOTION:
                position = event.pos
                if hitbutton.isOver(position):
                    hitbutton.colour = DARKBLUE
                else:
                    hitbutton.colour = BLUE
                if passbutton.isOver(position):
                    passbutton.colour = DARKBLUE
                else:
                    passbutton.colour = BLUE



        if p1done == True and p2done == True:
            if p1hand.hand_total() > p2hand.hand_total():
                msg = 'Player 1 Wins'
                p1score += 1
            elif p2hand.hand_total() > p1hand.hand_total():
                msg = 'Casino Wins'
                p2score += 1
            else:
                msg = 'Tie'

            final = minimainfont.render(msg,1,WHITE)
            window.blit(final,(200,300))
            pg.display.update()
            pg.time.delay(5000)
            break

        draw(p1hand, p2hand, hand, p1score, p2score)

        if int(p1hand.hand_total()) > 21 or int(p2hand.hand_total()) > 21:
            if hand == p1hand:
                    p2score += 1

            elif hand == p2hand:
                    p1score += 1

            draw(p1hand, p2hand, hand, p1score, p2score)
            finished = mainfont.render('BUST',1,(150,0,0))
            window.blit(finished, (400,280))
            pg.display.update()
            pg.time.delay(5000)
            break
        pg.display.update()
    casino(p1score,p2score)

program()





