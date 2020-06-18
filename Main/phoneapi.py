import requests;
apikey = 'eefdddb60352ece3762c37AcA4efccA2';


def ask():
    print("Press 1 to check balance");
    print("Press 2 to order phones")
    print("Press 3 to exit")
    choise = input("Hello, Please select a service")

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
        print('Press 1 for Google')
        print('Press 2 for tinder')
        service = input('Select an option: ')
        if (service == '1'):
            serviceId = 'go'
        elif (service == '2'):
            serviceId='oi'
        print(serviceId)
        print(countryId)
        phoneid=buyPhone(serviceId, countryId);
        while alwaystrue:
            print('Press 1 to check status')
            print('Press 2 to check phone number')
            print('Press 3 to exit - Note if you had an error please exit and reorder')
            b = input("Select your option: ")

            if (b == '1'):
                print(phoneid[1])
                response2 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key='+apikey+'&action=getStatus&id='+phoneid[1]);
                Responce2 = response2.text;
                print(Responce2);
            elif (b == '2'):
                print(phoneid[2])
            elif (b == '3'):
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
        print(phoneid)
        response2 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key=eefdddb60352ece3762c37AcA4efccA2&action=getStatus&id='+phoneid[1]+'275173238');
        Responce2 = response2.text;
        print(Responce2);


