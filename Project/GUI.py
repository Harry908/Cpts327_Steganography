import customtkinter
from tkinter import filedialog
from PIL import Image
import cv2

# Welcome page
class WelcomeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Set alignment for content
        # Configure rows for vertical centering and balanced spacing
        self.grid_rowconfigure(0, weight=1)  # Top spacer
        self.grid_rowconfigure(1, weight=0)  # Label row
        self.grid_rowconfigure(2, weight=1)  # Spacer between label and first button
        self.grid_rowconfigure(3, weight=0)  # Encrypt button row
        self.grid_rowconfigure(4, weight=0)  # Spacer between buttons
        self.grid_rowconfigure(5, weight=0)  # Decrypt button row
        self.grid_rowconfigure(6, weight=1)  # Bottom spacer
        self.grid_columnconfigure(0,weight=1)

        # Create and place a label in the frame
        label = customtkinter.CTkLabel(self, text="Welcome to Image Steganography App", font=("Arial", 26))
        label.grid(row=1, column=0, pady=20, padx=20, sticky="ew")  # Place the label using grid

        # Create and place a button in the frame
        button = customtkinter.CTkButton(self, text="Encrypt",command= self.encryptBtn_callback)
        button.grid(row=3, column=0, pady=10, padx=20, sticky="ew")  # Place the button using grid

        # Create and place a button in the frame
        button = customtkinter.CTkButton(self, text="Decrypt", command=self.decryptBtn_callback)
        button.grid(row=5, column=0, pady=10, padx=20, sticky="ew")  # Place the button using grid

    # Action for encrypt button
    def encryptBtn_callback(self):
        self.master.show_encrypt_frame()  # Call the method in App to switch frames

    # Action for encrypt button
    def decryptBtn_callback(self):
        self.master.show_decrypt_frame()

