
def cartesian_product(X, Y):
# provide your code here
# find each combination for the two sets
    length1 =len(X)
    length2 =len(Y)
    def product(X,Y, index1,index2):
        if index1==length1:
            return()
        elif index2 == length2:
            return product(X,Y,index1 +1 ,0)
        else:
            return((X[index1],Y[index2]),)+ product(X,Y,index1,index2 +1)
            #if you want  1a and a1 ect... then add ((Y[index2],X[index1]),) to the return statement
    return product(X,Y,0,0)



X = [1, 2]
Y = ['a', 'b', 'c', 'd']

print cartesian_product(X, Y)

print ("-------------------------")


def power_set(X):
# provide your code here
    if X:
        rest= power_set(X[1:])
        return rest + [[X[0]]+ x for x in rest]
    return [[]]

print power_set(Y)


#    for i in X:
#        for j in Y:
#           print(i,j)

#    [y+x for y in Y for x in X]
