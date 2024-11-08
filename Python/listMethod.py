number = [5,4,6,6,7,8,9,5]
number.insert(1,18)
print(number)

number.pop()
print(number)
print(number.index(18))

print(number.count(6))
number.sort()
print(number)


# remove duplicate number from list

numbers = [2,2,4,6,3,4,6,1]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
unique.sort()
print(unique)        