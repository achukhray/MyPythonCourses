#The ATM dispenses the amount in the maximum possible bills
bills = [1000, 500, 200, 100, 50, 20, 10]
sum1 = int(input("sum: "))
if not(sum1%10):
    i = 0
    while (sum1 > 0):
        n = sum1//bills[i]
        if (n):
            print(bills[i], n)
            sum1 %= bills[i]
        i += 1
else: print("Impossible")