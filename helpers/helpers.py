from math import isclose


class Die:
    def __init__(self, *args):
        self.edge_probabilities = args
        if not args:
            raise ValueError("Die must have at least one edge!")
        if not isclose(sum(args), 1, abs_tol=0.01):
            raise ValueError("Edge probabilities must sum up to 1!")
        self.dict_edge_probabilities = {str(key): value for key, value in enumerate(args, 1)}

    def __repr__(self):
        return f"Die: {self.dict_edge_probabilities}"

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, item):
        if isinstance(item, int):
            if item < len(self.edge_probabilities):
                return self.edge_probabilities[item]
            else:
                return 0
        if isinstance(item, str):
            if item in self.dict_edge_probabilities:
                return self.dict_edge_probabilities[item]
            else:
                return 0

    @property
    def fair(self):
        return all([isclose(x, self.edge_probabilities[0]) for x in self.edge_probabilities])


def roll_proba_given_dice_correct(list_dice, roll_value):
    roll_proba = 0
    for die, die_proba in list_dice:
        roll_proba += die[str(roll_value)] * die_proba
    return roll_proba


def observation_given_die_correct(die, observation):
    observation_proba = 1
    for roll in observation:
        observation_proba *= die[str(roll)]
    return observation_proba


def proba_of_dice_given_observation_correct(list_dice, observation):
    list_observations_proba = [observation_given_die_correct(pair[0], observation) for pair in list_dice]
    denominator = sum([op * pair[1] for op, pair in zip(list_observations_proba, list_dice)])
    if denominator == 0:
        return [0] * len(list_dice)
    else:
        list_dice_proba = [(op * pair[1]) / denominator for op, pair in zip(list_observations_proba, list_dice)]
        return list_dice_proba


def path_probability_computation_correct(list_dice, path, transition_matrix):
    path_probability = list_dice[int(path[0])][1]
    for node1, node2 in zip(path, path[1:]):
        node1, node2 = int(node1), int(node2)
        trans_proba = transition_matrix[node1][node2]
        path_probability *= trans_proba
    return path_probability


def observation_probability_computation_given_path_correct(list_dice, observation, path):
    observation_probability = 1
    for roll, node in zip(observation, path):
        die = list_dice[int(node)][0]
        roll_proba = die[str(roll)]
        observation_probability *= roll_proba

    return observation_probability


def observation_path_joint_probability_computation_correct(list_dice, observation, path):
    path_proba = path_probability_computation_correct(list_dice, observation, path)
    obserbation_proba = observation_probability_computation_given_path_correct(list_dice, observation, path)
    return path_proba * obserbation_proba


def main():
    die = Die(0.3, 0.7, 0.0)
    print(die)
    print(die.fair)
    print(die["1"])
    print(die[0])
    print(observation_given_die_correct(die, [1, 1, 1, 2]))

    fair_die = Die(1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
    loaded_die = Die(0.1, 0.1, 0.1, 0.1, 0.1, 0.5)
    casino_dice = [(fair_die, 0.98), (loaded_die, 0.02)]
    print(roll_proba_given_dice_correct(casino_dice, 6))
    print(proba_of_dice_given_observation_correct(casino_dice, [6, 6, 6]))
    print(proba_of_dice_given_observation_correct(casino_dice, [6, 6, 6, 6, 6, 6]))

    casino_dice = [(fair_die, 0.9), (loaded_die, 0.1)]
    transition_casino = [[0.95, 0.05], [0.1, 0.9]]
    path = "1110000"
    path_proba = path_probability_computation_correct(casino_dice, path, transition_casino)
    print(path_proba)

    observation = "3661634"
    observation_proba = observation_probability_computation_given_path_correct(casino_dice, observation, path)
    print(observation_proba)


if __name__ == "__main__":
    main()
