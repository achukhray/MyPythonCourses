# У банкоматі є по 10 купюр номіналів: 10,20,50,100,200,500,1000.
# # Банкомат видає дрібними купюрами, але не більше 10 штук кожної купюри.
#----------------------------------------------------------------
# 1a + 2b + 5c + 10d + 20e + 50f + 100g = S
#   Суму S вводити без останньої цифри 0


S = 165   #вводити суму від 1 до 1880

for a in (K:= list(range(10,-1,-1))):  
  for b in K:
     for c in K:
       x = a + b*2 + c*5
       for d in K:
         for e in K:
           y = x + d*10 + e*20  
           for f in K:
            z = y + f*50  
            for g in K:
              if (r:= S - g*100) >= 0:  
                if r == z:
                   print(L:=[a,b,c,d,e,f,g], sum(L),'\n')
                   bills = 10,20,50,100,200,500,1000
                   for i,j in zip (L, bills):
                       print(f"{j:10} x {i:2}")
                   print('===> ', S*10)    
                   exit()
               


# a,b,c,d,e,f,g - параметри циклів
# K, r, L;  x, y, z - допоміжні змінні
