l1 = ["2", "4", "7", "4", "2", "1", "9"]
l2 = sorted(set(l1), key=l1.index)
print(l2)


test = {"key": "1", "le": "2"}
print(test.items())
print(sorted(test.items(), key=lambda x: x[0]))

print(test.keys())
print(test.values())
