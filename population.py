__author__ = 'stretford'
import chromosome
import random
import test


class population:
    colony = []
    colony_size_allowed = 20
    intercross_rate = 0.8
    agamogenesis_rate = 0.1
    mutate_rate = 0.05
    rule_num = 0

    def __init__(self, rulenum, ranges):
        self.rule_num = rulenum
        #initializing rule sets
        for i in range(0, self.colony_size_allowed):
            c = chromosome.randomize_chromosome(ranges, rulenum)
            self.colony.append(c)

    def best_gene(self):
        best_score = -1
        best_gene = chromosome.Chromosome(7)
        for c in self.colony:
            if c.fitness_score >= best_score:
                best_gene = c
        return best_gene

    def intercross(self):
        intercross_times = int(self.intercross_rate * len(self.colony))
        for i in range(0, intercross_times):
            rand1 = random.randint(0, len(self.colony) - 1)
            rand2 = random.randint(0, len(self.colony) - 1)
            if rand1 == rand2:
                rand2 = (rand2 + 1) % self.colony_size_allowed
            chromosome.intercross(self.colony[rand1], self.colony[rand2])

    def agamogenesis(self):
        agamogenesis_times = int(self.agamogenesis_rate * len(self.colony))
        for i in range(0, agamogenesis_times):
            self.colony.append(self.best_gene())

    def mutate(self):
        mutate_times = int(self.mutate_rate * len(self.colony))
        for i in range(0, mutate_times):
            unfortunate = random.choice(self.colony)
            unfortunate.mutate()

    def keep_size(self):
        sorted_dict = []
        for i in range(0, len(self.colony)):
            sorted_dict.append((self.colony[i], self.colony[i].fitness_score))
        sorted_dict.sort(cmp=lambda x, y: cmp(x[1], y[1]), reverse=True)
        colony_new = []
        for i in range(0, self.colony_size_allowed):
            chmsm = sorted_dict[i][0]
            colony_new.append(chmsm)
        self.colony = colony_new

    def next_generation(self):
        self.intercross()
        self.agamogenesis()
        self.mutate()

    def __str__(self):
        return "\n\n".join(repr(c) for c in self.colony)

# test for GA
inputs = test.data1
ranges = test.ranges
p = population(9, ranges)
for i in range(0, 20):
    for c in p.colony:
        c.fitness_score = c.cal_fitness(inputs)
    p.next_generation()
    p.keep_size()

print(p.best_gene())
print(','.join(str(c.fitness_score) for c in p.colony))

y = p.best_gene().defuzzify(1767307288, 1892712653)
print(str(y))