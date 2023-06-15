import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from math import sqrt
PATH = "./file.csv"
dataFrame = pd.read_csv(PATH)
dataFrame = dataFrame.drop(['Unnamed: 0'], axis=1)
dataFrame.head()
#Question 1: what is the probability of receiving an evaluation score greater than 3.5 and less than 4.2?
eval_mean = round(dataFrame['eval'].mean(), 3)
eval_sd = round(dataFrame['eval'].std(), 3)
P1 = scipy.stats.norm.cdf((3.5-eval_mean)/eval_sd)
P2=scipy.stats.norm.cdf((4.2-eval_mean)/eval_sd)
answer1= round(P2-P1,3)
print("answer to Question1 is :")
print(answer1)
#Question 2: what is the probability of receiving an evaluation score greater than 3.3?
P=scipy.stats.norm.cdf((3.3-eval_mean)/eval_sd)
answer2=round(1-P,3)
print("answer to Question2 is :")
print(answer2)
#Question 3: what is the probability of receiving an evaluation score between 2 and 3?
Px1=scipy.stats.norm.cdf((2-eval_mean)/eval_sd)
Px2=scipy.stats.norm.cdf((3-eval_mean)/eval_sd)
answer3=round(Px2-Px1,3)
print("answer to Question3 is :")
print(answer3)
#Question 4: To test the hypothesis that sleeping for at least 8 hours makes one smarter, 12 people
# who have slept for at least 8 hours every day for the past one year have their IQ tested.
data=[116,111,101,120,99,94,106,115,107,101,110,92]
mu=100
x_not=106
stdv=scipy.stats.tstd(data)
n=12
z=(sqrt(n)*(x_not-mu))/stdv
print("answer to Question4 is :")
print(z)
#Question 5: Consider a computer system with Poisson job-arrival stream at an average of 2 per minute.
# Determine the probability that in any one-minute interval there will be :
#part1) 0 jobs;
l1=2
t1=1
k1=0
lt1=l1*t1
f1=scipy.stats.poisson.pmf(k1,lt1)
answer5_1=round(f1,4)
print("the answer to first part is :")
print(answer5_1)
#part2) exactly 2 jobs;
l2=2
t2=1
k2=2
lt2=l2*t2
f2=scipy.stats.poisson.pmf(k2,lt2)
answer5_2=round(f2,4)
print("the answer to second part is :")
print(answer5_2)
#part3) at most 3 arrivals.
l3=2
t3=1
k3=3
lt3=l3*t3
f3=scipy.stats.poisson.cdf(k3,lt3)
answer5_3=round(f3,4)
print("the answer to third part is :")
print(answer5_3)
