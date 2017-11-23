def wrapper(f):
    def fun(l):
        # complete the function
        l = [str(x) for x in l]
        for i in range(len(l)):
            if len(l[i]) == 10:                
                l[i] = '+91' + l[i]
            elif len(l[i]) == 11:
                l[i] = l[i][1:]
                l[i] = '+91' + l[i]
            elif len(l[i]) == 12:                
                l[i] = '+' + l[i]
            l[i] = l[i][:3] + ' ' + l[i][3:8] + ' ' + l[i][8:]
        return l           
    return fun
