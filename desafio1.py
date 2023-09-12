#Robinson Rojas
#Desafio 1

import requests

def rot(text, n):
    result = ""
    for char in text:
        if char.isalpha():
            is_lowercase = char.islower()
            char_code = ord(char)
            base = ord('a') if is_lowercase else ord('A')
            shifted_char = chr(((char_code - base + n) % 26) + base)
            result += shifted_char
        else:
            result += char
    return result

def desencriptar(text, key):
    key_length = len(key)
    decrypted_text = ""
    for i, char in enumerate(text):
        if char.isalpha():
            is_lowercase = char.islower()
            n = ord(key[i % key_length].lower()) - ord('a')
            char_code = ord(char)
            base = ord('a') if is_lowercase else ord('A')
            decrypted_char = chr(((char_code - base - n) % 26) + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def encriptar(text, key):
    key_length = len(key)
    encrypted_text = ""
    for i, char in enumerate(text):
        if char.isalpha():
            is_lowercase = char.islower()
            n = ord(key[i % key_length].lower()) - ord('a')
            char_code = ord(char)
            base = ord('a') if is_lowercase else ord('A')
            encrypted_char = chr(((char_code - base + n) % 26) + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Mensaje cifrado
mensaje_cifrado = "nose que poner"
# Aplicar rot 15
mensaje_rot = rot(mensaje_cifrado, 15)
# Clave Vigenere
clave_vigenere = "cvqnoteshrwnszhhksorbqcoas"
# Descifrar Vigenere
mensaje_descifrado = desencriptar(mensaje_rot, clave_vigenere)
# Aplicar rot -7
mensaje_final = rot(mensaje_descifrado, -7)

headers = {
    'Content-Type': 'text/plain',
}

data = '{"msg":"' + mensaje_final + '"}'

response = requests.post('http://finis.malba.cl/SendMsg', headers=headers, data=data)

print(response.text)

# PROCESO DE DECRIFRADO

# Aplicar rot  7
mensaje_final = rot(mensaje_final, 7)

# Aplicar Vigenere
mensaje_final = encriptar(mensaje_final, clave_vigenere)

# Aplicar rot -15
mensaje_final = rot(mensaje_final, -15)

print("mensaje desencriptado: ", mensaje_final)
