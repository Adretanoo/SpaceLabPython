from circle import Circle

obj1 = Circle("Red", 10, 10)
obj2 = obj1.clone()
print(obj1.color)
print(obj2.color)

obj2.color = "Blue"

print(obj1.color)
print(obj2.color)