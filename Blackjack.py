import random
import time


# Blackjack and you use only one deck for this game

type = ["of Hearts", "of Diamonds", "of Clubs", "of Spades"]
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "J", "K"]
picked_cards = []
player_sum = 0
dealer_sum = 0
Ace = False

class Player:
    def __init__(self, pcards):
        self.pcards = pcards

    def player_cards(self):
        print("Your cards: {}".format(', '.join(self.pcards)))


class Dealer:
    def __init__(self, dcards):
        self.dcards = dcards
    def dealer_cards(self):
        print("Dealer's cards: {}".format(', '.join(self.dcards)))


# Make random card
def card_generator(TorF):
    global Ace
    num = cards[random.randint(0, 11)]
    name = type[random.randint(0, 3)]
    if num == "A":
        temp = num
        num = 1
        Ace = True
        if TorF == False:
            num = 11
        sum_cards(TorF, num)
        c = temp + " " + name
        return c
    elif num == "Q" or num == "K" or num == "J":
        temp = num
        num = 10
        sum_cards(TorF, num)
        c = temp + " " + name
        return c
    sum_cards(TorF, num)
    c = str(num) + " " + name
    return c

#Keep tracks of sum of cards
def sum_cards(TorF, num):
    global player_sum
    global dealer_sum
    if TorF:
        player_sum += num
    elif not TorF:
        dealer_sum += num

# check if the card has drawn and generate it again if it was
def check_card(generated_card, alist,TorF):
    while True:
        if generated_card not in alist:
            alist.append(generated_card)
            break
        else:
            generated_card = card_generator(TorF)
    return generated_card


#Ask player if they want to take another card and generate another card if so
def add_card(P1):
    while True:
        print("\nWould like to an another card? Y/N")
        answer = input()
        if answer.lower() == "y":
            P1.pcards.append(assign_card(True))
            busted(player_sum, P1)
            P1.player_cards()
            add_card(P1)
            break
        elif answer.lower() == "n":
            break
        else:
            print("The answer has to be Y or N")

#generated card and run through check card function
def assign_card(TorF):
    return check_card(card_generator(TorF), picked_cards, TorF)


#check if player got busted or not
def busted(player_sum, P1):
    if player_sum < 22 and Ace == True:
        if player_sum + 10 < 22:
            player_sum += 10
    if player_sum > 21:
        P1.player_cards()
        print("The sum of your cards is : " + str(player_sum))
        raise SystemExit("Busted! Game over..")
    elif player_sum == 21:
        P1.player_cards()
        print("The sum of your cards is : " + str(player_sum))
        raise SystemExit("Blackjack! You won!")


#compare cards of player and dealer
def compare(player_sum, dealer_sum):
    if player_sum < 22 and Ace == True:
        if player_sum + 10 < 22:
            player_sum += 10
    if player_sum == dealer_sum:
        print("Player sum : " +str(player_sum))
        print("Dealer sum : " + str(dealer_sum))
        raise SystemExit("Tie!")
    elif player_sum > dealer_sum:
        print("Player sum : " + str(player_sum))
        print("Dealer sum : " + str(dealer_sum))
        raise SystemExit("You Won!")
    elif player_sum < dealer_sum and dealer_sum < 22:
        print("Player sum : " + str(player_sum))
        print("Dealer sum : " + str(dealer_sum))

        raise SystemExit("You lost...")


    if player_sum < 22 and Ace == True:
        if player_sum + 10 < 22:
            player_sum += 10
def main():
    p = True
    d = False
    # Setting up the cards
    P1 = Player([assign_card(p), assign_card(p)])
    P1.player_cards()
    D1 = Dealer([assign_card(d)])
    D1.dealer_cards()

    busted(player_sum, P1)
    # Player draws card or not
    add_card(P1)

    # Dealer shows the hidden card
    D1.dcards.append(assign_card(d))
    D1.dealer_cards()

    if (dealer_sum > 16 and player_sum > dealer_sum):
        raise SystemExit("You won!")
    while dealer_sum < 17:
        print("Dealer takes another card")
        D1.dcards.append(assign_card(d))
        time.sleep(1)
        D1.dealer_cards()
        if dealer_sum > 21:
            time.sleep(1)
            raise SystemExit("Dealer got busted... You won!")

    time.sleep(1)
    compare(player_sum, dealer_sum)



main()
