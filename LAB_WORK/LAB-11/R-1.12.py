from random import randrange
if __name__ == "__main__":
    def my_chice(data):
        if not data:
            raise IndexError("sequence must not be empty")
        index=randrange(len(data))
        return data[index]


items = ["apple", "banana", "cherry", "date", "mango"]


    # Run multiple times to see randomness
for i in range(5):

    print(my_chice(items))