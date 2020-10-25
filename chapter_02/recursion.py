list_re = []

def recursion_list(ls):
    for i in ls:
        if isinstance(i,list):
            recursion_list(i)
        else:
            list_re.append(i)

if __name__ == '__main__':
    ls_1 = [1,2,3,4,[5,[6,7],8],9]
    recursion_list(ls_1)
    print(list_re)