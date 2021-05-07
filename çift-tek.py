#!/usr/bin/env python
# coding: utf-8

# In[1]:


s=input("Bir sayi giriniz: ")
sayi=int(s)
if sayi%2==0:
    print("{} sayısı çift sayıdır".format(sayi))
else:
    print("{} sayısı tek sayıdır".format(sayi))

