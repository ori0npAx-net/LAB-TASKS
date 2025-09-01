class Vector:
    def __init__(self,dimension):           #takes input, ke kitney ki list chahiye shows n-dimensions
        self._coords=[0]*dimension
    
    def __len__(self):
        return len(self._coords)
    
    def __setitem__(self,j,value):          #sets value ke jth index per konsi value honi chahiye
        self._coords[j] = value
    
    def __getitem__(self,j):                #gets the value at jth index
        return self._coords[j]
    
    def __add__(self,other):
        
        if len(self)!= len(other):
            raise ValueError('DIMENSIONS SHOULD BE EQUAL')
        
        
        result=Vector(len(self))            # aik new vector object bana jiski len len(self) ke barabar hai. agar self waley vector ka size 3 elements hai then uska result bhi 3 size ke empty vecto mein baneyga
        for j in range (len(self)):         #loop ka kaam hai har element ko iterate karna, har element per addition karna and result new vector (jo uper banaya hai) usmein store karna 
            result[j]=self[j]+other[j]
        return f"added vector is:{result}"
    
    def __eq__(self,other):
        return self._coords == other._coords
    
 #  def __ne__(self,other):
 #      return self._coords != other._coords  
    def __ne__(self,other):             
        return not self==other             #both not equals to work the second one relies on th __eq__ definition
    
    def __str__(self):                           
       return "<"+str(self._coords)[1:-1]+">"
    """
    str(self._coords) → list ko string banata hai
    [1:-1] → outer square brackets hatata hai      
    " < ... > " → apne desired format mein likh sakty hain
    """
    
    
    
if __name__=='__main__':
    vector1=Vector(3)
    vector2=Vector(3)
    
    vector1.__setitem__(0,1)
    vector1.__setitem__(1,2)
    vector1.__setitem__(2,3)
    vector2.__setitem__(0,5)
    vector2.__setitem__(1,4)
    vector2.__setitem__(2,4)
    print(vector1)
    print(vector2)
    print(vector1.__getitem__(1))
    print(vector2.__getitem__(0))
    
    vec=vector1.__add__(vector2)        #this line works -->using method/function directly
    d=vector1+vector2                 #this line works too operator just got overload
    print(vec,d)

    print(vector1==vector2)
    print( vector1!=vector2)
    
        