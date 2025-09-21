if __name__=="__main__":
    # traditional
    
    def is_even(k):
        k=abs(k)
        current=0
        while current<k:
            current=current+2
            
        if current==k:       #return current ==k --> will also return a bool value cuz all equality operators return bool value 
            return True
        else:
            return False
      
    
    o=is_even(-10)
    print(o)        
        
    
    #pythonic
    
    def is_even(k):
        k=abs(k)
        for c in range(0,k+1,2):
            if c==k:
                return True
        return False
    print(is_even(-11))
    
    
    
    