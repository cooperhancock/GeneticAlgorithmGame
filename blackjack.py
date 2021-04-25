import random
import sys
import GeneticAlgorithm

# genetic algorithm individual
GA = None

# creates deck of cards for blackjack as a list of integers (16 10s instead of 10s and face cards)
def create_blackjack_deck():
    deck = []
    for i in range(1,14):
        for j in range(4):
            deck.append(min(i,10))
    return deck

# calculates sum of hand with Aces as 11
def high_sum(hand):
    sum = 0
    ace_made_11 = False
    for i in hand:
        if i == 1 and not ace_made_11:
            sum += 11
            ace_made_11 = True
        else:
            sum += i
    return sum

# calculates sum of hand with Aces as 1
def low_sum(hand):
    sum = 0
    for i in hand:
        sum += i
    return sum

# calculates highest sum that doesn't bust or lowest sum
def sum(hand):
    if low_sum(hand) > 21: return low_sum(hand)
    if high_sum(hand) < 22:
        return high_sum(hand)
    else:
        return low_sum(hand)

# calculates state of hand
# returns None if less than 21, False if busted (>21), and True if 21
def hand_state(hand):
    if sum(hand) > 21:
        return False
    elif sum(hand) < 21:
        return None
    else:
        return True
    

## CHOOSERS ##

# randomly returns hit or stand
def random_chooser():
    if random.randint(0,1) == 1:
        return 'h'
    else:
        return 's'

# uses dealer strategy of hitting if sum is under 17
def dealer_strategy(hand):
    if high_sum(hand) < 17 or (low_sum(hand) < 17 and high_sum(hand) > 21):
        return 'h'
    else:
        return 's'

# use genetic algorithm chromosome to choose
def genetic_algorithm(hand, dealer, ga_player):
    #print(GA)
    #print('hand',hand,'dealer',dealer)
    # pairs & soft hands
    if len(hand) == 2:
        # pairs
        if hand[0] == hand[1]:
            #print('pair')
            return ga_player.chromosome.pairs[hand[0]][dealer]
        # soft hand
        elif 1 in hand:
            #print('soft')
            if not hand[0] == 1:
                return ga_player.chromosome.soft_hands[hand[0]][dealer]
            else:
                return ga_player.chromosome.soft_hands[hand[1]][dealer]
    # hard hands
    #print('hard')
    return ga_player.chromosome.hard_hands[sum(hand)][dealer]
        


# main blackjack game (1 hand)
# return True if player wins or ties, False if they lose
def play_blackjack_hand(player,ga_player=None):
    deck = create_blackjack_deck()
    random.shuffle(deck)
    player_hand = [deck.pop(0),deck.pop(0)]
    dealer_hand = [deck.pop(0),deck.pop(0)]
    if player == 'human': print("dealer's card: ",dealer_hand[0])
    choice = None
    if hand_state(player_hand):
            if player == 'human': print('you have blackjack!')
            return True
    while not choice == 's':
        if player == 'human': print("your hand:",player_hand)
        # choice
        if player == 'human':
            choice = input("enter s for stand or h for hit: ")
        if player == 'random':
            choice = random_chooser()
        if player == 'dealer':
            choice = dealer_strategy(player_hand)
        if player == 'ga':
            choice = genetic_algorithm(player_hand,dealer_hand[0],ga_player)
            #print(choice)
        # hit
        if choice == 'h':
            player_hand.append(deck.pop(0))
            if player == 'human': print("new card:",player_hand[len(player_hand)-1])
        # check game state
        if hand_state(player_hand):
            if player == 'human': print('you have 21!')
            return True
        elif hand_state(player_hand) == False:
            if player == 'human': print('you busted :(')
            return False
    if hand_state(dealer_hand): # check for dealer blackjack
        if player == 'human': print('dealer has blackjack :(')
        #print("player",player_hand,"dealer",dealer_hand)
        return False
    # dealer plays
    while high_sum(dealer_hand) < 17 or (low_sum(dealer_hand) < 17 and high_sum(dealer_hand) > 21):
        dealer_hand.append(deck.pop(0))
    # compare hands
    if hand_state(dealer_hand) == False:
        if player == 'human': print('the dealer busted!')
        #print("player",player_hand,"dealer",dealer_hand)
        return True
    elif sum(dealer_hand) > sum(player_hand):
        if player == 'human': print('you lose :(')
        #print("player",player_hand,"dealer",dealer_hand)
        return False
    else:
        if player == 'human': print('you win!')
        #print("player",player_hand,"dealer",dealer_hand)
        return True

def blackjack_tournament(player,num_games=100):
    wins = 0
    for i in range(num_games):
        if play_blackjack_hand(player): wins += 1
    return wins

if __name__ == "__main__":
    if 'human' in sys.argv:
        play_blackjack_hand('human')
    if 'tournament' in sys.argv:
        print(blackjack_tournament(sys.argv[sys.argv.index('tournament') + 1],int(sys.argv[sys.argv.index('tournament') + 2])))
    if 'ga' in sys.argv:
        print(play_blackjack_hand('ga'))
    else:
        x = input('enter player: ')
        print(play_blackjack_hand(x))                               
