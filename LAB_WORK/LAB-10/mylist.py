class List:
    def __init__(self, sequence):
        self._seq=sequence
        self._k=-1
        self._length=len(self._seq)
   
    def __setitem__(self,k,value):      #assigns  value to the index provided
        self._seq[k]=value
    
  
    def __getitem__(self,k):      #gets the item at the given index
        return self._seq[k]
        
  
    def __len__(self):          #provides length of the sequence
        return self._length
    
  
    def __delitem__(self,k):        #deleted item at the given index
        #del self._seq[k]            #using built in function
        self._seq = [self._seq[i] for i in range(len(self._seq)) if i !=k]      #uses list comprehension to delete item 
        self._length=len(self._seq)     #this makes a new list and does not add the item u want t delete
        return self._seq

    def __contains__(self,n):       #containment check
        for item in self._seq:
            if item == n:
                return True
        return False 
    
                 
    def __call__(self, value):   #object function ki tarhan nehave karey like obj(..) likhne per meri custome logic chl sakey
        self._seq.append(value)
        self._length=len(self._seq)
        return self._seq
    
  
    def __str__(self):      
        return str(self._seq)
    

    def __next__(self):     #provides next value in the sequence
        self._k+=1
        if self._k < len(self._seq):
            return self._k,self._seq[self._k]
        else:
            raise StopIteration()
        
  
    def __iter__(self):     #iteration
        return self
    
        
    def __reversed__(self):  #reverses the sequence
        for x in range(len(self._seq)-1,-1,-1):
            yield self._seq[x]
    
        
if __name__=="__main__":
    
    seq=[1,2,3,40]
    first=List(seq)
    
    first.__setitem__(1,50)
    first[2]=60
    print(first)
    print(list(first.__reversed__()))
    print(first.__len__())
    print(10 in first)  #this one works too (containment)
    print(first.__contains__(10))   #this one too (containment)
    print(first.__delitem__(3))
    print (first(100))
    
    for i in range(5):
        print(first)