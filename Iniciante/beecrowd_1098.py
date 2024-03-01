i = 0
j = 1

while i <= 2.0:
    j = 1
    while j < 4:
        if (round(i,1) == 1.0):
            print("I=" + str(int(i)) + " J=" + str(int(j + i)))

        elif (round(i,1) == 2.0):
            print("I=" + str(int(i+0.2)) + " J=" + str(int(j + i))) 
        else:
            print("I=" + str(round(i,1)) + " J=" + str(round((j + i), 1)))

        j += 1
    i += 0.2