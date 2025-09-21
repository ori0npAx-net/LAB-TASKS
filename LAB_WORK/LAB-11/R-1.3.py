
if __name__=="__main__":
    
    def minmax(data):
        data=list(data)
        data.sort()
        return (data[0],data[-1])
    
    
    seq=(34,78,12,10,56)
    print(minmax(seq))
    
    

