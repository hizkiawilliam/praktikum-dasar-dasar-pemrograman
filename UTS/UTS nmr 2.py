def find_modus(alist):
    blist = []
    for i in alist:
        blist.append([alist.count(i),i])
    blist.sort()
    return blist[-1][1]
