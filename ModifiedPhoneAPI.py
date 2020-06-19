import requests;


class API:
    
    def __init__(self, key): # Contructor(?) function.
        self.apikey = key
        self.countryID = 0
        self.isWaiting = False
    
    def GetBalance(self):
        response = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+self.apikey+'&action=getBalance')
        print(response.text)
    
    def SetCountryID(self,_int): # Sets the country id.
        self.countryID = str(_int)
        
    def GetcountryID(self): # Get's the country ID.
        return self.countryID
    
    def Waite(self): # Change the isWaiting variable to TRUE.
        self.isWaiting = True
        
    def StopWaite(self): # Change teh isWaiting variable to FALSE.
        self.isWaiting = False
    
    
    
#End of API class


def Main():
    apikey = 'eefdddb60352ece3762c37AcA4efccA2'
    api = API(apikey)
    print("====== Phone API Interface ======")
    Ask(api)
    print("====== Exiting Phone API Interface ======")
    
    
def Ask(D):
    #Text based User Interface.
    print("--- Main menu ---")
    print("1 - Check Balance")
    print("2 - Order Phones")
    print("3 - Exit")
    #Ask for user input.
    choise = input("Please select a service: ")
    
    
    if (choise == '1'): # Get the balance from the API class
        print("--------------")
        D.GetBalance()
        print("--------------")
        Ask(D)
    elif (choise =='2'):
        PhoneBuyer(D)
        Ask(D)
    elif (choise =='3'): # End the recursion.
        print('Goodbye.')
    else: #Catches anything that isn't a hardcoded input.
        print("ERROR: Unexpected Input. Please try again.")
        Ask(D)
        
def PhoneBuyer(D):
    
    def ChoiceManager(D): #Sub-function which manages the choice between google / tinder accounts.
        print("--- Account Choice ---")
        print('1 - Google')
        print('2 - tinder')
        service = input('What type of account would you like?: ')
        if (service == '1'):
            serviceId = 'go'
        elif (service == '2'):
            serviceId='oi'
        phoneid=buyPhone(serviceId, D);
        while (True):
            print('Press 1 to check status.')
            print('Press 2 to check phone number.')
            print('Press 3 to cancel the current number.')
            print('Press 4 to confirm the code and go back.')
            print('Press 5 to go back and exit.')
            b = input("Select your option: ")
            if (b == '1'):
                response2 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+D.apikey+'&action=getStatus&id='+phoneid[1])
                print(response2.text);
            elif (b == '2'):
                print(phoneid[2])
            elif (b == '3'):
                response3 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+D.apikey+'&action=setStatus&status=8&id='+phoneid[1]);
                print(response3)
                break;
            elif (b == '4'):
                response4 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+D.apikey+'&action=setStatus&status=6&id=' +phoneid[1]);
                print(response4)
                break
            elif (b == '5'):
                break;
    
    #Phone Buyer User interface:
    print("--- Order Phones ---") 
    print('1 - Ukrane')
    print('2 - England')
    print('3 - Portugal')
    print('4 - Sweden')
    print('5 - Brazil')
    print('6 - Germany')
    print('7 - Italy')
    print('8 - Spain')
    print("Any Key to exit.")
    country = input('Select the type of number: ')
    
    if (country == '1'):
        D.SetCountryID(1)
        ChoiceManager(D)
    elif (country == '2'):
        D.SetCountryID(16)
        ChoiceManager(D)
    elif (country == '3'):
        D.SetCountryID(117)
        ChoiceManager(D)
    elif (country == '4'):
        D.SetCountryID(46)
        ChoiceManager(D)
    elif (country == '5'):
        D.SetCountryID(73)
        ChoiceManager(D)
    elif (country == '6'):
        D.SetCountryID(43)
        ChoiceManager(D)
    elif (country == '7'):
        D.SetCountryID(86)
        ChoiceManager(D)
    elif (country == '8'):
        D.SetCountryID(56)
        ChoiceManager(D)
        
        
        



def buyPhone(serviceId, D):
    response1 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+D.apikey+'&action=getNumber&service='+serviceId+'$&ref=745234$ref&country='+D.countryID)
    print(response1.text)
    return response1.text.split(":")


    
Main()