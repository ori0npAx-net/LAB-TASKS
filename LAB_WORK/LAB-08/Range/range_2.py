#using book logic 

class Range:
    def __init__(self,start,end=None,step=1):
        if step==0:
            raise ValueError("step cannot be zero")
        
        if end is None:
            start,end=0,start
            
        self._length=max(0,(end - start + step - 1)//step)
        self._start=start 
        self._step=step
        
    def __len__(self):
        return self._length
    
    def __getitem__(self,k):        #this function allows if we access an element through index by writing r[i]
        if k<0:                     #agar index negative mein ho tou ussey positve mein convert karta hai
            k+=len(self)        #negative indexing handle karta hai
            
        if not 0<=k<self._length:                   
            raise IndexError("INDEX OUT OF RANGE")  #agar range index se bahar ja rahi ho then INDEXERROR
        
        return self._start+k*self._step             #if not then it calculats the element 
    
    def __str__(self):
        return f"Range({self._length}, length={self._length}, step={self._step})"
    
    
if __name__ == "__main__":
    #r1=Range(1,10,0)
    r2=Range(30)
    r3=Range(2,45,3)
    
    getter=r3.__getitem__(3)
    
    print(len(r2))
    print(getter)
    
    #print(r1)
    print(r2)
    print(r3)
    