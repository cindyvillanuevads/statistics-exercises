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

# 2. If you flip 8 coins, what is the probability of getting exactly 3 heads? 
# What is the probability of getting more than 3 heads?
n_trial = n_rows = 10_000
n_coins = n_cols = 8
#heads=0
flips =  np.random.choice([0,1], n_trial * n_coins).reshape(n_rows, n_cols)

sum_by_flips = flips.sum(axis =1)
heads = sum_by_flips == 3
heads3= heads.mean()

heads_more = sum_by_flips > 3
heads_more_3 = heads_more.mean()

# 3. There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup.
#  Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards 
# I drive past both have data science students on them?
p_ds = 1/4
n_billb = n_cols = 2
n_simulated_al = n_rows = 10_000

trials = np.random.random((n_rows,n_cols))
odds_ds = trials < p_ds
# When we sum an array of boolean values, numpy will treat True as 1 and False as 0. odds_ds.sum(axis=1)

p_dsis2 = (odds_ds.sum(axis=1) == 2).mean()



# 4. Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. 
# If on monday the machine is restocked with 17 poptart packages, 
# how likely is it that I will be able to buy some poptarts on Friday afternoon?
avg = 3
std= 1.5
 
consumed = np.random.normal(avg, std, size=(10_000, 5))
pops_bought = consumed.sum(axis =1)
pop_left = 17 - pops_bought
(pop_left >= 1).mean()



# 5. Compare Heights

#   Men have an average height of 178 cm and standard deviation of 8cm.
#   Women have a mean of 170, sd = 6cm.
#   If a man and woman are chosen at random, P(woman taller than man)?


men = np.random.normal(178, 8, size=(10_000, 1))
women = np.random.normal(170, 6, size=(10_000, 1))

w_taller = women > men
prob_w_taller = w_taller.mean()

# 6.When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails.
#  What are the odds that after having 50 students download anaconda, no one has an installation issue?
#  100 students?

probability = 1/250
n_students = n_cols = 50
n_simulations = n_rows = 10_000

trial = np.random.random((n_rows,n_cols))
corrup=  trial < probability
no_issu = (corrup.sum(axis=1) == 0).mean()
#  What is the probability that we observe an installation issue within the first 150 students that download anaconda?

# How likely is it that 450 students all download anaconda without an issue?

# 7. There's a 70% chance on any given day that there will be at least one food truck at Travis Park. 
# However, you haven't seen a food truck there in 3 days. How unlikely is this?
chance = .70
n_days = n_cols = 3
n_sim_ft = n_rows = 10**6

trials = np.random.random((n_rows,n_cols))

food_truck = trials < chance
no_ft = (food_truck.sum(axis=1) == 0).mean()


# How likely is it that a food truck will show up sometime this week?
n_days = n_cols = 2 #it represents the las 2 days
trials = np.random.random((n_rows,n_cols))
food_truck = trials < chance
some_ft= (food_truck.sum(axis=1) > 0).mean()

# 8. If 23 people are in the same room, what are the odds that two of them share a birthday?
#  What if it's 20 people? 40?