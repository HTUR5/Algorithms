from typing import List
from queue import Queue


# we use the first part. we pass all the m items. if there is more than n-1 shared items - there is circle

def checkCircles(items: List):
    shared_items = [False for i in range(len(items[0]))]
    count = 0
    for player in items:
        for item in range(len(player)):
            if 0 < player[item] < 1:
                if shared_items[item] is False:
                    shared_items[item] = True
                    count = count + 1
    if count >= len(items):
        return True
    return False


# actualy if there is less than n shared items the algorithm shuld return dont know.
# in this case we need to refer this as a graph and use dfs

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(bool(checkCircles([[1, 1, 0.07, 0], [0, 0, 0.93, 1]])))
    print(bool(checkCircles([[1, 0.4, 0.07, 0], [0, 0.6, 0.93, 1]])))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
