#arv=print("arv")

#try:
#    arv=int(arv)
#    print("int")
#except:
#    try:
#        arv=float(arv)
#        print("Float")
#    except:
#        print("tekst")


#Задача 

#В программе должны выполняться ниже следующие действия:

#            вывод на экран приветствия "Tere! Olen sinu uus sõber - Python!"
#            присваивание переменной nimi введённого пользователем имени
#            вывод на экран текста: nimi ", oi kui ilus nimi!" 
#            вывод на экран текста: nimi  "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "

#print("Tere! Olen sinu uus sober - Python")

#nimi=input("")
#print(",oi kui ilus nimi!", nimi)
#vastus=input("Kas leian Sinu keha indeksi ? 0-ei, ja-jah=>")
#a=input("Pikkus")
#print("Pikkus")
#if a.isdigit():


print("Tere! Olen sinu uus sober - Python")
a=input("Kas leian Sinu keha indeksi ? 0-ei, 1-jah=>")
if a=="1":
    try:
        pikkus=int(input("pikkus"))
    except:
        pikkus=175
        print("error, pikkus=175")
    try:
        mass=int(input("Mass: "))
    except:
        mass=55
        print("Error, siis mass=55")
    try:
        index=mass/0.01**2
        if index<16:
            print("Ohtlik alakaal")
        elif index>=16 and index<19:
            print("Alakaal")
    except:
        print("error")
    if index>15 and index<20:
        print("Alakaal")
    if index>18 and index<26:
        print("Normaalkaal")
    if index>24 and index<31:
        print("Ulekaal")
    if index>29 and index<36:
        print("Rasvumine")
    if index>34 and index<41:
        print("Tugev rasvumine")
    if index>40:
        print("Ohtlik rasvumine")
        
        
        print("Tere! Olen sinu uus sober - Python")
a=input("Kas leian Sinu keha indeksi ? 0-ei, 1-jah=>")
if a=="1":
    while True:
        try:
            pikkus=int(input("pikkus"))
            if pikkus>0 and pikkus<273: break
        except:
            
            print("error, pikkus=175")
    mass=-1
    while mass<0 or mass>400:
        try:
            mass=int(input("Mass: "))
        except:
            
            print("Error, siis mass=55")
  
    







        
 

    




