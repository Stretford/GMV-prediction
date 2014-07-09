from __future__ import division
__author__ = 'stretford'
import tool
import random


class Gaussian:  # for a single gaussian function:(center, width, degree)
    Center = 0
    Width = 0
    Degree = 0  # degree of usefulness

    def __init__(self, center, width):
        self.Center = center
        self.Width = width
        #self.Degree = 0

    def __str__(self):
        return ''.join(['(', str(self.Center), ',', str(self.Width), ')'])

    def cal_degree(self, x):
        self.Degree = tool.gaussian(self.Center, self.Width, x)
        return self.Degree


class Rule:  # for a single rule: IF A IS GAUSSIAN(...) AND B IS GAUSSIAN(...) THEN Y IS GAUSSIAN(...)
    Gaussian1 = Gaussian(0, 0)
    Gaussian2 = Gaussian(0, 0)
    GaussianY = Gaussian(0, 0)

    def __init__(self, gaussian1, gaussian2, gaussiany):
        self.Gaussian1 = gaussian1
        self.Gaussian2 = gaussian2
        self.GaussianY = gaussiany

    def __repr__(self):
        return ''.join(['IF A IS ', str(self.Gaussian1), ' AND B IS ', str(self.Gaussian2), ' THEN Y IS ', str(self.GaussianY)])

    def Defuzzify(self, x1, x2):
        degree1 = tool.gaussian(self.Gaussian1.Center, self.Gaussian1.Width, x1)
        degree2 = tool.gaussian(self.Gaussian2.Center, self.Gaussian2.Width, x2)
        return degree1 * degree2


class Chromosome:  # for a single chromosome consisting of several rules
    ruleNum = 0
    rule_sets = []

    def __init__(self, rulenum, rulesets=[]):
        if rulesets:
            self.rule_sets = rulesets
            self.ruleNum = rulenum
        else:
            for i in range(0, rulenum):
                self.rule_sets.append(-1)

    def __repr__(self):
        str = "\n".join(repr(rule) for rule in self.rule_sets)
        return str

    def defuzzify(self, x1, x2):  # calculate the predictive output via defuzzification of rules
        sums = weights = 0
        for i in range(0, self.ruleNum):
            amd = self.rule_sets[i].Defuzzify(x1, x2)
            sums += amd * self.rule_sets[i].GaussianY.Center
            weights += amd
        return sums / weights

    def mutate(self):
        rule = self.rule_sets[random.randint(0, len(self.rule_sets) - 1)]
        g_sets = [rule.Gaussian1, rule.Gaussian2, rule.GaussianY]
        gaussian = random.choice(g_sets)
        if random.random() > 0.5:
            gaussian.Center *= 2 * random.random()
        else:
            gaussian.Width *= 2 * random.random()


def randomize_rule(center_min, center_max, N_init):
    max_width = 2 * (center_max - center_min) / (N_init ** 0.5)
    g1 = Gaussian(random.uniform(center_min, center_max), random.uniform(0, max_width))
    g2 = Gaussian(random.uniform(center_min, center_max), random.uniform(0, max_width))
    gy = Gaussian(random.uniform(center_min, center_max), random.uniform(0, max_width))
    return Rule(g1, g2, gy)


def randomize_chromosome(min, max, rulenum, n_init):
    rule_sets = []
    for i in range(0, rulenum):
        rule = randomize_rule(min, max, n_init)
        rule_sets.append(rule)
    return Chromosome(rulenum, rule_sets)


def intercross(p1, p2):
    intercross_point = 2
    c = [i for i in range(0, intercross_point)]
    for i in range(0, intercross_point):
        c[i] = p1.rule_sets[i]
        p1.rule_sets[i] = p2.rule_sets[i]
        p2.rule_sets[i] = c[i]





c = randomize_chromosome(900,1200,3,10)
print(c)
print(' ')
c.mutate()
print(c)

#print randomize_chromosome(4000, 7000, 9, 18)

