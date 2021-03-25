import math
import random

class Chromosome:

    def __init__(self):
        self.hard_hands = {}
        self.soft_hands = {}
        self.pairs = {}
        self.choices = ['h', 's']

    def initilize_hands(self):
        # Hard hands
        for i in range(5,21):
            _d = {}
            for j in range(2,11):
                move = self.choices[math.trunc(random.random() * len(self.choices))]
                if j == 10:
                    _d['T'] = move
                elif j == 11:
                    _d['A'] = move
                else:
                    _d[j] = move
            self.hard_hands[i] = _d
        #Soft Hands
        for i in range(2,10):
            _d = {}
            for j in range(2,12):
                move = self.choices[math.trunc(random.random() * len(self.choices))]
                if j == 10:
                    _d['T'] = move
                elif j == 11:
                    _d['A'] = move
                else:
                    _d[j] = move
            self.soft_hands[i] = _d
        #Pairs
        for i in range(2, 12):
            _d = {}
            for j in range(2,12):
                move = self.choices[math.trunc(random.random() * len(self.choices))]
                if j == 10:
                    _d['T'] = move
                elif j == 11:
                    _d['A'] = move
                else:
                    _d[j] = move
            self.pairs[i] = _d
    
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

    def update_fitness(self, fitness):
        self.fitness = fitness

    def __str__(self):
        return 'Fitness: ' + str(self.fitness) + '\n' + str(self.chromosome)




class GeneticAlgorithm:

    def __init(self):
        pass


    def genetic(self):

        population_size = 100
        population = []

        for i in range(population_size):
            chrom = Chromosome()
            chrom.initilize_hands()
            population.append(Individual(chrom))
        
        print(population[0])

        # for i in population[0].chromosome.hard_hands:
        #     print(i)

        # for pop in population:
        #     print(pop.chromosome.hard_hands)
        #     break



ga = GeneticAlgorithm()

ga.genetic()
