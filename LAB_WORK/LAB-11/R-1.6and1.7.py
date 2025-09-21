if __name__=="__main__":
    
    #r-1.6
    #traditional
    def odd(n):
        c=0
        sum=0
        while c<n:
            if c%2!=0:
                sum=c**2+sum
            c+=1
        return sum
    
    print (odd(4))    
    
    # pythonic 
    
    def odd(n):
        sum=0
        for i in range(1,n):
            if i%2!=0:
                sum+=i**2
                
        return sum
            
    print(odd(4))     
    
    #r-1.7
    
    def odd(n):
        return sum(i**2 for i in range(1,n) if i%2!=0)
    
    print (odd(4))
            
            