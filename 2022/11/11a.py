class Monkey:
    items: list[int]
    operation: str
    divisible: int
    trueMonkey: int
    falseMonkey: int
    itemsInspected: int

    def __init__(self, items, operation, divisible, trueMonkey, falseMonkey):
        self.items = items
        self.operation = operation
        self.divisible = int(divisible)
        self.trueMonkey = int(trueMonkey)
        self.falseMonkey = int(falseMonkey)
        self.itemsInspected = 0

    def receive(self, item: int):
        self.items.append(item)

    def inspect(self, item: int):
        self.itemsInspected += 1
        calculation = self.operation.replace("old", str(item))
        item = eval(calculation)
        item = item % r
        if item % self.divisible == 0:
            monkeyList[self.trueMonkey].receive(item)
        else:
            monkeyList[self.falseMonkey].receive(item)

    def listItems(self):
        return ",".join(map(str, self.items))

    def monkeyRound(self):
        while len(self.items) > 0:
            itemToInspect = self.items[0]
            del(self.items[0])
            self.inspect(itemToInspect)


monkeyList = []

def readMonkey(input: str):
    input = input.split("\n")
    number = int(input[0][7])
    itemList = input[1].split(" ",4)[4].split(", ")
    operation = input[2].split(" ",5)[5]
    divisible =input[3].split(" ")[5]
    trueMonkey = input[4].split(" ")[9]
    falseMonkey = input[5].split(" ")[9]
    monkeyList.append(Monkey(itemList, operation, divisible, trueMonkey, falseMonkey))

with open("input.txt", "r") as f:
    monkeyInputs = f.read().split("\n\n")

for monkeyInput in monkeyInputs:
    readMonkey(monkeyInput)

divisibles = [monkey.divisible for monkey in monkeyList]
r = 1
for divisible in divisibles:
    r = r * divisible

for _ in range(10000):
    for monkey in monkeyList:
        monkey.monkeyRound()

listHighest = []
for monkey in monkeyList:
    listHighest.append(monkey.itemsInspected)
listHighest.sort()
print(listHighest[6] * listHighest[7])


