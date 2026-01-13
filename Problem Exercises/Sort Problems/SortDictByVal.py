#Sort dictionary by value.
data = {"a": 3, "b": 1, "c": 2}
sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_dict)  # {'b': 1, 'c': 2, 'a': 3}
