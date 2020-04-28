counter = 0
total = 0
number = 0
while number >= 0 :
    number = int(input("Enter a Positive Number \ a Negative to exit : "))
    total += number
    counter +=1
average = total/counter
print(counter)
print(total)
print(number)
print(average)
