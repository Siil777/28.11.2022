
#Задача 

#В программе должны выполняться ниже следующие действия:

# вывод на экран приветствия "Tere! Olen sinu uus sõber - Python!"
# присваивание переменной nimi введённого пользователем имени
# вывод на экран текста: nimi ", oi kui ilus nimi!" 
# вывод на экран текста: nimi  "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "
print("Tere! Olen sinu uus sober - Python!")
a=input("Kas leian Sinu kehaa indeksi ? 0-ei 1-jah=>")
if a=="1":
    try:
        pikkus=int(input("pikkus"))
    except:
        pikkus=175
        print("error, pikkus=175")
    try:
        mass=int(input("mass"))
    except:
        mass=55
        print("error, kui mass=55")
    try:
        index=mass/(0.01*pikkus)**2
    except:
        print("error")
    if  index<16:  
        print("Ohtlik alakaal")
    if index>=16 and index<=19:
        print("Alakaal")
    if index>19 and index<=25:
         print("Normalkaal")
    if index>25 and index<=30:
        print("Ulekaal")
    if index>30 and index<=35:
        print("Rasvumine")
    if index>35 and index<=40:
        print("Tugev rasvumine")
    if index>40:
        print("Ohtlik rasvumine")
else:
    print("Kahju! see on vaga kasulik info")
    print("")
    print("Kohtumiseni, Pavel !Igavesti sinu,Python!")


#Цикл (FOR,WHILE,WHILE True)
#1 option 
#1.Вводят 15 чисел. Определить, сколько среди них целых.
import math

j=0
for i in range(1,16,1):
    A=float(input(f"sisesta A:"))
    int(A)==A
    if int(A)==A: j+=1
print(j)

#Цикл (FOR,WHILE,WHILE True)
#2 option 
#1.Вводят 15 чисел. Определить, сколько среди них целых.

j=0
i=0
while True:
    i+=1
    A=float(input(f"{i} sisesta A:"))
    if int(A)==A: j+=1
    if i==15: break
print(j)

#Цикл (FOR,WHILE,WHILE True)
#3 option 
#1.Вводят 15 чисел. Определить, сколько среди них целых.

j=0
i=0
while i<15:
    i+=1
    A=float(input(f"{i} sisesta A:"))
    if int(A)==A: j+=1
print(j)
        
        
       
    
    
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
  
    







        
 

    




