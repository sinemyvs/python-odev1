def TemizVeri(): 
    ilk_string ="Ah5me4t" 
    ikinci_string = "M9eHm4eT" 
    ucuncu_string ="Ha3K5a1n" 
    ilk_string=''.join([i for i in ilk_string if not i.isdigit()]) 
    ikinci_string= ''.join([i for i in ikinci_string if not i.isdigit()])
    ucuncu_string=''.join([i for i in ucuncu_string if not i.isdigit()]) 
    Birlesmis_deger="-".join([ilk_string,ikinci_string,ucuncu_string]) 
    print(Birlesmis_deger)
    return Birlesmis_deger
TemizVeri()

