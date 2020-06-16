#Tinder bot account creator


def intro():
    print("Hello, Welcome to the tinder account creation tool");
    print("Press 1 to change image signitures");
    print("Press 2 to connect to Nord VPN");
    print("Press 3 to disconnect to Nord VPN");

    choise = input("Select a number")
    if (choise == 1):
            import MD5Sig;

    elif (choise ==2):
        import vpnCon;
    elif (choise ==3):
        import vpnDis;


intro()
