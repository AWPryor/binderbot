from PIL import Image
import random
import os
import time


def Main(): # Main function
    images = [] #A List which contains the PIL.Images of the Input File.
    print('Starting')
    ClearOutput() # Clears the Output folder.
    images = Load() # Load the images that we wish to get a random hash from.
    images = HashImages(images)# Process each image in the images List.
    Save(images)# Save the processed images in the image list to the Output folder.
    print('Finished')
    
    
def Load(): # Loads the images from the Input folder and returns a list of PIL.Images.
    images = []
    with os.scandir("Input") as dirs:
        for entry in dirs:
            im = Image.open("Input/"+entry.name)
            images.append(im)
    return images

def Save(images): # Saves processed images to the Output folder
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
    k = random.randint(5,10)
    for i in range (k):
        im = SwapSingle(im)
    return im
        
def HashImages(img): # Hashes all images
    images = img
    for k in range(len(images)):
        images[k] = GetSingleHash(images[k])
    return images
    
def ClearOutput(): # Clears the Output Folder
    path = r"Output"
    with os.scandir(path) as dirs: # Iteratively removes each file inside the output folder.
        for entry in dirs:
            os.remove("Output/"+entry.name)
            
start_time = time.time() # Code to find the runtime of the function.
Main()
print("--- Time to hash images: %s seconds ---" % (time.time() - start_time))