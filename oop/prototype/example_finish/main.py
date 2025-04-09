from tesla import Tesla

tesla1 = Tesla('Model S', 'White', 2020)
tesla2 = tesla1.clone()


print(tesla1.color)
print(tesla2.color)

tesla1.color = 'Red'

print(tesla1.color)
print(tesla2.color)
