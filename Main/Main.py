import os


def intro():
    print("-------------------------------------------");
    print("-------------------------------------------");
    print("-------------------------------------------");
    print("Hello, Welcome to the tinder account creation tool");
    print("Press 1 to change image signitures");
    print("Press 2 to connect to Nord VPN");
    print("Press 3 to disconnect to Nord VPN");
    choise = input("Select a number: ");
    print(type(choise));

    if (choise == "1"):
        os.system('md5Sig.py');
        intro();

    elif (choise == "2"):
        os.system('vpnCon.py');
        print("You are now connected")
        intro();
    elif (choise == "3"):
        os.system('vpnDis.py');
        print("You are now disconnected")
        intro();



intro();