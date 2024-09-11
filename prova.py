#some_bytes = b'\xC3\xA9'

with open("pitone.jpeg", "rb") as binary_file:
    file =binary_file.read()


import binascii
Ascii = binascii.b2a_base64(file)
print(Ascii)


