# GeneticAlgorithmGame

Implements simplifies version of Blackjack, only allowing hits and stands

## Program Structure Overview

### blackjack.py

**Utility Functions**
* create_blackjack_deck
    * creates list of integers to represent a deck of cards
    * 1s represent Aces, 10s represent 10s and face cards
* high_sum
    * calculates sum of hand with Aces as 11s
* low_sum
    * calculates sum of hand with Aces as 1s
* hand_sum
    * returns highest sum that doesn't bust, or the lowest sum if the hand busts
    * used for comparing dealer and player's hands
* hand_state
    * determines if the hand is under 21, has 21, or busts
**Chooser Functions**
* random_chooser
    * randomly chooses to hit or stand
* dealer strategy
    * uses dealer's strategy of hitting if less than 17, standing otherwise
* genetic_algorithm
    * uses genetic algorithm data to choose
**Gameplay Functions**
* play_blackjack_hand
    * plays a hand of blackjack for human through the terminal or with chooser function
    * has extra utilities for training genetic algorithm
* blackjack_tournament
    * plays 100 hands of blackjack for a chooser to test performance

### GeneticAlgorithm.py

contains global params at the beginning of the file to be adjusted by user
* log
    * logs data to log file and console
**Chromosome**
* init
    * creates chromosome data structure
    * represented as 3 maps, one each for pairs, soft hands, and hard hands
* initialize_hands
    * randomly populates chromosome with choices to either hit or stand
* str
    * string representation
**Individual**
* init
    * creates individual with random chromosome
* calc_fitness
    * plays hands of blackjack to determine fitness
    * individual is penalized for losing and rewarded for winning
* crossover
    * child randomly inherits each of the 3 choice maps from either parent
    * iterates through maps and has a chance to mutate each value
* str
    * string representation
* random_population
    * creates population of random individuals
* main
    * runs main genetic algorithm
    * for each generation, each individual is evaluated for fitness, then the best individuals move on and crossover to produce more individuals for the next generation

## Design Notes

#### Example Chromosome

player = Fitness: -214.4
Hard Hands:
5:  {2: 's', 3: 'h', 4: 'h', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 's', 10: 's', 1: 'h'}
6:  {2: 's', 3: 'h', 4: 'h', 5: 's', 6: 's', 7: 's', 8: 'h', 9: 'h', 10: 's', 1: 's'}
7:  {2: 's', 3: 's', 4: 'h', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 'h', 1: 's'}
8:  {2: 's', 3: 's', 4: 'h', 5: 's', 6: 's', 7: 'h', 8: 's', 9: 's', 10: 'h', 1: 'h'}
9:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 's', 8: 'h', 9: 's', 10: 'h', 1: 'h'}
10: {2: 'h', 3: 's', 4: 'h', 5: 's', 6: 'h', 7: 'h', 8: 'h', 9: 's', 10: 'h', 1: 'h'}
11: {2: 's', 3: 'h', 4: 'h', 5: 'h', 6: 's', 7: 'h', 8: 's', 9: 's', 10: 'h', 1: 's'}
12: {2: 's', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 's', 10: 'h', 1: 's'}
13: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 'h', 1: 'h'}
14: {2: 'h', 3: 's', 4: 's', 5: 'h', 6: 'h', 7: 's', 8: 's', 9: 'h', 10: 's', 1: 's'}
15: {2: 'h', 3: 's', 4: 's', 5: 's', 6: 'h', 7: 's', 8: 's', 9: 's', 10: 's', 1: 'h'}
16: {2: 's', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 's', 8: 's', 9: 's', 10: 'h', 1: 's'}
17: {2: 's', 3: 's', 4: 's', 5: 's', 6: 'h', 7: 'h', 8: 's', 9: 's', 10: 'h', 1: 's'}
18: {2: 'h', 3: 's', 4: 'h', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 's', 1: 'h'}
19: {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 'h', 9: 's', 10: 's', 1: 'h'}
20: {2: 'h', 3: 's', 4: 's', 5: 's', 6: 'h', 7: 'h', 8: 's', 9: 'h', 10: 's', 1: 's'}
Soft Hands:
2:  {2: 's', 3: 's', 4: 's', 5: 's', 6: 'h', 7: 'h', 8: 'h', 9: 's', 10: 's', 1: 'h'}
3:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 's', 7: 'h', 8: 'h', 9: 'h', 10: 'h', 1: 'h'}
4:  {2: 'h', 3: 'h', 4: 'h', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 's', 10: 'h', 1: 'h'}
5:  {2: 's', 3: 's', 4: 'h', 5: 'h', 6: 'h', 7: 's', 8: 's', 9: 's', 10: 'h', 1: 'h'}
6:  {2: 'h', 3: 's', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 's', 9: 's', 10: 's', 1: 's'}
7:  {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 'h', 1: 's'}
8:  {2: 'h', 3: 's', 4: 's', 5: 's', 6: 'h', 7: 's', 8: 's', 9: 's', 10: 's', 1: 'h'}
9:  {2: 's', 3: 's', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 's', 9: 'h', 10: 's', 1: 's'}
Pairs:
2:  {2: 'h', 3: 's', 4: 'h', 5: 's', 6: 'h', 7: 's', 8: 'h', 9: 's', 10: 'h', 1: 'h'}
3:  {2: 's', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 'h', 9: 's', 10: 'h', 1: 'h'}
4:  {2: 's', 3: 'h', 4: 's', 5: 's', 6: 'h', 7: 's', 8: 's', 9: 's', 10: 's', 1: 's'}
5:  {2: 's', 3: 'h', 4: 'h', 5: 'h', 6: 'h', 7: 's', 8: 's', 9: 's', 10: 's', 1: 'h'}
6:  {2: 'h', 3: 's', 4: 'h', 5: 'h', 6: 'h', 7: 'h', 8: 's', 9: 'h', 10: 'h', 1: 'h'}
7:  {2: 's', 3: 'h', 4: 's', 5: 's', 6: 's', 7: 's', 8: 'h', 9: 'h', 10: 'h', 1: 's'}
8:  {2: 's', 3: 'h', 4: 's', 5: 's', 6: 's', 7: 'h', 8: 'h', 9: 's', 10: 's', 1: 'h'}
9:  {2: 's', 3: 's', 4: 's', 5: 's', 6: 'h', 7: 's', 8: 'h', 9: 's', 10: 'h', 1: 'h'}
10: {2: 's', 3: 's', 4: 'h', 5: 's', 6: 's', 7: 's', 8: 's', 9: 's', 10: 'h', 1: 's'}
1:  {2: 'h', 3: 'h', 4: 'h', 5: 'h', 6: 's', 7: 's', 8: 'h', 9: 'h', 10: 'h', 1: 'h'}

* Fitness function plays a hand for every combination of 2 cards dealt to the player and 1 dealer card player can see (1000 combinations). Multiple iterations are done and the average fitness of 15 rounds of the 1000 hands is set as the fitness. This is to ensure accuracy in the fitness score. 