# Encrypt function page
class EncryptFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Fields
        self.oimage = None
        self.eimageMatrix = None

        # Grid layout
        self.grid_columnconfigure(0, weight=1)
        # Top spacer
        self.grid_rowconfigure(0, weight=1)
        # Content rows
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
        self.grid_rowconfigure(7, weight=0)
        self.grid_rowconfigure(8, weight=0)
        self.grid_rowconfigure(9, weight=0)
        self.grid_rowconfigure(10, weight=0)
        # bottom spacer
        self.grid_rowconfigure(11, weight=1)

        # Create and place a label for message input
        label_message = customtkinter.CTkLabel(self, text="Message:", font=("Arial", 16))
        label_message.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        # Create and place a text input field for message
        self.entry_message = customtkinter.CTkEntry(self)
        self.entry_message.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a label for security key input
        label_key = customtkinter.CTkLabel(self, text="Security Key:", font=("Arial", 16))
        label_key.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        # Create and place a text input field for security key
        self.entry_key = customtkinter.CTkEntry(self)
        self.entry_key.grid(row=5, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a placeholder for the image
        self.image_placeholder = customtkinter.CTkLabel(self, text="No Image Selected", font=("Arial", 16))
        self.image_placeholder.grid(row=6, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a button to open an image file
        button_open_image = customtkinter.CTkButton(self, text="Open Image", command=self.open_image)
        button_open_image.grid(row=7, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a button to encrypt message
        button_encrypt = customtkinter.CTkButton(self, text="Encrypt", command=self.encrypt_callback)
        button_encrypt.grid(row=8, column=0, pady=10, padx=20, sticky="ew")

    def encrypt_callback(self):
        # TODO: Add encryption logic here

        # Simulate encryption logic and show success message
        self.show_success_message()

    def show_success_message(self):
        # Create a label to show success message (initially hidden)
        self.success_message_label = customtkinter.CTkLabel(self, text="Successfully encrypted message!",
                                                            font=("Arial", 16, "bold"), text_color="green")
        self.success_message_label.grid(row=9, column=0, pady=10, padx=10, sticky="ew")

        # Create and place a button to view encrypted image
        self.button_viewEI = customtkinter.CTkButton(self, text="View encrypted image", command=self.viewEI_callback)
        self.button_viewEI.grid(row=10, column=0, pady=10, padx=20, sticky="ew")

    def viewEI_callback(self):
        # TODO change frame to view encrypted image
        self.master.show_viewEI_frame(self.entry_message.get(), self.entry_key.get(), self.oimage, self.eimageMatrix)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((300, 300))  # Resize image to fit the placeholder
            self.oimage = customtkinter.CTkImage(light_image=image, dark_image=image, size=(300, 300))
            self.image_placeholder.configure(image=self.oimage)

# View encrypted image page
class ViewEIFrame(customtkinter.CTkFrame):
    def __init__(self, master, message, key, oimage, eimageMatrix):
        super().__init__(master)

        self.message = message
        self.key = key
        self.oimage = oimage
        self.eimageMatrix = eimageMatrix

        # Grid layout
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1)
        # Create and place a "Home" button in the top-left corner
        home_button = customtkinter.CTkButton(self, text="Home", command=self.go_home)
        home_button.grid(row=0, column=0, pady=10, padx=10, sticky="nw", columnspan=2)  # "nw" = top-left

        # Display message and key
        label_message = customtkinter.CTkLabel(self, text="Message: " + self.message, font=("Arial", 16))
        label_message.grid(row=1, column=0, pady=10, padx=20, sticky="w", columnspan=2)

        label_key = customtkinter.CTkLabel(self, text="Security Key: " + self.key, font=("Arial", 16))
        label_key.grid(row=2, column=0, pady=10, padx=20, sticky="w", columnspan=2)

        # Display original image and encrypted image side by side
        label_oimage = customtkinter.CTkLabel(self, text="Original Image", font=("Arial", 14))
        label_oimage.grid(row=3, column=0, pady=10, padx=20, sticky="ew")

        label_eimage = customtkinter.CTkLabel(self, text="Encrypted Image", font=("Arial", 14))
        label_eimage.grid(row=3, column=1, pady=10, padx=20, sticky="ew")

        # Convert PIL image to CTkImage for display
        self.oimage_label = customtkinter.CTkLabel(self, image=self.oimage)
        self.oimage_label.grid(row=4, column=0, pady=10, padx=20, sticky="ew")

        self.eimage_label = customtkinter.CTkLabel(self, image=self.oimage)  # Dummy placeholder for now
        self.eimage_label.grid(row=4, column=1, pady=10, padx=20, sticky="ew")

        # Button to save the encrypted image
        button_save_image = customtkinter.CTkButton(self, text="Save Encrypted Image", command=self.save_image)
        button_save_image.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

    def go_home(self):
        # Logic to go back to home screen (could be showing the welcome frame)
        #print("Going back to Home Screen")
        self.master.show_welcome_frame()  # Assuming you have a method to show the welcome frame

    def save_image(self):

        # Ask user to select a file location to save the image
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            # Save the encrypted image using OpenCV
            cv2.imwrite(file_path, self.eimageMatrix)
            print(f"Encrypted image saved at: {file_path}")

    def update_encrypted_image(self, encrypted_image):
        # Convert encrypted image to CTkImage for display
        self.eimage = customtkinter.CTkImage(light_image=encrypted_image, dark_image=encrypted_image, size=(300, 300))
        self.eimage_label.configure(image=self.eimage)

# Decrypt frame
class DecryptFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Fields
        self.image_path = None
        self.decrypted_message = None
        self.oimage = None  # This will store the image in CTkImage format

        # Grid layout
        self.grid_columnconfigure(0, weight=1)
        # Top spacer
        self.grid_rowconfigure(0, weight=1)
        # Content rows
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
        self.grid_rowconfigure(7, weight=0)
        # bottom spacer
        self.grid_rowconfigure(8, weight=1)

        # Create and place a "Home" button in the top-left corner
        home_button = customtkinter.CTkButton(self, text="Home", command=self.go_home)
        home_button.grid(row=0, column=0, pady=10, padx=10, sticky="nw")  # "nw" = top-left

        # Create and place a label for security key input
        label_key = customtkinter.CTkLabel(self, text="Security Key:", font=("Arial", 16))
        label_key.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        # Create and place a text input field for security key
        self.entry_key = customtkinter.CTkEntry(self)
        self.entry_key.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        # Create a label to display the image (initially hidden)
        self.image_placeholder = customtkinter.CTkLabel(self, text="No image selected")
        self.image_placeholder.grid(row=3, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a button to open an image file
        button_open_image = customtkinter.CTkButton(self, text="Open Encrypted Image", command=self.open_image)
        button_open_image.grid(row=4, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a button to decrypt message
        button_decrypt = customtkinter.CTkButton(self, text="Decrypt", command=self.decrypt_callback)
        button_decrypt.grid(row=5, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a label to display the decrypted message (initially hidden)
        self.label_decrypted_message = customtkinter.CTkLabel(self, text="", font=("Arial", 16, "bold"))
        self.label_decrypted_message.grid(row=6, column=0, pady=10, padx=20, sticky="ew")



    def go_home(self):
        # Logic to go back to home screen (could be showing the welcome frame)
        #print("Going back to Home Screen")
        self.master.show_welcome_frame()  # Assuming you have a method to show the welcome frame

    def open_image(self):
        # Open the image file (only .png)
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)
            print(f"Image loaded: {file_path}")

    def display_image(self, file_path):
        # Use PIL to open and resize the image for display in the UI
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # Resize image to fit the label
        self.oimage = customtkinter.CTkImage(light_image=image, dark_image=image, size=(300, 300))
        self.image_placeholder.configure(image=self.oimage)
        self.image_placeholder.image = self.oimage  # Keep a reference to avoid garbage collection

    def decrypt_callback(self):
        # Get the security key entered by the user
        key = self.entry_key.get()

        if self.image_path and key:
            # Perform decryption (this is just a placeholder for your actual decryption algorithm)
            decrypted_message = self.decrypt_message(self.image_path, key)

            # Display the decrypted message
            self.label_decrypted_message.configure(text=f"Secret Message: {decrypted_message}")

    def decrypt_message(self, image_path, key):
        # Placeholder for actual decryption logic
        # In this method, you would load the image, extract the encoded data using the provided key,
        # and return the decrypted message.

        # Example: Load image using OpenCV
        image = cv2.imread(image_path)
        # Example decryption logic (you should replace this with your actual decryption algorithm)
        decrypted_message = "This is a decrypted message"  # Replace with actual decrypted data
        return decrypted_message

# Main app window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Image Steganography")
        self.geometry("1000x800")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.welcome_frame = WelcomeFrame(self)
        self.welcome_frame.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

        self.encrypt_frame = None
        self.viewEI_frame = None
        self.decrypt_frame = None

    # Render encrypt function page
    def show_encrypt_frame(self):
        self.welcome_frame.grid_forget()
        self.encrypt_frame = EncryptFrame(self)
        self.encrypt_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show EncryptFrame
    # Show encrypted image
    def show_viewEI_frame(self, message, key, oimage, eimageMatrix):
        if self.encrypt_frame is not None:
            self.encrypt_frame.destroy()
        self.viewEI_frame = ViewEIFrame(self,message,key,oimage,eimageMatrix)
        self.viewEI_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Render decrypt function page
    def show_decrypt_frame(self):
        self.welcome_frame.grid_forget()
        self.decrypt_frame = DecryptFrame(self)
        self.decrypt_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Go back to home page
    def show_welcome_frame(self):
        if self.decrypt_frame is not None:
            self.decrypt_frame.destroy()
        if self.viewEI_frame is not None:
            self.viewEI_frame.destroy()
        self.welcome_frame.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

app = App()
app.mainloop()