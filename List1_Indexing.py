marks=[99,88,56,42,47,59,"Tashi",True]
print(marks)


print(marks[2])
print(marks[-3])
print(marks[len(marks)-3])


if "Tashi" in marks:
    print("yes")
else:
    print("no")


if "as" in "Tashi": #variable create of Tashi by using ",.,,,"
    print("yes")    

print(marks[1:-1])    
print(marks[1:4])
print(marks[1:8:2])