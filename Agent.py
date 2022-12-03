from typing import List


class Agent:

    def __init__(self):
        self.values = dict()

    def value(self, option: int) -> float:
        return self.values[option]

    def set_value(self, option: int, value: float) -> float:
        self.values[option] = value


def isParetoImprovement(agents: List[Agent], option1: int, option2: int) -> bool:
    for agent in agents:
        if agent.value(option1) < agent.value(option2):
            return False
    return True


def isParetoOptimal(agents: List[Agent], option: int, allOptions: List[int]) -> bool:
    for opt in allOptions:
        if opt is not option:
            if isParetoImprovement(agents, opt, option) is True:
                return False
    return True


if __name__ == '__main__':
    Ami = Agent()
    Ami.set_value(1, 1)
    Ami.set_value(2, 2)
    Ami.set_value(3, 3)
    Ami.set_value(4, 4)
    Ami.set_value(5, 5)
    Tami = Agent()
    Tami.set_value(1, 3)
    Tami.set_value(2, 1)
    Tami.set_value(3, 2)
    Tami.set_value(4, 5)
    Tami.set_value(5, 4)
    Rami = Agent()
    Rami.set_value(1, 3)
    Rami.set_value(2, 5)
    Rami.set_value(3, 5)
    Rami.set_value(4, 1)
    Rami.set_value(5, 1)
    agentsList = [Ami, Tami, Rami]
    optionList = [1, 2, 3, 4, 5]
    print(bool(isParetoImprovement(agentsList, 4, 1)))
    print(bool(isParetoOptimal(agentsList, 4, optionList)))
