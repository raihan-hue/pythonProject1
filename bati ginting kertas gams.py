from random import randint

# buat list option untuk permainan
glist = ["Gunting", "Batu", "Kertas"]

# buat bilihan secara radom dengan func randint
komputer = glist[randint(0,2)].lower()

# set pemain ke false
pemain = False

while pemain == False:
    #set pemain ke true
    pemain = input("Gunting, Batu, Kertas: ").lower()
    print(pemain)
    if pemain == komputer:
        print(("seri"))
    elif pemain == "Batu".lower():
        if komputer == "Kertas".lower():
            print("kamu kalah!", pemain, "membungkus", pemain)
        else:
            print("kamu menang!", pemain, "menghancurkan", komputer)
    elif pemain == "Kertas".lower():
        if komputer == "Gunting".lower():
            print("kamu kalah!", komputer, "memotong", pemain)
        else:
            print("kamu menang!", pemain, "membungkus", komputer)
    elif pemain == "Gunting".lower():
        if komputer == "Batu".lower():
            print("kamu kalah!", komputers, "menghancurkan", pemain)
        else:
            print("kamu menang!", pemain, "memotong", komputer)
    else:
        print("pilihan yang kamu masukan salah...")

        #ini ulang permainannya

    pemain = False
komputer = glist[randint(0,2)]