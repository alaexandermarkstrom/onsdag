import random #importera random så det kan användas
onsdag = 0 #variabel för att ge en input
onsdagslistan = ["Du gissade rätt!", "Du gissade fel!"] #lista för att ge resultat istället för att skriva allt flera gånger
while True: #while loop som är igång tills break körs
    ai = random.randint(1, 4) #slumpar ett nummer mellan 1-4
    try: #försöker få dig att skriva in ett nummer
        onsdag = int(input("Här gissar du ett nummer\n>"))
    except: #om du inte skriver in ett nummer
        print("Du måste välja ett nummer") #du får veta att du måste välja ett nummer

    if onsdag == 1: #om du väljer 1
        if ai == 1: #om du och ai väljer 1
            print(onsdagslistan[0]) #skriver ut den första meningen i listan
            break #avslutar loopen
        elif ai == 2:
            print(onsdagslistan[1])
        elif ai == 3:
            print(onsdagslistan[1])
        elif ai == 4:
            print(onsdagslistan[1])
    elif onsdag == 2:
        if ai == 1:
            print(onsdagslistan[0])
        elif ai == 2:
            print(onsdagslistan[0])
            break
        elif ai == 3:
            print(onsdagslistan[0])
        elif ai == 4:
            print(onsdagslistan[0])
    elif onsdag == 3:
        if ai == 1:
            print(onsdagslistan[0])
        elif ai == 2:
            print(onsdagslistan[0])
        elif ai == 3:
            print(onsdagslistan[0])
            break
        elif ai == 4:
            print(onsdagslistan[0])
    elif onsdag == 4:
        if ai == 1:
            print(onsdagslistan[0])
        elif ai == 2:
            print(onsdagslistan[0])
        elif ai == 3:
            print(onsdagslistan[0])
        elif ai == 4:
            print(onsdagslistan[1])
            break
    else: #om du skriver ett nummer som inte är mellan 1-4
        print("Du kan bara gissa mellan 1-4!")