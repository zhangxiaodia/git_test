import os

file_sizes = {}
def file_size(dir_file):

    if os.path.isfile(dir_file):
        size = os.path.getsize(dir_file)
        file_sizes[dir_file] = size
    else:
        for dir_i in os.listdir(dir_file):
            file_size(dir_file+'/'+dir_i)

def big_size(size):
    number = -1
    for key, value in size.items():
#       print("字典表内容:{} {}".format(key,value))
        if value > number:
            number = value
            file = key
    return file, number


if __name__ == '__main__':

    dir_test = '/Users/admin/git_test/chapter_02'
    file_size(dir_test)
    big_number = big_size(file_sizes)
    print(big_number)