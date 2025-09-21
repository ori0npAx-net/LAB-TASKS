
if __name__=="__main__":
    
    
    #traditional
    def is_multiple(n,m):
        if n%m==0:
            return True
        else:
            return False
            
    print(is_multiple(159,5))
    
    #pythonic
    def is_multiple(n,m):
        return n%m==0
        
        
    print(is_multiple(10,2))
    
    
    
    even_sq=[2**i for i in range(0,9)]
    print (even_sq)