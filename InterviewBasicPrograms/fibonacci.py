n = 10 #fibonacci of 1st 10 numbers
i = 0 #start number from 0
j = 1 #second number
k = j # sum of 1st and 2nd number
count = 1
while count <10:
    print(i) #print series from 0
    count += 1 #increment count
    i = j # start number increment
    j = k 
    k = i + j  # 2nd number will be sum of previous 2
