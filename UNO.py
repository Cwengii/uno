import random
# Initializing
def initialize_game():
    a = input("Welcome to the Game UNO, press enter to play: ").strip().lower()
    print("""UNO Game Rules: The first player is normally the player to the left of the dealer (you can also choose the youngest player) 
          and gameplay usually follows a clockwise direction. Every player views his/her cards and tries to match the card in the Discard Pile.
          You have to match either by the number, color, or the symbol/Action. For instance, if the Discard Pile has a red card that is an 8 you have to place either a red card or a card with an 8 on it. You can also play a Wild card (which can alter current color in play).
If the player has no matches or they choose not to play any of their cards even though they might have a match, they must draw a card from the Draw pile. If that card can be played, play it. Otherwise, keep the card, and the game moves on to the next person in turn. You can also play a Wild card, or a Wild Draw Four card on your turn.

Note: If the first card turned up from the Draw Pile (to form the Discard Pile) is an Action card, the Action from that card applies and must be carried out by the first player (as stated, it is usually the player to the dealer’s left). The exceptions are if a Wild or Wild Draw Four card is turned up.
 If it is a Wild card, Mattel has now stated that the first player to start (usually the one on the dealer’s left), can choose whatever color to begin play. If the first card is a Wild Draw Four card – Return it to the Draw Pile, shuffle the deck, and turn over a new card. At any time during the game, if the Draw Pile becomes depleted and no one has yet won the round, take the Discard Pile, shuffle it, and turn it over to regenerate a new Draw Pile.

Take note that you can only put down one card at a time; you cannot stack two or more cards together on the same turn. For example, you cannot put down a Draw Two on top of another Draw Two, or Wild Draw Four during the same turn, or put down two Wild Draw Four cards together.

The game continues until a player has one card left. The moment a player has just one card they must yell “UNO!”. If they are caught not saying “Uno” by another player before the next player has taken their turn, that player must draw two new cards as a penalty. Assuming that the player is unable to play/discard their last card and needs to draw, but after drawing, is then able to play/discard that penultimate card, the player has to repeat the action of calling out “Uno”. The bottom line is – Announcing “Uno” needs to be repeated every time you are left with one card. Once a player has no cards remaining, the game round is over, points are scored, and the game begins over again. Normally, everyone tries to be the first one to achieve 500 points, but you can also choose whatever points number to win the game, as long as everyone agrees to it.""")
    # if a != "yes":
    #     print("Game Exiting.")
    #     return False
    
    input("Click any key to start playing.")
    print(" ")
    print("************Game Start************")
    print(" ")
    return True

# Create a deck of cards
def create_deck():
    colours = ["Red", "Blue", "Yellow", "Green"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Skip", "Reverse", "Draw 2"]
    special_cards = ["Wild", "Wild draw 4"]

    deck = [(colour, value) for colour in colours for value in values]
    deck.extend([(colour, value) for colour in colours for value in values if value != 0])
    deck.extend([(None, card) for card in special_cards for _ in range(4)])
    
    random.shuffle(deck)
    return deck

    # Discard pile
    discard =[deck.pop()]
    print("Player 1:" , Player)
    print("                           ")
    # print("Player 2:", Computer)
    print("                           ")
    print("Top Card:", discard[-1])
    print("                           ")

# Handing out cards to player
def deal_cards(deck):
    return [deck.pop(0) for _ in range(7)]

# Check if the card can be played
def can_play(card, top_card):
    return (card[0] == top_card[0] or 
            card[1] == top_card[1] or 
            card[0] is None)  # Wild cards can always be played

# Player's turn
def player_turn(player_hand, discard):
    print(f"Cards: {player_hand}")
    print(f"Top card: {discard[-1]}")
    
    while True:
        card_idx = input(f"Select a card you want to play (0-{len(player_hand)-1}) or 'draw': ").strip().lower()
        
        if card_idx == 'draw':
            new_card = deck.pop()
            player_hand.append(new_card)
            print(f"You drew: {new_card}")
            return False  # Move to the computer's turn
        
        try:
            card_idx = int(card_idx)
            if can_play(player_hand[card_idx], discard[-1]):
                return player_hand.pop(card_idx)
            else:
                print("Wrong card, it doesn't match the top card. Select another card and try again.")
        except (ValueError, IndexError):
            print("Invalid entry, try again.")


# Computer's turn
def computer_turn(computer_hand, discard):
    playable_cards = [card for card in computer_hand if can_play(card, discard[-1])]
    
    if playable_cards:
        card_to_play = playable_cards[0]
        computer_hand.remove(card_to_play)
        print(f"\nComputer played: {card_to_play}")
        return card_to_play
    else:
        new_card = deck.pop()
        computer_hand.append(new_card)
        print("\nComputer drew a card.")
        return False

# Special cards 
def handle_special_card(card, player_hand, computer_hand):
    if card[1] == "Skip":
        print("Player's turn skipped!")
        return "skip"
    elif card[1] == "Draw 2":
        print("Player draws 2 cards!")
        for _ in range(2):
            computer_hand.append(deck.pop())
        return "draw 2"
    elif card[1] == "Wild":
        chosen_color = input("Select a color (Red, Blue, Yellow, Green): ").capitalize()
        return (chosen_color, "Wild")
    elif card[1] == "Wild draw 4":
        print("Player draws 4 cards!")
        for _ in range(4):
            computer_hand.append(deck.pop())
        chosen_color = input("Select a color (Red, Blue, Yellow, Green): ").capitalize()
        return (chosen_color)
    return None

# Check if someone has one card left
def check_uno(player_hand, name):
    if len(player_hand) == 1:
        print(f"{name} UNO!")

# Check if someone has zero cards left
def check_winner(player_hand, name):
    if len(player_hand) == 0:
        print(f"{name} wins!")
        return True
    return False

# Game loop
def game_loop():
    global deck
    deck = create_deck()
    
    player_hand = deal_cards(deck)
    computer_hand = deal_cards(deck)
    
    discard = [deck.pop()]
    
    while True:
        # Player's turn
        player_move = player_turn(player_hand, discard)
        if player_move:
            discard.append(player_move)
            check_uno(player_hand, "Player")
            if check_winner(player_hand, "Player"):
                break
            special_action = handle_special_card(player_move, player_hand, computer_hand)
            if special_action == "skip":
                continue

        # Computer's turn
        computer_move = computer_turn(computer_hand, discard)
        if computer_move:
            discard.append(computer_move)
            check_uno(computer_hand, "Computer")
            if check_winner(computer_hand, "Computer"):
                break
            special_action = handle_special_card(computer_move, player_hand, computer_hand)

# Main game entry
if initialize_game():
    game_loop()