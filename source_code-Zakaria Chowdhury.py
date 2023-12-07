# Binomial Theorem Probability Calculator by Zakaria Chowdhury
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def binomial_probability(n, k, probability):
    numerator = factorial(n)
    denominator = factorial(n-k) * factorial(k)
    binomial_coefficient = numerator/denominator

    first_term = probability**k
    second_term = (1-probability)**(n-k)

    return binomial_coefficient * first_term * second_term

print("Enter the number of steps to solve the problem:")
n = int(input())

print("Enter the number of steps we are interested in:")
k = int(input())

print("What's the probability of what we're interested in happening?")
probability = float(input())

result = binomial_probability(n,k,probability)

print("Your probability is:", result)

