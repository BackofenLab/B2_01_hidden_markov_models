<img src="./figures/banner.png" alt="UniFreiburg Banner"/>

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 2
###### SS 2022
##### Exercise sheet 1: Hidden Markov models
---

### _Exercise 3 - Programming Assignment_
In this exercise you will be working with dice: namely probabilities of different rolls, observations, state sequences, etc.
In order to make your experience better we implemented a Die class for you.

You can create a die by simply providing the probabilities of the corresponding edges.
For example:
```
fair_die = Die(1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
loaded_die = Die(0.1, 0.1, 0.1, 0.1, 0.1, 0.5)
```

You can access the value of the desired edge with two ways.

We prefer to start counting from zero so the probability of the first edge can be accessed by its index (which is 0) like:
```
fair_die[0]
```
Alternatively the value on the first edge is 1, so the edge probability can be accessed by the "name" of the edge and in this case we use the string value "1":
```
fair_die["1"]
```
We recommend sticking to the second way while solving the exercise.

Whenever we work with the set of dice we will define this set as a list of tuples. Each tuple consists a pair: a die and the corresponding probability of picking the die.
For example:
```
fair_die = Die(1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
loaded_die = Die(0.1, 0.1, 0.1, 0.1, 0.1, 0.5)

casino_dice = [(fair_die, 0.98), (loaded_die, 0.02)]
```

<img src="./figures/sheet01-exercise3-intro.svg" alt="intro" width="70%"/>

**a)** Implement the function `roll_proba_given_dice` which takes a `list of dice` and a `roll` value and returns the `probability of the roll`. A roll is a single value which can be obtained by throwing a die once.

<details>
  <summary>Example: (Spoiler)</summary>

  ```
   >>> fair_die = Die(1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
   >>> loaded_die = Die(1/10, 1/10, 1/10, 1/10, 1/10, 1/2)
   >>> roll_proba_given_dice([(fair_die, 0.1), (loaded_die, 0.9)], "6")
  0.4666666666666667
  ```

</details>

**b)** Implement the function `observation_given_die` which takes a `list of dice` and an `observation` and returns the `probability of the observation`.

<details>
  <summary>Example: (Spoiler)</summary>

</details>

**c)** Implement the function `proba_of_dice_given_observation` which takes a `list of dice` and an `observation` and returns the `probability for each die` to be used to have the corresponding outcome.

<details>
  <summary>Example: (Spoiler)</summary>

</details>

**d)** Implement the function `state_sequence_probability_computation` which takes a `list of dice`, a `state sequence` and the corresponding `transition matrix` for the given dice and returns the `probability of the state sequence`.

<details>
  <summary>Example: (Spoiler)</summary>

</details>

**e)** Implement the function `observation_probability_computation_given_state_sequence` which takes a `list of dice`, an `observation` and a `state sequence` and returns the `probability of the given observation`.

<details>
  <summary>Example: (Spoiler)</summary>

</details>

**f)** Implement the function `observation_state_sequence_joint_probability_computation` which takes a `list of dice`, an `observation`, a `state sequence` and a `transition matrix` and return the joint probability of the observation and the state sequence.

<details>
  <summary>Example: (Spoiler)</summary>

</details>