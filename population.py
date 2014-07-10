__author__ = 'stretford'
import chromosome
import random


class population:
    colony = []
    colony_size_allowed = 100
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
        for i in range(0, self.colony_size_allowed):
            c = chromosome.randomize_chromosome(4000, 7000, 7, 18)
            self.colony.append(c)

    def intercross(self):
        intercross_times = int(self.intercross_rate * len(self.colony))
        for i in range(0, intercross_times):
            rand1 = random.randint(0, len(self.colony))
            rand2 = random.randint(0, len(self.colony))
            if rand1 == rand2:
                rand2 = (rand2 + 1) % self.colony_size_allowed
            chromosome.intercross(self.colony[rand1], self.colony[rand2])

    def agamogenesis(self):
        agamogenesis_times = int(self.agamogenesis_rate * len(self.colony))
        for i in range(0, agamogenesis_times):
            self.colony.append(self.best_gene)

    def mutate(self):
        mutate_times = int(self.mutate_rate * len(self.colony))
        for i in range(0, mutate_times):
            unfortunate = random.choice(self.colony)
            unfortunate.mutate()

    def keep_size(self):
        sorted_dict = []
        for i in range(0, len(self.colony)):
            sorted_dict.append((i, self.colony[i].fitness_score))
        sorted_dict.sort(cmp=lambda x, y: cmp(x[1], y[1]))
        for i in range(self.colony_size_allowed, len(sorted_dict)):
            tp = sorted_dict[i][0]  # get the sequence in colony
            self.colony.remove(tp)


    def next_generation(self):
        self.intercross()
        self.agamogenesis()
        self.mutate()


    def __str__(self):
        return "\n".join(repr(c) for c in self.colony)


p = population(0, 0, 0, 7)
print(p)