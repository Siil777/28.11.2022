
#Задача 

#В программе должны выполняться ниже следующие действия:

# вывод на экран приветствия "Tere! Olen sinu uus sõber - Python!"
# присваивание переменной nimi введённого пользователем имени
# вывод на экран текста: nimi ", oi kui ilus nimi!" 
# вывод на экран текста: nimi  "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "
import sys
print('hi there !I am the Python your new friend')
while True:
	t=input('would you like to check your weight?')
	if t.lower()=='yes' or 'no':
			if t=='yes':
				try:
					height=int(input('enter height:'))
				except:
					height=200
					print('illigal', height=200)
				try:
					mass=int(input('enter mass:'))
	
				except:
					mass=100
					print('incorrect', mass=100)
				try:
					index=mass/(0.01*height)**2
				except:
					print('error')
				if index<16:
					print('dangerous underweight')
				elif index>=16 and index<19:
					print('underwight')
				elif index>19 and index<=25:
					print('normal weight')
				elif index>25 and index<=35:
					print('overweight')
				elif index>35 and index<=40:
					print('extreme obesity')
				elif index>40:
					print('high-risk-obesity')
			else:
				print('that a pity, this is realy usefull info')
				sys.exit()
	
		
	
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
  
    







        
 

    




