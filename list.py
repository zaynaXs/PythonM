letters = ["a", "b", "c", "d"]
#letters.append("e")
#letters.insert(1, "o")
#letters.pop()
#letters.pop(1)
#letters.remove("c")
#del letters[1:2]
#letters.clear()

#if "d" in letters:
#    print(letters.index("d"))
#print(letters)
#for index, letters in enumerate(letters):
#    print(index, letters)

matrix = [[0, 1], [2, 3]]
zeros = [0] * 100
numbers = list(range(20))
chars = list("Hello World")
#print(numbers[::-1])

#Unpacking list
num = [1, 2, 3, 4, 4, 4, 4, 5]
first, *other, last = num
#print(first, last)
#print(other)