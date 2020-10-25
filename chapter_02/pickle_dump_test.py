import pickle

def pickle_dump(object_p):
    file_name = '/Users/admin/git_test/chapter_02/pickle_data.txt'
    with open(file_name, 'wb') as f:
        pickle.dump(object_p, f)

def pickle_load():
    file_name = '/Users/admin/git_test/chapter_02/pickle_data.txt'
    with open(file_name, 'rb') as f:
        return pickle.load(f)

if __name__ == '__main__':
    object_p = 'demi'
    pl = pickle_dump(object_p)
    pl = pickle_load()
    print(pl)