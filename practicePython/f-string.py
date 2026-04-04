# it use the string formeting

letter = "Hey my name is {1} and i am from {0}"
country = "India"
name = "Navaj"

print(letter.format(country, name))
print(f"hey my name is {name} and I am from {country}")

price = 235
txt = f"For only {price} dollars!"
print(txt)

print(f"{3 * 6}")