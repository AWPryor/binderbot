
import os;
import phoneapi;


def intro():
    print("-------------------------------------------");
    print("-------------------------------------------");
    print("-------------------------------------------");
    print("Hello, Welcome to the tinder account creation tool");
    print("Press 1 to change image signitures");
    print("Press 2 to connect to Nord VPN");
    print("Press 3 to disconnect to Nord VPN");
    print('Press 4 to buy phone numbers')
    print('Press 5 to clear cache')
    choise = input("Select a number: ");
    print(type(choise));

    if (choise == "1"):
        os.system('ImageProcessor.py');
        print('done')
        intro();

    elif (choise == "2"):
        os.system('vpnCon.py');
        print("You are now connected")
        intro();
    elif (choise == "3"):
        os.system('vpnDis.py');
        print("You are now disconnected")
        intro();
    elif (choise == '4'):
        phoneapi.ask();
        intro();
    elif (choise == '5'):
        os.system('ClearBrowser.py');
        print('cookies cleared')
        intro();





intro();