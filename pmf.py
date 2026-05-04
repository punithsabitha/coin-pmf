import scipy.stats as stats

# number of heads
# change this
a = 2
b = 4

# number of coin flips
# change this
n = 10

# probability of head
p = 0.5

# calculate probability
result = 0

for i in range(a, b + 1):
    result = result + stats.binom.pmf(i, n, p)

print("Probability of getting heads between 2 and 4")
print(result)