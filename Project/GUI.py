import customtkinter
from tkinter import filedialog
from PIL import Image, ImageTk
from Stegan import *


# Welcome page
class WelcomeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Set alignment for content
        self.grid_rowconfigure(0, weight=1)  # Top spacer
        self.grid_rowconfigure(1, weight=0)  # Logo row
        self.grid_rowconfigure(2, weight=0)  # Label row
        self.grid_rowconfigure(3, weight=1)  # Spacer between label and first button
        self.grid_rowconfigure(4, weight=0)  # Encrypt button row
        self.grid_rowconfigure(5, weight=0)  # Spacer between buttons
        self.grid_rowconfigure(6, weight=0)  # Decrypt button row
        self.grid_rowconfigure(7, weight=1)  # Bottom spacer
        self.grid_columnconfigure(0, weight=1)

        # Load and place the logo
        logo_image = Image.open("logo.png")
        self.logo = customtkinter.CTkImage(light_image=logo_image, dark_image=logo_image, size=(400, 400))
        logo_label = customtkinter.CTkLabel(self, image=self.logo, text="")
        logo_label.grid(row=1, column=0, pady=10, padx=20, sticky="n")  # Adjust as needed

        # Create and place a label in the frame
        label = customtkinter.CTkLabel(self, text="Welcome to Image Steganography App", font=("Arial", 28, "bold"))
        label.grid(row=2, column=0, pady=20, padx=20, sticky="ew")  # Place the label using grid

        # Create and place a button in the frame
        button = customtkinter.CTkButton(self, text="Encrypt", font=("Arial", 24, "bold"),
                                         command=self.encryptBtn_callback)
        button.grid(row=4, column=0, pady=15, padx=20, sticky="ew")  # Place the button using grid

        # Create and place a button in the frame
        button = customtkinter.CTkButton(self, text="Decrypt", font=("Arial", 24, "bold"),
                                         command=self.decryptBtn_callback)
        button.grid(row=6, column=0, pady=15, padx=20, sticky="ew")  # Place the button using grid

    # Action for encrypt button
    def encryptBtn_callback(self):
        self.master.show_encrypt_frame()  # Call the method in App to switch frames

    # Action for decrypt button
    def decryptBtn_callback(self):
        self.master.show_decrypt_frame()  # Call the method in App to switch frames


