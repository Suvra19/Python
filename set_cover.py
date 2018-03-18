def set_cover(dict):
    U = dict['U'];
    S = dict['S'];
    covered = set();
    cover = [];
    while covered != U:
        print(covered)
        subset = max(S, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset
    return cover

if __name__ == "__main__":
    ''' dict = {'U': {1,2,3,4,5}, 'S': [{1,2,3}, {2,3,4}, {3,4,5}]}; '''
    ''' dict = {'U': {1,2,3,4,5}, 'S': [{2,3,4}, {1,2,3}, {3,4,5}]}; '''
    ''' dict = {'U': {1,2,3,4,5}, 'S': [{1,3}, {2,4}, {1,4}, {2,5}]}; '''
    dict = {'U': {1,2,3,4,5}, 'S': [{1,3}, {2,3}, {1,4}, {1,5}]}
    ''' dict = {'U': {1,2,3,4,5}, 'S': [{2,3}, {1,4}, {1,5}, {1,3}]} '''
    print(set_cover(dict));
    