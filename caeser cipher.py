alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, shift):
    cipher_text=""
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position + shift) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print("The encrypted text is: \n" + cipher_text)
def decrypt(text, shift):
    plain_text=""
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position - shift) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text  +=  char
    print("The decrypted text is: \n" + plain_text)
text = input("Enter your text: \n")
shift = int(input("Enter shift value: \n"))
action = input("Encrypt or Decrypt: \n")

if action == "encrypt":
    encrypt(text, shift)
elif action == "decrypt":
    decrypt(text, shift)
else:
    print("Invalid action. Please choose 'Encrypt' or 'Decrypt'.")