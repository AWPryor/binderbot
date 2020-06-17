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
    print("Your new Hashes are: ")
    new1 = hashlib.md5(open('Images\Test.jpg','rb').read()).hexdigest();
    hasher = hashlib.md5()
    with open('Images\Test.jpg', 'ab') as afile:
        buf = afile.write(b'\0')
    new = hashlib.md5(open('Images\Test.jpg','rb').read()).hexdigest();


    hasher1 = hashlib.md5()
    with open('Images\Test1.jpg', 'ab') as afile:
        buf = afile.write(b'\0')
    new1 = hashlib.md5(open('Images\Test1.jpg','rb').read()).hexdigest();

    hasher2 = hashlib.md5()
    with open('Images\Test2.jpg', 'ab') as afile:
        buf = afile.write(b'\0')
    new2 = hashlib.md5(open('Images\Test2.jpg','rb').read()).hexdigest();

    hasher3 = hashlib.md5()
    with open('Images\Test3.jpg', 'ab') as afile:
        buf = afile.write(b'\0')
    new3 = hashlib.md5(open('Images\Test3.jpg','rb').read()).hexdigest();


    print("Hash1: " + new);
    print("Hash2: " + new1);
    print("Hash3: " + new2);
    print("Hash4: " + new3);



Main();
