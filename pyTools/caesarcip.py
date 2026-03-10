# The shift key is set here
key = 3

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

print(f"\n---XNerk's Caesar Cipher Tool (Default Key: {key}) ---")
print("Type your message and press Enter. Type 'exit' to quit. Type 'cha_key12' to change key.")

while True:
    user_input = input("\nEnter message: ")
    
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    elif user_input.lower() =='cha_key12':
        key = int(input("Enter the new key:"))
        continue
    else:
        encrypted_text = caesar_cipher(user_input, key)
        print(f"Ciphertext: {encrypted_text}")
        
        
 
