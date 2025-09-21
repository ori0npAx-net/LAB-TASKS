
#R-1.8
if __name__=="__main__":
    def equivalent(s):
        n=len(s)
        for k in range(-n,0):
            j=n+k
            if s[k]==s[j]:
                print(f"s[{k}]=s[{j}]={s[k]}")
                
                
obj=[1,9,4,6,7,32]
print(equivalent(obj))


#R-1.9

r=range(50,81,10)
print (list(r))

#R-1.10
r=range(8,-9,-2)
print(list(r))


#R-1.11
list=[2**i for i in range(0,9)]
print(list)