name11 = input("Enter the first name: ")
name12 = input("Enter the partenr's name: ")
name1 = list(name11.lower().replace(" ", ""))
name2 = list(name12.lower().replace(" ", ""))
name1_copy = name1.copy()
name2_copy = name2.copy()

relationships = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
   
for i in name1_copy:
    
    if i in name2_copy:

        name1.remove(i)  
        name2.remove(i) 
unique_elements = name2+name1

count = len(unique_elements)

while len(relationships) > 1:
    index = count % len(relationships) -1
    if index >= 0:
        right = relationships[index + 1:]
        left = relationships[:index]
        relationships = right + left
    else:
        relationships = relationships[:len(relationships) - 1]

print(name11,'&',name12, "have", *relationships, "relationship")

relationships = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
