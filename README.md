# Image Steganography Application

This Python application enables image-based **steganography**, allowing users to encrypt a secret message into an image using a **security key**. The encrypted message is hidden within the image pixels and can be retrieved later using the same key.

## Features

- Encrypt a secret message into an image.
- Use a custom **security key** to encrypt and decrypt the message.
- Open, select, and manipulate images in formats like `.png`, `.jpg`, `.jpeg`.
- Show encrypted image with the hidden message using the decryption feature.
- Save the encrypted image as `.png` after the message is encoded.

## Requirements

Before running the application, ensure that the following libraries are installed:

- Python 3.x
- `customtkinter`: For the graphical user interface (GUI)
- `Pillow`: To manipulate images
- `cv2`: For handling image processing tasks (used in getting image matrix for encrypt and decrypt)

### Install dependencies:

You can install the required libraries using **pip**:

```bash
pip install customtkinter Pillow opencv-python
```

## How to Use

1. **Run the Application:**
   - Execute the Python script to launch the application.

2. **Encrypting a Message:**
   - Select the "Encrypt" mode.
   - Upload an image of your choice (PNG, JPEG, JPG).
   - Enter the **secret message** you wish to hide inside the image.
   - Set a **security key** that will be used to encrypt and decrypt the message.
   - Click "Encrypt" to hide the message in the image.
   - You can view the encrypted image.

3. **Decrypting a Message:**
   - Select the "Decrypt" mode.
   - Upload the encrypted image.
   - Enter the **security key** that was used to encrypt the image.
   - The secret message will be revealed after decryption.

4. **Save Encrypted Image:**
   - After encryption, the application will provide an option to save the image with the hidden message.
   - You can save the image in **.png** format.


## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for more details.
