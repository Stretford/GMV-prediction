from __future__ import division
__author__ = 'stretford'
import tool
import random


class Gaussian:  # for a single gaussian function:(center, width, degree)
    center = 0
    width = 0
    degree = 0  # degree of usefulness

    def __init__(self, center, width):
        self.center = center
        self.width = width
        #self.Degree = 0

    def __str__(self):
        return ''.join(['(', str(self.center), ',', str(self.width), ')'])

    def cal_degree(self, x):
        self.degree = tool.gaussian(self.center, self.width, x)
        return self.degree


class Rule:  # for a single rule: IF A IS GAUSSIAN(...) AND B IS GAUSSIAN(...) THEN Y IS GAUSSIAN(...)
    gaussian1 = Gaussian(0, 0)
    gaussian2 = Gaussian(0, 0)
    gaussian_y = Gaussian(0, 0)

    def __init__(self, gaussian1, gaussian2, gaussian_y):
        self.gaussian1 = gaussian1
        self.gaussian2 = gaussian2
        self.gaussian_y = gaussian_y

    def __repr__(self):
        return ''.join(['IF A IS ', str(self.gaussian1),
                        ' AND B IS ', str(self.gaussian2), ' THEN Y IS ', str(self.gaussian_y)])

    def defuzzify(self, x1, x2):
        degree1 = tool.gaussian(self.gaussian1.center, self.gaussian1.width, x1)
        degree2 = tool.gaussian(self.gaussian2.center, self.gaussian2.width, x2)
        return degree1 * degree2


class Chromosome:  # for a single chromosome consisting of several rules
    rule_num = 0
    rule_sets = []
    fitness_score = 0

    def __init__(self, rule_num, rule_sets=[]):
        if rule_sets:
            self.rule_sets = rule_sets
            self.rule_num = rule_num
        else:
            for i in range(0, rule_num):
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
        g_sets = [rule.gaussian1, rule.gaussian2, rule.gaussian_y]
        gaussian = random.choice(g_sets)
        if random.random() > 0.5:
            gaussian.center *= 2 * random.random()
        else:
            gaussian.width *= 2 * random.random()

    def fitness(self, inputs):  # calculate the fitness value via inputs in forms of [(x1, x2, y),...]
        mse = 0
        for x1, x2, y in inputs:
            y_predict = self.defuzzify(x1, x2)
            mse += (y_predict - y) ** 2
        mse /= len(inputs)
        return mse


def randomize_rule(center_min, center_max, n_init): # initialize a randomized rule given the bounding range
    max_width = 2 * (center_max - center_min) / (n_init ** 0.5)
    g1 = Gaussian(random.uniform(center_min, center_max), random.uniform(0, max_width))
    g2 = Gaussian(random.uniform(center_min, center_max), random.uniform(0, max_width))
    gy = Gaussian(random.uniform(center_min, center_max), random.uniform(0, max_width))
    return Rule(g1, g2, gy)


def randomize_chromosome(minimum, maximum, rule_num, n_init):
# initialize a randomized chromosome given the bounding range
    rule_sets = []
    for i in range(0, rule_num):
        rule = randomize_rule(minimum, maximum, n_init)
        rule_sets.append(rule)
    return Chromosome(rule_num, rule_sets)


def intercross(p1, p2):  # intercross of two chromosomes for GA
    intercross_point = 2
    c = [i for i in range(0, intercross_point)]
    for i in range(0, intercross_point):
        c[i] = p1.rule_sets[i]
        p1.rule_sets[i] = p2.rule_sets[i]
        p2.rule_sets[i] = c[i]


c = randomize_chromosome(900, 1200, 3, 10)
print(c)
print(' ')
c.mutate()
print(c)

#print randomize_chromosome(4000, 7000, 9, 18)

