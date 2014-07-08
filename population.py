__author__ = 'stretford'
import chromosome

class population:
    colony = []
    colony_size = 100
    intercross_rate = 0
    agamogenesis_rate = 0
    mutate_rate = 0
    rule_num = 0
    best_gene = chromosome.Chromosome()

    def __init__(self, intercrossRate, agamogenesisRate, mutateRate, rulenum):
        self.intercross_rate = intercrossRate
        self.agamogenesis_rate = agamogenesisRate
        self.mutate_rate = mutateRate
        self.rule_num = rulenum
        #initializing rule sets
        for i in range(0, self.colony_size):
            c = chromosome.randomize_chromosome(4000, 7000, 7, 18)
            self.colony.append(c)

    def __str__(self):
        return "\n".join(repr(c) for c in self.colony)


p = population(0, 0, 0, 7)
print(p)