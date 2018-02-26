# 1. Create a function for modular addition
def modAdd(x, y, m):
    # Provide your code here
    result =0
    result = (x + y) % m
    return result
    
print "7 + 9 (mod 11):\t\t\t", modAdd(7, 9, 11) # => 5
    

# 2. Create a function for modular multiplication
def modTimes(x, y, m):
    # Provide your code here
    result = (x *y) % m
    return result
    
print "7 * 9 (mod 11):\t\t\t", modTimes(7, 9, 11) # => 8
   
   
# 3. Create a function for converting binary to decimal. Binary numbers are represented as strings of 1 and 0        
def binToDec(n):
    # Provide your code here
    return int (n,2)
        
        
print  "1010000100 in decimal:\t\t", binToDec('1010000100') # => 644


# 4. Create a function for converting decimal to binary. Binary numbers are represented as strings of 1 and 0
def decToBin(n):
    # Provide your code here
    return int(bin(n)[2:])
    
    
print "644 in binary:\t\t\t", decToBin(644) # => 1010000100


# 5. Create a function for modular exponentiation. Your function should compute in a reasonable time for exponents on the order of 10 billion
def modExp(n, p, m):
    # Provide your code here
    y=1
    while p>0:
        if p%2 ==0:
            n=(n*n)%m
            p=p/2
        else:
            y=(n*y)%m
            p=p-1
    return y

print "3^644 (mod 645):\t\t", modExp(3, 644, 645) # => 36

print "3^9876543210 (mod 2017):\t", modExp(3, 9876543210, 2017) # => 1040


# 6. Write a function to determine the last digit of an integer represented as a base raised to an exponent.


def lastDigit(base, exponent):
    # Provide your code here
    if exponent == 0:
        return 1
    
    cycle = [base% 10]
    while True:
       nxt = (cycle[-1] * base) % 10
       if nxt == cycle[0]:
           break
       cycle.append(nxt)
    return cycle[(exponent - 1) % len(cycle)]

    # result = base * exponent
    # if result % 2 == 0:
    #    return result % 10
    # elif result % 2 != 0:
    #    return result % 10


print "Last digit of 7^56746365435748:\t", lastDigit(7, 56746365435748) # => 1

    
    
        
