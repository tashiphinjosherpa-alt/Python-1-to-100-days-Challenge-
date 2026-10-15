countries=("Spain","Nepal","Italy","Inddia","England")
temp= list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)