import os, os.path


def all_files(dir_file):
    if os.path.isfile(dir_file):
        print(os.path.basename(dir_file))
    else:
        for dir_i in os.listdir(dir_file):
            all_files(dir_file+'/'+dir_i)

if __name__ == '__main__':
    dir_test = '/Users/admin/git_test/chapter_02'
    all_files(dir_test)
