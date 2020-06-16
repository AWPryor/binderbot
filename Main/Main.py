import vpnCon;
import vpnDis;
import MD5Sig;


def intro():
    print("-------------------------------------------");
    print("-------------------------------------------");
    print("-------------------------------------------");
    print("Hello, Welcome to the tinder account creation tool");
    print("Press 1 to change image signitures");
    print("Press 2 to connect to Nord VPN");
    print("Press 3 to disconnect to Nord VPN");

    choise = input("Select a number: ")
    if (choise == 1):
        MD5Sig.Main();
        intro();
    elif (choise ==2):
        vpnCon.Main();
        intro();
    elif (choise ==3):
        vpnDis.Main();
        intro();


intro()
