__author__ = 'stretford'
import chromosome
import random


class population:
    colony = []
    colony_size = 100
    intercross_rate = 0
    agamogenesis_rate = 0
    mutate_rate = 0
    rule_num = 0
    best_gene = chromosome.Chromosome(7)

    def __init__(self, intercross_rate, agamogenesis_rate, mutate_rate, rulenum):
        self.intercross_rate = intercross_rate
        self.agamogenesis_rate = agamogenesis_rate
        self.mutate_rate = mutate_rate
        self.rule_num = rulenum
        #initializing rule sets
        for i in range(0, self.colony_size):
            c = chromosome.randomize_chromosome(4000, 7000, 7, 18)
            self.colony.append(c)

    def intercross(self):
        intercross_times = int(self.intercross_rate * self.colony_size)
        for i in range(0, intercross_times):
            rand1 = random.randint(0, self.colony_size)
            rand2 = random.randint(0, self.colony_size)
            if rand1 == rand2:
                rand2 = (rand2 + 1) % self.colony_size
            chromosome.intercross(self.colony[rand1], self.colony[rand2])

    def agamogenesis(self):
        agamogenesis_times = int(self.agamogenesis_rate * self.colony_size)
        for i in range(0, agamogenesis_times):
            self.colony.append(self.best_gene)

    def mutate(self):
        mutate_times = int(self.mutate_rate * self.colony_size)
        for i in range(0, mutate_times):
            unfortunate = random.choice(self.colony)
            unfortunate.mutate()

    def keep_size(self):
        sorted_dict = {}
        #for c in self.colony:
            #sorted_dict[c.]

    def next_generation(self):
        self.intercross()
        self.agamogenesis()
        self.mutate()


    def __str__(self):
        return "\n".join(repr(c) for c in self.colony)


p = population(0, 0, 0, 7)
print(p)