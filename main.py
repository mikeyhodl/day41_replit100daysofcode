# myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

# for i in myDictionary:
#   print(myDictionary[i])


# myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

# for value in myDictionary.values():
#   print(value)


# myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

# for name,value in myDictionary.items():
#   print(f"{name}:{value}")


# myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

# for name,value in myDictionary.items():
#   print(f"{name}:{value}")

#   if (name == "strength"):
#     print("Whoa, SO STRONG!")


# myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 105, "equipped":"l33t haxx0r p0werz"}

# for name,value in myDictionary.items():
#   print(f"{name}:{value}")

#   if (name == "strength"):
#     if value > 100:
#       print("Whoa, SO STRONG")
#     else:
#       print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")



# myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

# for name,value in myDictionary.items():
#   print(f"{name}:{value}")


# myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 104, "equipped":"l33t haxx0r p0werz"}

# for name,value in myDictionary.items():
#   print(f"{name}:{value}")

#   if (name == "strength"):
#     if value > 100:
#       print("Whoa, SO STRONG")
#     else:
#       print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")



website = {"name": None, "url": None, "desc": None, "rating": None}

for name, value in website.items():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")