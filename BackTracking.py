from re import X


def permutaciones(list, s):
    if list == 1:
        return s
    else:
        return [
            y + x 
            for y in permutaciones(1, s)
            for x in permutaciones(list - 1,s)
        ]
print(permutaciones(1, ["a","b","c"]))
print(permutaciones(2, ["a","b","c"]))
print(permutaciones(3, ["a","b","c"]))
print(permutaciones(4, ["a","b","c"]))
