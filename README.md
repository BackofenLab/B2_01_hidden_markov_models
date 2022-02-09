<img src="./figures/banner.png" alt="UniFreiburg Banner"/>

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 2
###### SS 2021/2022
##### Exercise sheet 1: Hidden Markov models
---

### _Exercise 1 - Two kind of dice_

A casino uses two kinds of dice: 98% of dice are fair and 2% are loaded. The loadd die has a probability of 0.5 to show number six and probability 0.1 for the numbers one to five.

**a)** When we pick up a die from a table at random, what is the probability of rolling a six?

**b)** We pick up a die from a table at random and roll [6,6,6]. What is the probability, that the die is loaded?

**c)** How many sixes in a row would we need to roll to be at least 90% sure that the die is loaded?

### _Exercise 2 - The ocassionally dishonest casino_
In a casiono they use a fair die most of the time, but occasionally they switch to a loaded die. The loaded die has a probability 0.5 to sow number six and probability 0.1 for th numbers one to five. Assume that the casiono switches from a fair to a loaded die with probability 0.05 before each roll, and that the probability of switching back is 0.1. The probability to tart a game with the fair die is 0.9.

**a)** Which of the following graphical representations depicts the above given explanation?

**b)** Given an observed sequence of outcomes O = 3661634 and two possible state sequences p<sub>1</sub> = LLLFFFF and p<sub>2</sub> = FFFFFFF (where F=fair and L=loaded), what are the joint probabilites Pr(O,p<sub>1</sub>) and Pr(O,p<sub>2</sub>) in the HMM described above?

**c)** Give an observation O = 1662, how many possible state sequences exist in the described HMM?

### _Exercise 3 - Programming Assignment_
