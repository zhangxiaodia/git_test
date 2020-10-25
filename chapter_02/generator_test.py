L = [[1, 2],[3, 4],[5,6,[7,8]]]
def flat(L):
    for sublist in L:
        for i in sublist:
            yield i

print(dir(flat(L)))
print(type(flat(L)))
print(next(flat(L)))
print(next(flat(L)))
a = flat(L)
print(type(a))
print(next(a))
print(next(a))
print("使用for循环")
for num in flat(L):
    print(num)