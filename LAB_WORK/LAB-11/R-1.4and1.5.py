    #  R-1.4
    #  traditional
    
if __name__=="__main__":
    def positive(n):
        c=0
        sum=0
        while c<n:
            sum=(c*c)+sum
            c=c+1
        return sum
        
print(positive(4))

    #   pythonic 

def positive(n):
    i=0
    for val in range(n):
        i=(val**2)+i
        
    return i

print(positive(4))


# r-1.5
#using list comprehension

def sq_sum(n):
    return sum(i**2 for i in range(1,n))

print(sq_sum(4))