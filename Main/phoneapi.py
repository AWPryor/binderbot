import requests;
apikey = 'eefdddb60352ece3762c37AcA4efccA2';


def ask():
    print("Press 1 to check balance");
    print("Press 2 to order phones")
    print("Press 3 to exit")
    choise = input("Hello, Please select a service: ")

    if (choise == '1') :
        accBalance();
        ask();

    elif (choise =='2'):
        alwaystrue = True;
        print('Press 1 for Ukrane')
        print('Press 2 for England')
        print('Press 3 for Portugal')
        print('Press 4 for Sweden')
        print('Press 5 for Brazil')
        print('Press 6 for Germany')
        print('Press 7 for Italy')
        print('Press 8 for Spain')

        country = input('Select a number: ')
        if (country == '1'):
            countryId = '1';
        elif (country == '2'):
            countryId = '16';
        elif (country == '3'):
            countryId = '117';
        elif (country == '4'):
            countryId = '46';
        elif (country == '5'):
            countryId = '73'
        elif (country == '6'):
            countryId = '43'
        elif (country == '7'):
            countryId = '86'
        elif (country == '8'):
            countryId = '56'
        print('Press 1 for Google')
        print('Press 2 for tinder')
        service = input('Select an option: ')
        if (service == '1'):
            serviceId = 'go'
        elif (service == '2'):
            serviceId='oi'
        phoneid=buyPhone(serviceId, countryId);
        while alwaystrue:
            print('Press 1 to check status')
            print('Press 2 to check phone number')
            print('Press 3 to cancel current number')
            print('Press 4 to confirm the code and go back')
            print('Press 5 to go back and exit')
            b = input("Select your option: ")

            if (b == '1'):
                response2 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+apikey+'&action=getStatus&id='+phoneid[1]);
                Responce2 = response2.text;
                print(Responce2);
            elif (b == '2'):
                print(phoneid[2])
            elif (b == '3'):
                response3 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+apikey+'&action=setStatus&status=8&id='+phoneid[1]);
                print(response3)
                break;
            elif (b == '4'):
                response4 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+apikey+'&action=setStatus&status=6&id=' +phoneid[1]);
                print(response4)

            elif (b == '5'):
                break;



        ask();


    elif(choise =='3'):
        print('goodbye')



def accBalance():
    response = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+apikey+'&action=getBalance')
    Responce = response.text
    print(Responce)

def buyPhone(serviceId, countryId):
    response1 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+apikey+'&action=getNumber&service='+serviceId+'$&ref=745234$ref&country='+countryId);
    Responce1 = response1.text;
    print(Responce1);
    return Responce1.split(":");

def checkPhone(phoneid):
        response2 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key=eefdddb60352ece3762c37AcA4efccA2&action=getStatus&id='+phoneid[1]+'275173238');
        Responce2 = response2.text;
        print(Responce2);


