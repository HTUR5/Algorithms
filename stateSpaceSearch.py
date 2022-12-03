from typing import List
from queue import Queue


def stateSpaceSearch(items: List):
    count = 0
    qq = Queue()
    qq.put((0, 0, 0))
    while qq.empty() is False:
        curr = qq.get()
        if curr[0] != len(items):
            qq.put((curr[0] + 1, curr[1] + items[curr[0]], curr[2]))
            qq.put((curr[0] + 1, curr[1], curr[2] + items[curr[0]]))
        count = count + 1
        print(curr)
    print(count)


def stateSpaceSearchPruning(items: List):
    count = 0
    qq = Queue()
    stock = []
    qq.put((0, 0, 0, -1))
    while qq.empty() is False:
        curr = qq.get()
        if curr[0] != len(items):
            saw = False
            for element in stock:
                if element[1] == curr[1] + items[curr[0]] and element[2] == curr[2]:
                    saw = True
            if saw is False:
                qq.put((curr[0] + 1, curr[1] + items[curr[0]], curr[2], -1))
                stock.append((curr[0] + 1, curr[1] + items[curr[0]], curr[2]))
            else:
                qq.put((curr[0] + 1, curr[1] + items[curr[0]], curr[2], -2))
            saw = False
            for element in stock:
                if element[1] == curr[1] and element[2] == curr[2] + items[curr[0]]:
                    saw = True
            if saw is False:
                qq.put((curr[0] + 1, curr[1], curr[2] + items[curr[0]], -1))
                stock.append((curr[0] + 1, curr[1], curr[2] + items[curr[0]]))
            else:
                stock.append((curr[0] + 1, curr[1], curr[2] + items[curr[0]], -2))
        if curr[3] == -1:
            count = count + 1
            print(curr)
    print(count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stateSpaceSearch([10, 20, 30, 40])
    print("/////////////")
    stateSpaceSearchPruning([10, 20, 30, 40])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
