import os

def test():
    print(os.getcwd())
    print(os.listdir())
    print(os.walk('/Users/admin/git_test/chapter_02'))
    w = os.walk('/Users/admin/git_test/chapter_02')
    # for cur_dir,child_dir,file in w:
    #     for i in file:
    #         print(cur_dir+'/'+i)
    for i in w:
        print(i)


#    print(os.mkdir('test'))
#    print(os.rmdir("/Users/admin/PycharmProjects/test_demi/test/test"))
#    os.rename('/Users/admin/git_test/chapter_02/pickle_data.txt','pickle_data.py')
#    os.remove('/Users/admin/git_test/chapter_02/pickle_data.txt')
if __name__ == '__main__':
    test()