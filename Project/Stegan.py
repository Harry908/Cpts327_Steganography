import cv2
import os

#Create ASCII dictionary
#d={chr(i): i for i in range(255)}
#c={i: chr(i) for i in range(255)}
d={}
c={}
for i in range(256):
    d[chr(i)]=i
    c[i]=chr(i)
#print(c)

def getImagePath():
    """
    Prompt the user to input the path of the image.
    """
    return input("Please enter the path to the image file: ")

def validatePath(imagePath):
    """
    Check if the provided image path exists and is a file.
    """
    if not os.path.isfile(imagePath):
        print(f"The file at {imagePath} does not exist.")
        return False
    return True

def importImage():
    # Get image file and validate
    imagePath = getImagePath()
    while(not validatePath(imagePath)):
        imagePath=getImagePath()
    return cv2.imread(imagePath)

def getMatrix(filePath):
    return cv2.imread(filePath)

def getMaxLength(imageMatrix):
    return imageMatrix.shape[0] # number of row

# Encrypt image
def encrypt(imageMatrix, key, text):
    i=imageMatrix.shape[0]
    j=imageMatrix.shape[1]
    print(i,j)
    
    text+="\0" # mark the end of text

    kl=0
    z=0 #decides plane
    n=0 #number of row
    m=0 #number of column
    l=len(text)

    for i in range(l):
        imageMatrix[n,m,z]=d[text[i]]^d[key[kl]]
        n=n+1
        m=m+1
        m=(m+1)%3
        kl=(kl+1)%len(key)

    return imageMatrix

# Save encrypted image
def saveEncrypted(imageMatrix):
    # Prompt user encrypted image name
    encryptedImage = input("Please enter encrypted image's name: ")
    encryptedImage += ".png"
    cv2.imwrite(encryptedImage, imageMatrix)
    os.startfile(encryptedImage)
    print("Data Hiding in Image completed successfully.")


class DecryptionError(Exception):
    pass


# Decrypt image function return a string
# Throw DecryptionError
def decrypt(imageMatrix, key):
    kl = 0
    z = 0  # decides plane
    n = 0  # number of row
    m = 0  # number of column

    decryptText = ""

    while True:
        # Check if we are within the bounds of the image
        if n >= imageMatrix.shape[0] or m >= imageMatrix.shape[1]:
            raise DecryptionError("Reached the end of the image data.")

        # Get the character by XORing
        char_code = imageMatrix[n, m, z] ^ d[key[kl]]

        # Ensure char_code is within valid range
        if char_code < 0 or char_code > 255:
            raise DecryptionError(f"Invalid char_code {char_code} at position ({n}, {m}).")

        decrypted_char = c[char_code]

        # Check for the termination character to stop
        if decrypted_char == '\0':
            break

        decryptText += decrypted_char
        n += 1
        m += 1
        m = (m + 1) % 3  # Cycle through color channels
        kl = (kl + 1) % len(key)

        # Prevent index out of bounds if the text is longer than the image size
        if m >= imageMatrix.shape[1]:  # Check column limit
            n += 1
            m = 0  # Reset column index for the next row

    return decryptText


def main():
     while True:
        choice = input("Enter '1' to encrypt an image, '2' to decrypt an image, or any key to quit: ")

        if choice == '1':
            imageMatrix = importImage()
            # Prompt security key and message
            key = input("Enter key to edit (Security Key): ")
            text = input("Enter text to hide : ")
            imageMatrix = encrypt(imageMatrix, key, text)
            saveEncrypted(imageMatrix)
        elif choice == '2':
            imageMatrix = importImage()
            key = input("\n\nEnter key to extract text : ")
            decryptText = decrypt(imageMatrix, key)
            print("Encrypted text was : ", decryptText)
        else:
            print("Exiting...")
            return

if __name__ == "__main__":
    main()