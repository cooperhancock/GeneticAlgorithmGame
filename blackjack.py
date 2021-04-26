import random
import sys
import GeneticAlgorithm
import math

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
def hand_sum(hand):
    if low_sum(hand) > 21: return low_sum(hand)
    if high_sum(hand) < 22:
        return high_sum(hand)
    else:
        return low_sum(hand)

# calculates state of hand
# returns None if less than 21, False if busted (>21), and True if 21
def hand_state(hand):
    if hand_sum(hand) > 21:
        return False
    elif hand_sum(hand) < 21:
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
    return ga_player.chromosome.hard_hands[hand_sum(hand)][dealer]
        
# chooser that uses ga filled with data from online strategy
# double downs were replaced with holds and pairs copy hard hands
def optimal(hand, dealer):
    optimalGA = GeneticAlgorithm.Individual(GeneticAlgorithm.Chromosome())
    optimalGA.chromosome.hard_hands = {
        5:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        6:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        7:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        8:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        9:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        10: {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        11: {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        12: {2: 'h', 3: 'h', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        13: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        14: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        15: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        16: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        17: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 's', 1: 's'},
        18: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 's', 1: 's'},
        19: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 's', 1: 's'},
        20: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 's', 1: 's'}} 
    optimalGA.chromosome.soft_hands = {
        2:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        3:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        4:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        5:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        6:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        7:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 's', 8: 's', 9: 'h', 10: 'h', 1: 'h'},
        8:  {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 's', 1: 's'},
        9:  {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 's', 1: 's'}}
    optimalGA.chromosome.pairs = {
        2:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        3:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        4:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        5: {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        6: {2: 'h', 3: 'h', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        7: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        8: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'},
        9: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 's', 1: 's'},
        10: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 's', 1: 's'},
        1: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 's', 1: 's'}} 
    return genetic_algorithm(hand, dealer, optimalGA)

# main blackjack game (1 hand)
# return 1 if player wins, 0 if ties, -1 if they lose
def play_blackjack_hand(player,ga_player=None,card1=None,card2=None,dealer_card=None):
    deck = create_blackjack_deck()
    random.shuffle(deck)
    player_hand = [deck.pop(deck.index(card1)),deck.pop(deck.index(card2))] if not (card1==None or card2==None) else [deck.pop(0),deck.pop(0)]
    dealer_hand = [deck.pop(deck.index(dealer_card)),deck.pop(0)] if not dealer_card == None else [deck.pop(0),deck.pop(0)]
    #print("player",player_hand,"dealer",dealer_hand)
    if player == 'human': print("dealer's card: ",dealer_hand[0])
    choice = None
    if hand_state(player_hand):
        if player == 'human': print('you have blackjack!')
        if hand_state(dealer_hand): # check for dealer blackjack
            if player == 'human': print('dealer also has blackjack')
            return 0
        else:
            return 1
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
        if player == 'optimal':
            choice = optimal(player_hand,dealer_hand[0])
        # hit
        if choice == 'h':
            player_hand.append(deck.pop(0))
            if player == 'human': print("new card:",player_hand[len(player_hand)-1])
        # check game state
        if hand_state(player_hand):
            break # if 21
        elif hand_state(player_hand) == False:
            if player == 'human': print('you busted :(')
            return -1
    if hand_state(dealer_hand): # check for dealer blackjack
        if player == 'human': print('dealer has blackjack :(')
        #print("player",player_hand,"dealer",dealer_hand)
        return -1
    # dealer plays
    while high_sum(dealer_hand) < 17 or (low_sum(dealer_hand) < 17 and high_sum(dealer_hand) > 21):
        dealer_hand.append(deck.pop(0))
    # compare hands
    if hand_state(dealer_hand) == False:
        if player == 'human': print('the dealer busted!')
        #print("player",player_hand,"dealer",dealer_hand)
        return 1
    elif hand_sum(dealer_hand) > hand_sum(player_hand):
        if player == 'human': print('you lose :(')
        #print("player",player_hand,"dealer",dealer_hand)
        return -1
    elif hand_sum(dealer_hand) < hand_sum(player_hand):
        if player == 'human': print('you win!')
        #print("player",player_hand,"dealer",dealer_hand)
        return 1
    else:
        if player == 'human': print("it's a tie")
        return 0

def blackjack_tournament(player,num_games=1000):
    score = 0
    for j in range(30):
        for i in range(num_games):
            score += play_blackjack_hand(player)
        print(score / (j + 1))
    return score / 30

if __name__ == "__main__":
    if 'human' in sys.argv:
        print(play_blackjack_hand('human')) 
    if 'tournament' in sys.argv:
        print(blackjack_tournament(sys.argv[sys.argv.index('tournament') + 1],int(sys.argv[sys.argv.index('tournament') + 2])))
    if 'ga' in sys.argv:
        print(play_blackjack_hand('ga'))
    if 'optimal' in sys.argv:
        print(blackjack_tournament('optimal'))
    if 'dealer' in sys.argv:
        print(blackjack_tournament('dealer'))
    else:
        x = input('enter player: ')
        print(play_blackjack_hand(x))                               
