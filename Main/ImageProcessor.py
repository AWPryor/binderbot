from PIL import Image
import random
import os

images = []


def Main(): # Main function
    print('Starting')
    ClearOutput()
    LOAD() # Load the images that we wish to get a random hash from.
    HashImages()    # Process each image and put the output in the output folder.
    Save(images)
    print('Finished')
    
    
def LOAD(): # Loads All images into the output folder.
    global images
    images = []
    with os.scandir("Input") as dirs:
        for entry in dirs:
            im = Image.open("Input/"+entry.name)
            images.append(im)

def Save(images):
    for k in range(len(images)):
        images[k].save("Output/"+str(k)+".png")
    
def SwapSingle(im): # Swaps a pair of random pixil's values.
    columns, rows = im.size
    c1 = random.randint(0,columns)
    c2 = random.randint(0,columns)
    r1 = random.randint(0,rows)
    r2 = random.randint(0,rows)
    pix = im.load()
    holder = pix[c1,r1]
    pix[c1,r1]=pix[c2,r2]
    pix[c2,r2]=holder
    return im
    
def GetSingleHash(im): # Generates a new hash for a single image by swapping random pixils
    k = random.randint(1,5)
    for i in range (k):
        im = SwapSingle(im)
    return im
        
def HashImages(): # Hashes all images
    global images
    for k in range(len(images)):
        images[k] = GetSingleHash(images[k])
    
def ClearOutput(): # Clears the Output Folder
    path = r"Output"
    with os.scandir(path) as dirs: # Iteratively removes each file inside the output folder.
        for entry in dirs:
            os.remove("Output/"+entry.name)
            

import time
start_time = time.time()
Main()
print("--- Time to complete hashing: %s seconds ---" % (time.time() - start_time))
