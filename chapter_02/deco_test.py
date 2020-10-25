def deco(func):
    def inner():
        func()
        print("inner function")
    return inner


def target():
    print("target function")
if __name__ == '__main__':
    target = deco(target)
    target()