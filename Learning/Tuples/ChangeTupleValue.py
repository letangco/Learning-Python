thistuples = ("apple", "banana", "cherry", "apple", "cherry")

y = list(thistuples)

y[1] = "watermelon"

y.append([1, 4, 5])
y.remove("apple")

thistuples = tuple(y)

print(thistuples)