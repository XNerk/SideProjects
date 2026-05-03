# The shift key is set here
key = 3
mode1 = 1

def mode(bool1):
    if bool1==0:
        return "Decipher"
    elif bool1==1:
        return "Cipher"
    print("the current mode is hahah:", mode1)
    
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetic characters as they are
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    # Deciphering is just shifting in the opposite direction
    return caesar_cipher(text, -shift)

print(f"\n---XNerk's Caesar Cipher Tool (Default Key: {key}) ---")
print("Type your message and press Enter.")
print("'exit'      - quit.")
print("'cha_key12' - change cipher key.") 
print("'mode_1'    - switch between cipher and decipher.") 


while True:
    print(" \nCurrent mode:",mode(mode1))
    user_input = input("\nEnter message: ")

    
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    elif user_input.lower() =='cha_key12':
        key = int(input("Enter the new key:"))
        continue
    elif user_input.lower()=='mode_1':
        mode1=int(input("Enter  0 - Decipher,  1 - Cipher: "))
        continue
    else:
        if mode1==1:
            encrypted_text = caesar_cipher(user_input, key)
            print(f"Ciphertext: {encrypted_text}")
        elif mode1==0:
            decrypted_text = caesar_decipher(user_input, key)
            print(f"deciphertext: {decrypted_text}")

        
        
        
 
