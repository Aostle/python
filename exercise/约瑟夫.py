li  = list(range(1,31))
count  = 0

while count <15:
    
    print("{}号下船".format(li[8]))
    li = li[9:]+li[:8]
    count+=1

