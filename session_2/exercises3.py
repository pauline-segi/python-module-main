# foods = [
#     "orange",
#     "apple",
#     "banana",
#     "strawberry",
#     "grape",
#     "blueberry",
#     ["carrot","cauliflower","pumpkin"],
#     "passionfruit",
#     "mango",
#     "kiwifruit"]


# print(foods[0])       orange
# print(foods[2])       banana
# print(foods[-1])      kiwifruit
# print(foods[0:3])     ['orange', 'apple', 'banana']
# print(foods[7:11])    ['passionfruit', 'mango', 'kiwifruit']
# print(foods[6][-1])   pumpkin    


# song = "A little bit of"

# verse = [ 
# # ["A little bit of"],
# "Monica in my life",
# "Erica by my side",
# "Rita's all I need",
# "Tina's what I see",
# "Sandra in the sun",
# "Mary having fun",
# "Jessica here I am"
# ]


# print(song,verse[0])
# print(song,verse[1])
# print(song,verse[2])
# print(song,verse[3])
# print(song,verse[4])
# print(song,verse[5])
# print(song,verse[6])
# print("A little bit of you, makes me your man!")



# names = []

# name1 = input("Enter a name: ")
# name2 = input("Enter a second name: ")
# name3 = input("Enter a third name: ")

# print(name1)
# print(name2)
# print(name3)

# names.append(name1)
# names.append(name2)
# names.append(name3)




a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

d = [a, b, c]  # Assigning a list of lists to d

print(d)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

a.insert(0, b)  # Inserting list b at index 0 in list a
a.insert(2, c)  # Inserting list c at index 2 in list a

print(a)  # Output: [[4, 5, 6], 1, [7, 8, 9], 2, 3]
