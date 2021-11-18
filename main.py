print("HelloPython")
if 5 > 2:
    print("Five is greater than two!")
txt = "The best things in life are free!"
print("free" in txt)

b = "Hello, World!"
print(b[2:5])

b = "Hello, 54321"
print(b[-12:])
a = "Hello, World!"
print(a.split(","))


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print(bool("Hello"))
print(bool(15))


mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:-4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
print(5,44,"\t",44)