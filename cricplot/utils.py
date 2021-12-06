__all__ = ['rand_jitter']


def rand_jitter(co_ord_1,co_ord_2,jitter = 0.3):
    '''
    add jitter for scatter points overlap
    
    co_ord_1 : list to check for overlapping (dimension 1)
    co_ord_2 : list which can be manipulated (dimension 2)
    jitter : jitter amount to add
    
    returns list containing modified co_ord2
    '''
    if len(co_ord_1)!= len(co_ord_2):
        raise Exception("Length of x and y are not equal!!!")
    if len(co_ord_1) == 0:
        raise Exception("Empty list passed")

    
    mod_co_ord = [None]*len(co_ord_2)
    
    mod_co_ord[0] = co_ord_2[0]
    
    for i in range(1,len(co_ord_1)):
        if co_ord_1[i] == co_ord_1[i-1] and co_ord_2[i] == co_ord_2[i-1]:
            mod_co_ord[i] = mod_co_ord[i-1] + jitter
        else:
            mod_co_ord[i] = co_ord_2[i]
    
    return mod_co_ord   