# Encrypt function page
class EncryptFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Fields
        self.oimage = None
        self.eimageMatrix = None
        self.maxLength = 0

        # Grid layout
        self.grid_columnconfigure(0, weight=1)
        # Top spacer
        self.grid_rowconfigure(0, weight=1)
        # Content rows
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
        self.grid_rowconfigure(7, weight=0)
        self.grid_rowconfigure(8, weight=0)
        self.grid_rowconfigure(9, weight=0)
        self.grid_rowconfigure(10, weight=0)
        self.grid_rowconfigure(11, weight=0)
        self.grid_rowconfigure(12, weight=0)
        # bottom spacer
        self.grid_rowconfigure(13, weight=1)

        # Create and place a "Home" button in the top-left corner
        home_button = customtkinter.CTkButton(self, text="Home", command=self.go_home)
        home_button.grid(row=0, column=0, pady=10, padx=10, sticky="nw")

        # Create and place an instructions label
        self.instructions_label = customtkinter.CTkLabel(self, text="Please open an image!", font=("Arial", 22, "bold"))
        self.instructions_label.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a label for message input
        label_message = customtkinter.CTkLabel(self, text="Message:", font=("Arial", 16, "bold"))
        label_message.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        # Create and place a text input field for message
        self.entry_message = customtkinter.CTkEntry(self, validate="key")
        self.entry_message.grid(row=4, column=0, pady=10, padx=20, sticky="ew")
        self.entry_message.bind("<KeyRelease>", lambda event: self.update_character_count())
        self.entry_message.configure(validatecommand=(self.register(self.validate_entry_length), '%P', '%W'))

        # Create and place a label for character count
        self.char_count_label = customtkinter.CTkLabel(self, text="0/0", font=("Arial", 14, "bold"))
        self.char_count_label.grid(row=5, column=0, pady=(0, 5), padx=20, sticky="e")

        # Create and place a label for security key input
        label_key = customtkinter.CTkLabel(self, text="Security Key:", font=("Arial", 16, "bold"))
        label_key.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        # Create and place a text input field for security key
        self.entry_key = customtkinter.CTkEntry(self)
        self.entry_key.grid(row=7, column=0, pady=10, padx=20, sticky="ew")
        self.entry_key.bind("<KeyRelease>", lambda event: self.update_encrypt_button_state())

        # Create and place a placeholder for the image
        self.image_placeholder = customtkinter.CTkLabel(self, text="No Image Selected", font=("Arial", 16))
        self.image_placeholder.grid(row=8, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a button to open an image file
        button_open_image = customtkinter.CTkButton(self, text="Open Image", command=self.open_image)
        button_open_image.grid(row=9, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a button to encrypt message
        self.button_encrypt = customtkinter.CTkButton(self, text="Encrypt", command=self.encrypt_callback)
        self.button_encrypt.grid(row=10, column=0, pady=10, padx=20, sticky="ew")

        self.update_encrypt_button_state()

    def validate_entry_length(self, P, W):
        if len(P) > self.maxLength:
            self.nametowidget(W).delete(self.maxLength, 'end')
            return False
        return True

    def encrypt_callback(self):
        self.eimageMatrix = encrypt(self.eimageMatrix, self.entry_key.get(), self.entry_message.get())
        # Simulate encryption logic and show success message
        self.show_success_message()

    def update_encrypt_button_state(self):
        if self.entry_message.get() and self.entry_key.get() and self.eimageMatrix is not None:
            self.button_encrypt.configure(state="normal")
            self.instructions_label.configure(text="Ready to encrypt!")
        elif self.eimageMatrix is not None:
            self.instructions_label.configure(text="Please enter message and security key!")
        else:
            self.button_encrypt.configure(state="disabled")
            self.instructions_label.configure(text="Please open an image!")

    def update_character_count(self):
        current_length = len(self.entry_message.get())
        self.char_count_label.configure(text=f"{current_length}/{self.maxLength}")

    def show_success_message(self):
        # Create a label to show success message (initially hidden)
        self.success_message_label = customtkinter.CTkLabel(self, text="Successfully encrypted message!",
                                                            font=("Arial", 18, "bold"), text_color="green")
        self.success_message_label.grid(row=11, column=0, pady=10, padx=10, sticky="ew")

        # Create and place a button to view encrypted image
        self.button_viewEI = customtkinter.CTkButton(self, text="View encrypted image", command=self.viewEI_callback)
        self.button_viewEI.grid(row=12, column=0, pady=10, padx=20, sticky="ew")

    def viewEI_callback(self):
        self.master.show_viewEI_frame(self.entry_message.get(), self.entry_key.get(), self.oimage, self.eimageMatrix)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.processImage(file_path)
            image = Image.open(file_path)
            image.thumbnail((300, 300))  # Resize image to fit the placeholder
            self.oimage = customtkinter.CTkImage(light_image=image, dark_image=image, size=(300, 300))
            self.image_placeholder.configure(image=self.oimage, text="")
            self.update_encrypt_button_state()

    def processImage(self, file_path):
        self.eimageMatrix = getMatrix(file_path)
        self.maxLength = getMaxLength(self.eimageMatrix)
        self.update_character_count()

    def go_home(self):
        # Logic to go back to home screen (could be showing the welcome frame)
        self.master.show_welcome_frame()  # Assuming you have a method to show the welcome frame


# View encrypted image page
class ViewEIFrame(customtkinter.CTkFrame):
    def __init__(self, master, message, key, oimage, eimageMatrix):
        super().__init__(master)

        self.message = message
        self.key = key
        self.oimage = oimage
        self.eimageMatrix = eimageMatrix

        # Grid layout
        self.grid_columnconfigure((0, 1), weight=1)
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
        self.oimage_label = customtkinter.CTkLabel(self, image=self.oimage, text="")
        self.oimage_label.grid(row=4, column=0, pady=10, padx=20, sticky="ew")

        # Convert eimageMatrix to CTkImage for display
        self.eimage = self.convert_cv2_to_ctkimage(self.eimageMatrix)
        self.eimage_label = customtkinter.CTkLabel(self, image=self.eimage, text="")
        self.eimage_label.grid(row=4, column=1, pady=10, padx=20, sticky="ew")

        # Button to save the encrypted image
        button_save_image = customtkinter.CTkButton(self, text="Save Encrypted Image", command=self.save_image)
        button_save_image.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

        # Label to display success message (initially hidden)
        self.success_message_label = customtkinter.CTkLabel(self, text="", font=("Arial", 16, "bold"),
                                                            text_color="green")
        self.success_message_label.grid(row=6, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

    def convert_cv2_to_ctkimage(self, cv2_image):
        # Convert the OpenCV image from BGR to RGB
        rgb_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
        # Convert the RGB image to a PIL image
        pil_image = Image.fromarray(rgb_image)
        pil_image.thumbnail((300, 300))  # Resize image to fit the placeholder
        # Convert the PIL image to a CTkImage
        ctk_image = customtkinter.CTkImage(light_image=pil_image, dark_image=pil_image, size=(300, 300))
        return ctk_image

    def go_home(self):
        # Logic to go back to home screen (could be showing the welcome frame)
        self.master.show_welcome_frame()  # Assuming you have a method to show the welcome frame

    def save_image(self):
        # Ask user to select a file location to save the image
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            # Save the encrypted image using OpenCV
            cv2.imwrite(file_path, self.eimageMatrix)
            # Show success message
            self.success_message_label.configure(text=f"Encrypted image saved at: {file_path}")
            # print(f"Encrypted image saved at: {file_path}")


# Decrypt frame
class DecryptFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Fields
        self.image_path = None
        self.decrypted_message = None
        self.oimage = None  # This will store the image in CTkImage format
        self.imageMatrix = None

        # Grid layout
        self.grid_columnconfigure(0, weight=1)
        # Top spacer
        self.grid_rowconfigure(0, weight=1)
        # Content rows
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
        self.grid_rowconfigure(7, weight=0)
        self.grid_rowconfigure(8, weight=0)
        self.grid_rowconfigure(9, weight=0)
        # bottom spacer
        self.grid_rowconfigure(10, weight=1)

        # Create and place a "Home" button in the top-left corner
        home_button = customtkinter.CTkButton(self, text="Home", command=self.go_home)
        home_button.grid(row=0, column=0, pady=10, padx=10, sticky="nw")

        # Create and place an instructions label
        self.instructions_label = customtkinter.CTkLabel(self, text="Please open the encrypted image!",
                                                         font=("Arial", 22, "bold"))
        self.instructions_label.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a label for security key input
        label_key = customtkinter.CTkLabel(self, text="Security Key:", font=("Arial", 18, "bold"))
        label_key.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        # Create and place a text input field for security key
        self.entry_key = customtkinter.CTkEntry(self)
        self.entry_key.grid(row=4, column=0, pady=10, padx=20, sticky="ew")
        self.entry_key.bind("<KeyRelease>", lambda event: self.update_decrypt_button_state())

        # Create a label to display the image (initially hidden)
        self.image_placeholder = customtkinter.CTkLabel(self, text="No image selected")
        self.image_placeholder.grid(row=5, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a button to open an image file
        button_open_image = customtkinter.CTkButton(self, text="Open Encrypted Image", command=self.open_image)
        button_open_image.grid(row=6, column=0, pady=10, padx=20, sticky="ew")

        # Create and place a button to decrypt message
        self.button_decrypt = customtkinter.CTkButton(self, text="Decrypt", command=self.decrypt_callback)
        self.button_decrypt.grid(row=7, column=0, pady=10, padx=20, sticky="ew")
        self.button_decrypt.configure(state="disabled")

        # Create and place a label to display the decrypted message (initially hidden)
        self.label_decrypted_message = customtkinter.CTkLabel(self, text="", font=("Arial", 22, "bold"),
                                                              text_color="green")
        self.label_decrypted_message.grid(row=8, column=0, pady=10, padx=20, sticky="ew")

    def go_home(self):
        # Logic to go back to home screen (could be showing the welcome frame)
        self.master.show_welcome_frame()  # Assuming you have a method to show the welcome frame

    def open_image(self):
        # Open the image file (only .png)
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)
            self.update_decrypt_button_state()
            print(f"Image loaded: {file_path}")

    def display_image(self, file_path):
        # Use PIL to open and resize the image for display in the UI
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # Resize image to fit the label
        self.oimage = customtkinter.CTkImage(light_image=image, dark_image=image, size=(300, 300))
        self.image_placeholder.configure(image=self.oimage, text="")
        # self.image_placeholder.image = self.oimage  # Keep a reference to avoid garbage collection

    def decrypt_callback(self):
        # Get the security key entered by the user
        key = self.entry_key.get()

        if self.image_path and key:
            # Perform decryption (this is just a placeholder for your actual decryption algorithm)
            decrypted_message = self.decrypt_message(key)

            # Display the decrypted message
            self.label_decrypted_message.configure(text=f"Secret Message: {decrypted_message}")

    def decrypt_message(self, key):
        self.imageMatrix = getMatrix(self.image_path)
        # Example decryption logic (you should replace this with your actual decryption algorithm)
        # decrypted_message = "This is a decrypted message"  # Replace with actual decrypted data
        self.decrypted_message = decrypt(self.imageMatrix, key)
        return self.decrypted_message

    def update_decrypt_button_state(self):
        if self.image_path and self.entry_key.get():
            self.button_decrypt.configure(state="normal")
            self.instructions_label.configure(text="Ready to decrypt!")
        else:
            self.button_decrypt.configure(state="disabled")
            self.instructions_label.configure(text="Please enter security key!")


# Main app window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Image Steganography")
        self.geometry("1100x900")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.welcome_frame = WelcomeFrame(self)
        self.welcome_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

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
        self.viewEI_frame = ViewEIFrame(self, message, key, oimage, eimageMatrix)
        self.viewEI_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Render decrypt function page
    def show_decrypt_frame(self):
        self.welcome_frame.grid_forget()
        self.decrypt_frame = DecryptFrame(self)
        self.decrypt_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Go back to home page
    def show_welcome_frame(self):
        if self.encrypt_frame is not None:
            self.encrypt_frame.destroy()
        if self.decrypt_frame is not None:
            self.decrypt_frame.destroy()
        if self.viewEI_frame is not None:
            self.viewEI_frame.destroy()
        self.welcome_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

app = App()
app.mainloop()
