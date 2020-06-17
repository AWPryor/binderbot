import requests
phoneid = [];


def ask():
    print("Press 1 to check balance");
    print("Press 2 to check order gmail ukrane phone")
    print("Press 3 to check order")
    choise = input("Hello, Please select a service")

    if (choise == '1') :
        accBalance();
        ask();
    elif (choise =='2'):
        savePhone();
        ask();
    elif (choise =='3'):
        print(savePhone);
        checkPhone(phoneid);

        ask();
def savePhone():
    phoneid = buyPhone();

def accBalance():
    response = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key=eefdddb60352ece3762c37AcA4efccA2&action=getBalance')
    Responce = response.text
    print(Responce)

def buyPhone():
    response1 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key=eefdddb60352ece3762c37AcA4efccA2&action=getNumber&service=oi$&ref=745234$ref&country=1');
    Responce1 = response1.text;
    print(Responce1);
    return Responce1.split(":");

def checkPhone(phoneid):
        print(phoneid)
        response2 = requests.post('https://sms-activate.ru/stubs/handler_api.php?api_key=eefdddb60352ece3762c37AcA4efccA2&action=getStatus&id='+phoneid[1] + '275173238');
        Responce2 = response2.text;
        print(Responce2);


ask();
