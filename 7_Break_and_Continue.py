counter = 0
sum  = 0
while True :
    this_input = float(input(" Enter a Number ? "))
    if this_input < 0:
        if counter == 0:
            print("You Haven't entered any numbers yes!")
            continue
        break
    sum += this_input
    counter += 1
    print(counter ,': ',sum)
