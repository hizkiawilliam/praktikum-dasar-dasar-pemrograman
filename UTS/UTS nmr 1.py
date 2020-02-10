def k_sum_pair(alist,x):
    blist = []
    for i in alist:
        for j in alist:
            if(i+j==x):
                blist.append((i,j))
    blist.sort()
    return blist
