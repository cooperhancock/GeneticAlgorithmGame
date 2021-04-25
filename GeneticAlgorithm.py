import math
import random
import time
import blackjack

## GLOBAL PARAMS ##
generations = 100
log_file = "blackjackLogs.txt"
population_size = 100
survivors = 10
mutation_rate = 0.10
log = True
calc_fitness_multiplier = 15

# log function
def log(o=''):
    if log:
        print(str(o))
        with open(log_file,'a') as f:
            f.write(str(o))
            f.write("\n")

class Chromosome:

    def __init__(self):
        self.hard_hands = {}
        self.soft_hands = {}
        self.pairs = {}
        self.choices = ['h', 's']

    # creates random chromosome
    def initilize_hands(self):
        # Hard hands
        for i in range(5,21):
            _d = {}
            for j in range(2,12):
                move = self.choices[math.trunc(random.random() * len(self.choices))]
                if j == 10:
                    _d[10] = move
                elif j == 11:
                    _d[1] = move
                else:
                    _d[j] = move
            self.hard_hands[i] = _d
        #Soft Hands
        for i in range(2,10):
            _d = {}
            for j in range(2,12):
                move = self.choices[math.trunc(random.random() * len(self.choices))]
                if j == 10:
                    _d[10] = move
                elif j == 11:
                    _d[1] = move
                else:
                    _d[j] = move
            self.soft_hands[i] = _d
        #Pairs
        for i in range(2, 12):
            _d = {}
            for j in range(2,12):
                move = self.choices[math.trunc(random.random() * len(self.choices))]
                if j == 10:
                    _d[10] = move
                elif j == 11:
                    _d[1] = move
                else:
                    _d[j] = move
            if i==11: self.pairs[1] = _d
            else: self.pairs[i] = _d

    # to string
    def __str__(self):
        s = ''
        s += "Hard Hands:\n"
        for i in self.hard_hands:
            s += str(i) + ': '
            if i<10: s += ' '
            s += str(self.hard_hands[i]) + '\n'
        s += "Soft Hands:\n"
        for i in self.soft_hands:
            s += str(i) + ': '
            if i<10: s += ' '
            s += str(self.soft_hands[i]) + '\n'
        s += "Pairs:\n"
        for i in self.pairs:
            s += str(i) + ': '
            if i<10: s += ' '
            s += str(self.pairs[i]) + '\n'
        return s


class Individual:

    def __init__(self, chromosome):
        self.fitness = 0
        self.chromosome = chromosome
        self.chromosome.initilize_hands()

    # total possible fitness of 1000 if all games are won
    # for comparison, using dealer strategy yeilds a fitness score of -80
    def calc_fitness(self):
        # play num_games number of blackjack Hands
        global calc_fitness_multiplier
        self.fitness = 0
        for iterations in range(calc_fitness_multiplier):
            for dealer_card in range(1,11): # range of dealer card options
                #print(dealer_card,'of',10)
                # play every combo of player cards
                for i in range(1,11):
                    for j in range(1,11):
                        self.fitness += int(blackjack.play_blackjack_hand('ga',self,i,j,dealer_card))
        self.fitness = self.fitness / calc_fitness_multiplier # take average fitness 
        return self.fitness

    def crossover(self, other):
        global mutation_rate
        child = Individual(Chromosome())
        rand = []
        for i in range(3):
            rand.append(random.randint(0, 100)/100)
        # 50% chance to inherit from each parent
        child.chromosome.hard_hands = self.chromosome.hard_hands if rand[0]<0.50 else other.chromosome.hard_hands
        child.chromosome.soft_hands = self.chromosome.soft_hands if rand[1]<0.50 else other.chromosome.soft_hands
        child.chromosome.pairs = self.chromosome.pairs if rand[2]<0.50 else other.chromosome.pairs
        # mutation sequence
        for row in child.chromosome.hard_hands:
            for choice in child.chromosome.hard_hands[row]:
                rand = random.randint(0, 100)/100
                if rand < mutation_rate: # chance to mutate
                    choice = self.chromosome.choices[random.randint(0, 1)]
        for row in child.chromosome.soft_hands:
            for choice in child.chromosome.soft_hands[row]:
                rand = random.randint(0, 100)/100
                if rand < mutation_rate: # chance to mutate
                    choice = self.chromosome.choices[random.randint(0, 1)]
        for row in child.chromosome.pairs:
            for choice in child.chromosome.pairs[row]:
                rand = random.randint(0, 100)/100
                if rand < mutation_rate: # chance to mutate
                    choice = self.chromosome.choices[random.randint(0, 1)]

        return child # return Individual

    def __str__(self):
        return 'Fitness: ' + str(self.fitness) + '\n' + str(self.chromosome)

# create population of given
def random_population(size):
    population = []
    for i in range(size):
        population.append(Individual(Chromosome()))
    return population

def main():
    # initial population
    population = random_population(population_size)
    # generation count
    generation = 1
    # setup log
    log()
    log(time.asctime(time.localtime(time.time())))
    # calculate run time
    timeStart = time.time()
    print('calculating run time...')
    dummyPop = random_population(int(population_size//10))
    for individual in dummyPop:
        individual.calc_fitness()
    log('estimated time to complete: ' + str(((time.time()-timeStart)*10*generations/60)) + ' minutes')
    x = input('Press Enter to continue or q to quit: ')
    if x == 'q':
        return

    # MAIN SIM #

    while generation < generations:
        # calculate fitness of population
        timeStart = time.time()
        log('CALCULATING FITNESS...')
        for i in range(population_size):
            population[i].calc_fitness()
            print(i,"of",population_size)
        log(str(generation) + ' calc_fitness time = ' + str(time.time()-timeStart))

        # sorts population by fitness
        population.sort(key=lambda x: x.fitness, reverse=True)
        highestFitness = population[0].fitness
        s = ''
        for i in range(population_size):
            s += str(population[i].fitness)
            s += ' '
        log("fitness distribution: " + s)
        log('highest fitness = ' + str(highestFitness))
        log('player = ' + str(population[0]))

        # create new population
        newPopulation = []

        # move best players to next generation
        for i in range(survivors):
            newPopulation.append(population[i])

        # cross best 50% of population
        log('CROSSING...')
        for i in range(population_size-survivors):
            rand = random.randint(0,population_size/2)
            parent1 = population[rand]
            rand = random.randint(0,population_size/2)
            parent2 = population[rand]
            child = parent1.crossover(parent2)
            newPopulation.append(child)

        # set population to new population
        population = newPopulation
        generation+=1
    log("end")

if __name__ == "__main__":
    main()
