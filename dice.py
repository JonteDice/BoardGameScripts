import random
import matplotlib.pyplot as plt
import numpy as np
import itertools
import math
from scipy.stats import norm

def bino(my_list, sides, total):
    """
    Generates the graph to show the distribution of dice rolls
    """
    xpoints = list(range(total, sides*total+1))
    ypoints = my_list
    plt.bar(xpoints, ypoints)
    plt.show()

    for i in range(total, sides*total+1):
        print("Odds of ", i, ": ", my_list[i-total])
    
def bino_bound(my_list, sides, total, bound, rng):
    sum = 0
    for i in range(bound, sides*total+1):
        sum += my_list[i-total]
    return sum / rng

def simulate_rolls(sides, total, rng):
    """
    Cheap way of running rolls many times to see average rolls
    """
    my_list = [0]*((sides*total)-total+1)
    for i in range(rng):
        sum = 0
        for die in range(total):
            sum += random.randint(1, sides)
            # sum = 5
        my_list[sum-total] += 1
    return my_list

def odds(sides, total, bound):

    outcomes = itertools.product(range(1, sides+1), repeat=total)

    favorable_outcomes = 0
    total_outcomes = 0

    for outcome in outcomes:
        total_outcomes += 1
        if sum(outcome) >= bound:
            favorable_outcomes += 1

    # Calculate the probability
    probability = favorable_outcomes / total_outcomes
    return probability

# def means(sides):
#     """
#     Calculates the means of a dice roll when only assuming one dice
#     """
#     return (1+sides)/2

def means(sides, total):
    """
    Calculates the means of the dice rolls
    """
    return total * (sides + 1) / 2

def variance(mean, sides):
    """
    Calculates the variance based on the sides on a dice and its mean from number of rolls
    """
    variance = 0
    for i in range(1, int((sides/2)+1)):
        variance += (i-mean)**2
    variance *= 2/sides
    return variance

def odds_approx(sides, total, bound):
    """
    Approximate the odds of rolling at least `bound` with `total` dice each having `sides` 
    sides using the normal approximation.
    """
    # Calculate mean and standard deviation
    mean = means(sides, total)
    vari = variance(mean, sides)
    std_dev = math.sqrt(vari)

    # Use normal approximation to find probability
    # Convert bound to the equivalent z-score
    z_score = (bound - mean) / std_dev

    # Calculate the upper tail probability using the normal distribution
    probability = 1 - norm.cdf(z_score)
    return probability



def main():

    # my_list = simulate_rolls(6, 2, 10**6)
    # bino(my_list, 6, 2)
    my_list = simulate_rolls(8, 10, 10**6)
    bino(my_list, 8, 10)
    print(bino_bound(my_list, 8, 10, 45, 10**6))


    # print(odds(6, 2, 9))
    # print(odds_approx(6, 2, 9))
    # print(odds(8, 10, 45))

    #TODO:
    # This should just return 1 but it is returning 93%.
    # Approximation can improve
    # bino_bound seems to do the trick even though it is simulating the rolls several times over to create its own binomial distribution
    print(odds_approx(6, 1, 1))


if __name__ == "__main__":
    main()