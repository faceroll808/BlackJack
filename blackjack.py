total_dealer = 0
total_player = 0
player = 10000


def start():
    global player
    global total_player
    global total_dealer
    import random

    class card:
        def __init__(self, name, suit, value):
            self.name = name
            self.suit = suit
            self.value = value

        def get_info(self):
            return f"{self.name} of {self.suit}"

        def __str__(self):
            return f"{self.name} of {self.suit}"

        def __repr__(self):
            return f"{self.name} of {self.suit}"

    def shuffle():
        if len(deck) < 10:
            for name in names:
                for suit in suits:
                    deck.append(card(name, suit, names[name]))

    def random_range():
        return (random.randrange(0, len(deck)))

    def draw_card():
        randnum = random_range()
        card = deck[randnum]
        deck.pop(randnum)
        return (card)

    def count_player_aces():
        global total_player
        total_player = 0
        aces = 0
        for card in player_cards:
            total_player = total_player + card.value
            if card.name == "Ace":
                aces += 1
        while total_player > 21 and aces > 0:
            total_player -= 10
            aces -= 1

    def count_dealer_aces():
        global total_dealer
        total_dealer = 0
        aces = 0
        for card in dealer_cards:
            total_dealer = total_dealer + card.value
            if card.name == "Ace":
                aces += 1
        while total_dealer > 21 and aces > 0:
            total_dealer -= 10
            aces -= 1

    def display_player():
        for card in player_cards:
            print(card.get_info())

    some_card = card('King', 'Spades', 10)

    # ace=11 or 1
    names = {'Ace': 11, 'King': 10, 'Queen': 10, 'Jack': 10, 'Ten': 10, 'Nine': 9, 'Eight': 8, 'Seven': 7, 'Six': 6,
             'Five': 5, 'Four': 4, 'Three': 3, 'Two': 2}
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    deck = []

    for name in names:
        for suit in suits:
            deck.append(card(name, suit, names[name]))
    # for card in deck:
    #	print(f'{card.name} of {card.suit} {card.value}')

    dealer = 10000000000

    print(f'player total: ${player}')
    bet = input('Enter Wager: ')
    if int(bet) > int(player):
        print('You do not have enough money')
    else:
        player = int(player) - int(bet)
    print(f'player total: ${player}')

    dfirst_card = draw_card()
    dsecond_card = draw_card()
    pfirst_card = draw_card()
    psecond_card = draw_card()

    # dealer_hand=(names.get['dfirst_card'])
    # print (dealer_hand)
    total_dealer = int(dfirst_card.value + dsecond_card.value)
    total_player = int(pfirst_card.value + psecond_card.value)

    dealer_cards = [dfirst_card, dsecond_card]
    # (f'dealer cards:{dfirst_card.name} of {dfirst_card.suit} and {dsecond_card.name} of {dsecond_card.suit} = {total_dealer}')
    player_cards = [pfirst_card, psecond_card]
    # (f'Player cards:{pfirst_card.name} of {pfirst_card.suit} and {psecond_card.name} of {psecond_card.suit} = {total_player}')
    draw_cards = (f'{draw_card}')

    print(f"Dealer has:'[{dfirst_card.get_info()}]', 'Face Down' = {dfirst_card.value}")
    print(f'Player has:{player_cards} = {total_player}')

    while True:
        if total_player > 21:
            print("Bust!")
            break

        player_action = int(input('what would you like to do? 1:Hit 2:stand 3:surrender: '))
        if player_action == 1:
            card = draw_card()
            player_cards.append(card)
            # total_player = total_player + card.value
            count_player_aces()
            # total_player=(f'{int(total_player) + card.value}')
            print(f'{player_cards} = {total_player}')

        elif player_action == 2:
            print(f'Player has:{player_cards} = {total_player}')
            break

        elif player_action == 3:
            player = (f'{int(player) + int(bet) / 2}')
            print(f'player total = ${player}')
            start()
        else:
            print('Make another selection!')

    count_dealer_aces()
    print(f"Dealer has: {dealer_cards} = {total_dealer}")
    while True:
        if total_player > 21:
            break
        if total_dealer > 21:
            print("Bust!")
            break

        if int(total_dealer) <= 16:
            card = draw_card()
            dealer_cards.append(card)
            # total_dealer = total_dealer + card.value
            count_dealer_aces()
            # total_dealer=(f'{int(total_dealer) + card.value}')
            print("dealer hits")
            print(f'Dealer Has:{dealer_cards} = {total_dealer}')

        else:
            print("dealer stands")
            break
    if total_dealer > 21:
        print("player wins")
        player = f'{int(player) + int(bet) * 2}'
        print(player)
    elif int(total_dealer) > int(total_player):
        print("dealer wins")
    elif int(total_dealer) == int(total_player):
        print("push")
    elif total_player > 21:
        print("dealer wins")
    else:
        print("player wins")
        player = f'{int(player) + int(bet) * 2}'
        print(player)
    shuffle()

    restart = input("do you want to play again? ").lower()

    if restart == 'yes':
        start()
    else:
        exit()


start()