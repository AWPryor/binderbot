import hashlib


def Main():
    checkOld();
    Hash();

def checkOld():
        old = hashlib.md5(open('Test.jpg','rb').read()).hexdigest(); #rb = readbyte ,so it will work for text as well as media (image,video) files
        print("Your old md5 hash was " + old);


def Hash():
    file = open('Test.jpg', 'rb').read()
    with open('Test.jpg', 'wb') as new_file:
        new_file.write(file+'\0')  #here we are adding a null to change the file content
    New = hashlib.md5(open('Test.jpg','rb').read()).hexdigest();
    print("Your new md5 hash was " + New);

Main();
