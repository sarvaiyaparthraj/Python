

fruits = ["Cherry,Coconut,Pomegranate,Orange"]



fruits.append("blue berry")


print("appending OP",fruits)
  

fruits.insert(2,"Currant")

print("adding specific position",fruits)


fruits.extend(["Guava,"," lychee"])

print("adding multiple elements",fruits)

fruits.pop()
print("removing last element",fruits)

fruits.pop(2)
print("removing element at specific possition",fruits)


fruits.remove("blue berry")
print("removing specific element using value",fruits)

del fruits[0]

print("deleting first element in list",fruits)

fruits[0] = "Guava"
print("updeting first element",fruits)



number = [5,8,4,6,9,1,1,1,1,]
print("sorted number",number)


number.sort()

print("sorted number",number)


number.sort(reverse=True)
print("number in descending order",number)


print("counting value",number.count(1))


print("index",number.index(1))
