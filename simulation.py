%matplotlib inline
import numpy as np
import pandas as pd

#import viz # curriculum example visualizations

np.random.seed(1349) #


# 1. How likely is it that you roll doubles when rolling two dice?

n_trials = nrows = 10_000
n_dice = ncols= 2
#get the posibles outcomes for each roll
rolls = np.random.choice([1,2,3,4,5,6], n_trials * n_dice).reshape(nrows, ncols)

#lets convert it  to a dataframe so we can use lambda and compare the two columns x[0] == x[1] this gives us a boolean result
res = pd.DataFrame(rolls).apply(lambda x : x[0] == x[1] in x.values, axis=1)

#calculate the mean
prob = res.mean()



# *** not using DataFrame **

#comprehension list
res = [x[0] == x[1] for x in rolls]

# I convert my list to a pdseries
x = pd.Series(res)

#then I calculate the mean
x.mean()

#syntaxis for labda useinf if lambda x: True if x % 2 == 0 else False

# 2. If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

# 3. There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

# 4. Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

# 5. Compare Heights

# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# If a man and woman are chosen at random, P(woman taller than man)?
# When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?

# What is the probability that we observe an installation issue within the first 150 students that download anaconda?

# How likely is it that 450 students all download anaconda without an issue?

# There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?

# How likely is it that a food truck will show up sometime this week?

# If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?