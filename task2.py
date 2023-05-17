#Перевірити, чи є введене число парним.
#Перевірити, чи є число не парним, ділиться чи на три і на п'ять одночасно, але так, щоб не ділитися на 10.
#Ввести число, вивести усі його дільники.
#Ввести число, вивести його розряди та їх множники.
numb=input()
n = int(numb)

#чи є введене число парним
if (n%2):
    print("Odd")
else:
    print("Even")

#чи є число не парним,
#ділиться чи на три і на п'ять одночасно,
#але так, щоб не ділитися на 10
if  (not(n%2) and not(n%3) and not(n%5) and (n%10)):
    print("Yes")
else:
    print("No")

#вивести усі його дільники
print("Fractors:")

for i in range(1,n//2+1):
    if (not(n%i)):
        print(i)



#вивести його розряди та їх множники
digits = len(numb)
print("Degrees:")
for i in range(1,digits+1):
    digit=n//pow(10,digits-i)
    print(digit,"*10^",digits-i,end="+")
    n=n%pow(10,digits-i)



