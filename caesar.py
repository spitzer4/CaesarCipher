def caesar_encrypt(message, shift):
    encrypted = ""
    for i in range(len(message)):
        c = message[i]
        if c.isupper():
            encrypted += chr((ord(c) + shift-65) % 26 + 65)
        else:
            encrypted += chr((ord(c) + shift - 97) % 26 + 97)

    return encrypted

message = "Hello World!"
shift = 2

print("Message: " + message)
print("Shift by: " + str(shift))
print("Cipher: " + caesar_encrypt(message, shift))