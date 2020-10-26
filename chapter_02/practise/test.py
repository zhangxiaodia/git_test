import os

def file_size(dir_file, number):

    if os.path.isfile(dir_file):
        size = os.path.getsize(dir_file)

        if size > number:
            number = size
            print("size的值是{}".format(size))
            print("number置换后的值{}".format(number))
        print("number{}".format(number))
        return number
    else:
        for dir_i in os.listdir(dir_file):
            file_size(dir_file+'/'+dir_i, number)

if __name__ == '__main__':

    dir_test = '/Users/admin/git_test/chapter_02'
    print(file_size(dir_test, -1))