def isPrime(n):   
    if n <= 1:    
        return False
    for i in range (2,n//2 + 1):   
        if n % i ==0:          
            return False       
    return True

n = int(input("Bir sayı giriniz:"))

if isPrime(n) == True:
    print(n, "sayısı bir asal sayıdır.")
else:
    print(n, "sayısı bir asal sayı değildir.")    

# Yöntem 2

def isPrime(sayi):    
    if sayi <= 1:
        return False
    if sayi <= 3:
        return True
    if sayi % 2 == 0 or sayi % 3 == 0:
        return False
    i = 5
    while i * i <= sayi:     
        if sayi % i == 0 or sayi % (i + 2) == 0:
            return False
        i += 6
    return True

sayi = int(input("Bir sayı giriniz: "))

if isPrime(sayi):
    print(sayi, "bir asal sayıdır.")
else:
    print(sayi, "bir asal sayı değildir.")

  

        
