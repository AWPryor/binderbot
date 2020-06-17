from PIL import Image
import random

def Main(): # Main function
    
    LOAD() # Load the images that we wish to get a random hash from.
    HashImages()    # Process each image and put the output in the output folder. 
    
def LoadNewOutput(i): #Loads a single image into the output folder.
    pathInput = 'Input/'+str(i)+'.png'
    pathOutput = 'Output/'+str(i)+'.png'
    im = Image.open(pathInput)
    im.save(pathOutput)
    
def LOAD(): # Loads All images into the output folder.
    LoadNewOutput(1)
    LoadNewOutput(2)
    LoadNewOutput(3)
    LoadNewOutput(4)
    
def SwapSingle(i): # Swaps a pair of random pixil's values.
    pathOutput = 'Output/'+str(i)+'.png'
    im = Image.open(pathOutput)
    columns, rows = im.size
    c1 = random.randint(0,columns)
    c2 = random.randint(0,columns)
    r1 = random.randint(0,rows)
    r2 = random.randint(0,rows)
    pix = im.load()
    holder = pix[c1,r1]
    pix[c1,r1]=pix[c2,r2]
    pix[c2,r2]=holder
    im.save(pathOutput)
    
def GetSingleHash(j): # Generates a new hash for a single image by swapping random pixils
    k = random.randint(1,5)
    for i in range (k):
        SwapSingle(j)
        
def HashImages(): # Hashes all images
    GetSingleHash(1)
    GetSingleHash(2)
    GetSingleHash(3)
    GetSingleHash(4)
    
Main()   
    
