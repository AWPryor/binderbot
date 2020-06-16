import hashlib


def Main():
    checkOld();
    Hash();

def checkOld():
        old = hashlib.md5(open('Images\Test.jpg','rb').read()).hexdigest(); #rb = readbyte ,so it will work for text as well as media (image,video) files
        old1 = hashlib.md5(open('Images\Test1.jpg','rb').read()).hexdigest();
        old2 = hashlib.md5(open('Images\Test2.jpg','rb').read()).hexdigest();
        old3 = hashlib.md5(open('Images\Test3.jpg','rb').read()).hexdigest();
        print("Your old Hashes were:");
        print("Hash1: " + old);
        print("Hash2: " + old1);
        print("Hash3: " + old2);
        print("Hash4: " + old3);





def Hash():
    file = open('Images\Test.jpg', 'rb').read()
    with open('Images\Test.jpg', 'wb') as new_file:
        new_file.write(file+'\0')  #here we are adding a null to change the file content
    New = hashlib.md5(open('Images\Test.jpg','rb').read()).hexdigest();
    print("Your new hashes are");
    print("Hash1: " + New);

    file = open('Images\Test1.jpg', 'rb').read()
    with open('Images\Test1.jpg', 'wb') as new_file:
        new_file.write(file+'\0')  #here we are adding a null to change the file content
    New1 = hashlib.md5(open('Images\Test1.jpg','rb').read()).hexdigest();
    print("Hash2: " + New1);

    file = open('Images\Test2.jpg', 'rb').read()
    with open('Images\Test2.jpg', 'wb') as new_file:
        new_file.write(file+'\0')  #here we are adding a null to change the file content
    New2 = hashlib.md5(open('Images\Test2.jpg','rb').read()).hexdigest();
    print("Hash3: " + New2);

    file = open('Images\Test3.jpg', 'rb').read()
    with open('Images\Test3.jpg', 'wb') as new_file:
        new_file.write(file+'\0')  #here we are adding a null to change the file content
    New3 = hashlib.md5(open('Images\Test3.jpg','rb').read()).hexdigest();
    print("Hash4: " + New3);

Main();
