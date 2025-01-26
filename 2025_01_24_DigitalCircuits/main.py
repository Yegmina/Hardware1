import itertools

def exercise1_1f():
    # 1.1 ex week 2, F
    symbols = ["=="]
    for symbol in symbols:
        for i, ii in itertools.product(range(0, 2), repeat=2):
            line = str(str(i) + symbol + str(ii))
            result = int(eval(line))
            print(line, result)

def exercise1_1g():
    # 1.1 ex week 2, g
    symbols = ["&"]
    for symbol in symbols:
        for i, ii in itertools.product(range(0, 2), repeat=2):
            line = str("(not (" + str(i) + "))" + symbol + "(not (" + str(ii) + "))")
            result = int(eval(line))
            print(line, result)

if __name__ == "__main__":
    exercise1_1f()
    exercise1_1g()
