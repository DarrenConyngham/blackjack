from random import choice
from art import logo

def deal_card():
    """Returns one random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(hand):
    """Calculates the score of the current hand"""
    return sum(hand)


def display_score():
    """Prints out the current score."""
    print(f"\tYour cards: {player_hand}, current score: {calculate_score(player_hand)} \n\tComputer's first card: {dealer_hand[0]}")


def final_score():
    """Displays the current score and prints out the final score."""
    display_score()
    print(f"\tYour final hand: {player_hand}, final_score: {calculate_score(player_hand)}")
    print(f"\tComputer's final hand: {dealer_hand}, final_score: {calculate_score(dealer_hand)}")


def main_menu():
    """Displays the main menu and initiates the game play"""
    print(logo)
    answer = input("Do you want to play a game of of blackjack? ")
    if answer.lower() == 'y':
        game_play()
    else:
        quit()


def game_play():
    """The main game play of the game"""
    global player_hand
    player_hand = [deal_card(), deal_card()]

    global dealer_hand
    dealer_hand = [deal_card(), deal_card()]
    
    display_score()

    global play_more
    play_more = input("Type 'y' to get another card, type 'n' to pass: ")

    while play_more == 'y': 
        player_hand.append(deal_card())
        if calculate_score(player_hand) > 21:
            break
        if calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card())
        display_score()
        play_more = input("Type 'y' to get another card, type 'n' to pass: ")

    end_game_conditions()
    game_play() 


def end_game_conditions():
    """Calculates and displays the end game output"""
    final_score()
    if calculate_score(player_hand) > 21:
        print("You went over you lose :(")      

    elif play_more != 'y':
        if calculate_score(dealer_hand) > 21:
            print("Computer went over. You win.")
        elif calculate_score(dealer_hand) > calculate_score(player_hand):
            print('You lose')
        elif calculate_score(dealer_hand) == calculate_score(player_hand):
            print('It is a draw')
        else:
            print('You win!')

    main_menu()


if __name__ == '__main__':
    main_menu()