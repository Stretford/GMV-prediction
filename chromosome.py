from __future__ import division
__author__ = 'stretford'
import tool
import random


class Gaussian: ##for a single gaussian function:(center, width, degree)
    Center = 0
    Width = 0
    Degree = 0  #degree of usefulness
    def __init__(self, center, width):
        self.Center = center
        self.Width = width
        #self.Degree = 0
    def __str__(self):
        return ''.join(['(', str(self.Center), ',', str(self.Width), ')'])

    def cal_degree(self, x):
        self.Degree = tool.gaussian(self.Center, self.Width, x)
        return self.Degree

class Rule: ##for a single rule: IF A IS GAUSSIAN(...) AND B IS GAUSSIAN(...) THEN Y IS GAUSSIAN(...)
    Gaussian1 = Gaussian(0, 0)
    Gaussian2 = Gaussian(0, 0)
    GaussianY = Gaussian(0, 0)
    def __init__(self, gaussian1, gaussian2, gaussiany):
        self.Gaussian1 = gaussian1
        self.Gaussian2 = gaussian2
        self.GaussianY = gaussiany
    def __str__(self):
        return ''.join(['IF A IS ', str(self.Gaussian1), ' AND B IS ', str(self.Gaussian2), ' THEN Y IS ', str(self.GaussianY)])

    def Defuzzify(self, x1, x2):
        degree1 = tool.gaussian(self.Gaussian1.Center, self.Gaussian1.Width, x1)
        degree2 = tool.gaussian(self.Gaussian2.Center, self.Gaussian2.Width, x2)
        return degree1 * degree2


class Chromosome: ##for a single chromosome consisting of several rules
    ruleNum = 0
    rule_sets = []
    def __init__(self, rulesets):
        self.rule_sets = rulesets
        self.ruleNum = len(self.rule_sets)
        """
        for i in range(0, rulenum):
            r = Rule()
            self.rule_sets.append(r)
        """

    def Defuzzify(self, x1, x2): ##calculate the predictive output via defuzzification of rules
        sums = weights = 0
        for i in range(0, self.ruleNum):
            amd = self.rule_sets[i].Defuzzify(x1, x2)
            sums += amd * self.rule_sets[i].GaussianY.Center
            weights += amd
        return sums / weights


def RandomRule(center_min, center_max, N_init):
    max_width = 2 * (center_max - center_min) / (N_init ** 0.5)
    g1 = Gaussian(random.uniform(center_min, center_max), random.uniform(0, max_width))
    g2 = Gaussian(random.uniform(center_min, center_max), random.uniform(0, max_width))
    gy = Gaussian(random.uniform(center_min, center_max), random.uniform(0, max_width))
    return Rule(g1, g2, gy)


def Intercross(p1, p2):
    IntercrossPoint = 2
    c1 = Chromosome()
    c2 = Chromosome()
    #for i in range(0, IntercrossPoint):

rule_sets = []
for i in range(9):
    rule = RandomRule(7000, 12000, 18)
    rule_sets.append(rule)

c = Chromosome(rule_sets)
y = c.Defuzzify(9700, 9900)
#print rule
print y
#print(tool.gaussian(5000, 200, 4900))

