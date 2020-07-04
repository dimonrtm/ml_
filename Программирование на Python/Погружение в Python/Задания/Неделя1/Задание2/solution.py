import sys
shape_size=int(sys.argv[1])
for i in range(shape_size-1,-1,-1):
    if i==0:
        print("#"*shape_size)
    else:
        print(" "*i+"#"*(shape_size-i))