file = "/Users/admin/git_test/test_data/add_list.txt"
f = open(file)

for line in f.readlines():
    #print(line)
    info = line.split(",")
    print(info[0])
    print(info[1])
    print(info[2])
