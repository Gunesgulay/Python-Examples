def ebob(sayi1, sayi2):     
    while sayi2:
        sayi1, sayi2 = sayi2, sayi1 % sayi2     
    return sayi1                                    

def ekok(sayi1, sayi2):                             
    return sayi1 * sayi2 // ebob(sayi1, sayi2)         

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))    

ebob_sonuc = ebob(sayi1, sayi2)
ekok_sonuc = ekok(sayi1, sayi2)

print(sayi1, "ve", sayi2, "sayılarının EBOB'u:",ebob_sonuc)
print(sayi1, "ve", sayi2, "sayılarının EKOK'u:",ekok_sonuc)