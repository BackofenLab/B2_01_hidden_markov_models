<img src="./figures/banner.png" alt="UniFreiburg Banner"/>

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 2
###### SS 2022
##### Exercise sheet 1: Hidden Markov models
---

### _Exercise 1 - Two kinds of dice_ <img src="./figures/decorative_die.svg" alt="die" width="5%"/>

A casino uses two kinds of dice: 98% of dice are fair and 2% are loaded. The loaded die has a probability of 0.5 to show number six and probability 0.1 for the numbers one to five.

**a)** When we pick up a die from a table at random, what is the probability of rolling a six?

<details>
  <summary>Formulae: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_1_e1a.svg" alt="1a-formula" width="90%"/>
</p>
</details>

<details>
  <summary>Calculation Method: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_2_e1a.svg" alt="1a-formula" width="90%"/>
</p>
</details>

<details>
  <summary>Solution: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_3_e1a.svg" alt="1a-formula" width="90%"/>
</p>
</details>

**b)** We pick up a die from a table at random and roll [6, 6, 6]. What is the probability, that the die is loaded?
<details>
  <summary>Formulae: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_1_e1b.svg" alt="1a-formula" width="90%"/>
</p>
</details>

<details>
  <summary>Calculation Method: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_2_e1b.svg" alt="1a-formula" width="90%"/>
</p>
</details>

<details>
  <summary>Solution: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_3_e1b.svg" alt="1a-formula" width="90%"/>
</p>
</details>

**c)** How many sixes in a row would we need to roll to be at least 90% sure that the die is loaded?
<details>
  <summary>Formulae: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_1_e1c.svg" alt="1a-formula" width="90%"/>
</p>
</details>

<details>
  <summary>Calculation Method: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_2_e1c.svg" alt="1a-formula" width="90%"/>
</p>
</details>

<details>
  <summary>Solution: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_3_e1c.svg" alt="1a-formula" width="90%"/>
</p>
</details>

### _Exercise 2 - The occasionally cheating casino_ <img src="./figures/loaded_die.svg" alt="l_die" width="5%"/>

In a casino they use a fair die most of the time, but occasionally they switch to a loaded die. The loaded die has a probability 0.5 to show number six and probability 0.1 for the numbers one to five. Assume that the casino switches from a fair to a loaded die with probability 0.05 before each roll, and that the probability of switching back is 0.1. The probability to start a game with the fair die is 0.9.

**a)** Build the correct HMM graph. Match the letters from the blank figure to the numbers of the correct parts in the parts lists!

<p align="center">
<img src="./figures/sheet01-exercise2-a-HMM-intro.svg" alt="HMM" width=100%"/>
</p>

<details>
  <summary>Part List: A </summary>
<p align="center">
<img src="./figures/sheet01-exercise2-a-HMM-A.svg" alt="Parts-A" width="100%"/>
</p>
</details>

<details>
  <summary>Part List: B </summary>
<p align="center">
<img src="./figures/sheet01-exercise2-a-HMM-B.svg" alt="Parts-B" width="100%"/>
</p>
</details>

<details>
  <summary>Part List: C </summary>
<p align="center">
<img src="./figures/sheet01-exercise2-a-HMM-C.svg" alt="Parts-C" width="100%"/>
</p>
</details>

<details>
  <summary>Part List: D </summary>
<p align="center">
<img src="./figures/sheet01-exercise2-a-HMM-D.svg" alt="Parts-D" width="100%"/>
</p>
</details>

<details>
  <summary>Part List: E </summary>
<p align="center">
<img src="./figures/sheet01-exercise2-a-HMM-E.svg" alt="Parts-E" width="100%"/>
</p>
</details>

<details>
  <summary>Part List: F </summary>
<p align="center">
<img src="./figures/sheet01-exercise2-a-HMM-F.svg" alt="Parts-F" width="100%"/>
</p>
</details>

<details>
  <summary>Part List: G </summary>
<p align="center">
<img src="./figures/sheet01-exercise2-a-HMM-G.svg" alt="Parts-G" width="100%"/>
</p>
</details>

<details>
  <summary> Solution (Spoiler) </summary>
<p align="center">
<img src="./figures/sheet01-exercise2-a-HMM-solution.svg" alt="HMM-solution" width="100%"/>
</p>
</details>

**b)** Given an observed sequence of outcomes O = 3661634 and two possible state sequences p<sub>1</sub> = LLLFFFF and p<sub>2</sub> = FFFFFFF (where F=fair and L=loaded), what are the joint probabilites Pr(O,p<sub>1</sub>) and Pr(O,p<sub>2</sub>) in the HMM described above?
<details>
  <summary>Formulae: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_1_e2b.svg" alt="1a-formula" width="90%"/>
</p>
</details>

<details>
  <summary>Calculation Method: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_2_e2b.svg" alt="1a-formula" width="90%"/>
</p>
</details>

<details>
  <summary>Solution: (Spoiler)</summary>
<p align="center">
<img src="./figures/solution_3_e2b.svg" alt="1a-formula" width="90%"/>
</p>
</details>

**c)** Give an observation O = 1662, how many possible state sequences exist in the described HMM?
<details>
  <summary>Calculation Method: (Spoiler)</summary>
The actual observation does not matter in this case because all emission probabilities are > 0.
Thus there are 2⁴ possible state sequences
</details>

<details>
  <summary> Solution (Spoiler) </summary>
16 possible state sequences
</details>


### _Exercise 3 - Programming Assignment_
