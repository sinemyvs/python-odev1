#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for m in range(1,6):
    sayi=int(input("Sayıyı Girin : "))
    if sayi > 1:
        for i in range(2,sayi):
            if (sayi % i) == 0:
                print(sayi," Asal Sayı Değildir.")
                break
        else:
            print(sayi," Asal Sayıdır.")
    else:
        print(sayi," Asal Sayı Değildir.")

