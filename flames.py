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

index = len(unique_elements) % len(relationships)
relationship = relationships[index]


print(name11,'&',name12, "have", relationship, "relationship")