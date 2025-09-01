#my logic using list (basic understanding does not include len,getitem)

class Range:
    def __init__(self, start,end=None,step=1):
        self._start=start
        self._step=step 
        self._end=end
        self._list=[]
    
        if end is None:             #agar arg aik diya h tou start ko 0 and end ko start consider karlo
            self._start=0
            self._end=start
            
        if self._step == 0:       #if not self._step -->yeh none,0,'',false sabko false treat karega 
           raise ValueError('step cannotbe zero')
           
        current=self._start
        while current < self._end:
            self._list.append(current)              #list mein kuch likhney ke liyen use append
            current+=self._step
    def __str__(self):
        return str(self._list)
    
    
if __name__=="__main__":
    r=Range(5,9)
    print(r)