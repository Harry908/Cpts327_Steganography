import cv2
import string
import os
d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)
  
  
#print(c)

x=cv2.imread("Project/TestImage.jpg")

i=x.shape[0]
j=x.shape[1]
print(i,j)

key=input("Enter key to edit(Security Key) : ")
text=input("Enter text to hide : ")
text+='\0'
kl=0
tln=len(text)
z=0 #decides plane
n=0 #number of row
m=0 #number of column

l=len(text)

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[kl]]
    n=n+1
    m=m+1
    m=(m+1)%3 #this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
                #whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
    kl=(kl+1)%len(key)
    
cv2.imwrite("encrypted2_img.png",x) 
os.startfile("encrypted2_img.png")
print("Data Hiding in Image completed successfully.")

#print(x)
y=cv2.imread("encrypted2_img.png")
#print(x==y)

kl=0
tln=len(text)
z=0 #decides plane
n=0 #number of row
m=0 #number of column

ch = int(input("\nEnter 1 to extract data from Image : "))

if ch == 1:
    key1=input("\n\nRe enter key to extract text : ")
    decrypt=""

    if key == key1 :
        while True:
            # Check if we are within the bounds of the image
            if n >= y.shape[0] or m >= y.shape[1]:
                print("Reached the end of the image data.")
                break

            # Get the character by XORing
            char_code = y[n, m, z] ^ d[key[kl]]

            # Ensure char_code is within valid range
            if char_code < 0 or char_code > 255:
                print(f"Invalid char_code {char_code} at position ({n}, {m}). Aborting decryption.")
                break

            decrypted_char = c[char_code]

            # Check for the termination character to stop
            if decrypted_char == '\0':
                break

            decrypt += decrypted_char
            n += 1
            m += 1
            m = (m + 1) % 3  # Cycle through color channels
            kl = (kl + 1) % len(key)

            # Prevent index out of bounds if the text is longer than the image size
            if m >= y.shape[1]:  # Check column limit
                n += 1
                m = 0  # Reset column index for the next row
        print("Encrypted text was : ",decrypt)
    else:
        print("Key doesn't matched.")
else:
    print("Thank you. EXITING.")