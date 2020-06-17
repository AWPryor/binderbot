import os

def Main():
    print("-------------------------------------------");
    print("-------------------------------------------");
    print("-------------------------------------------");
    print("Initiating Automation...");
    os.system('vpnCon.py');
    print("Connecting to VPN...");
    os.system('ClearBrowser.py');
    print('Browser data cleared.')
    print('Changing Input signatures...')
    os.system('ImageProcessor.py');
    print('Input processing complete.')
    print("Automation steps completed. Awaiting phone order.")

Main()