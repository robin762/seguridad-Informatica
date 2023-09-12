#Robinson Rojas
#Desafio 2

import json
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
            n = ord(key[i % key_length].lower()) - ord('a')
            is_lowercase = char.islower()
            char_code = ord(char)
            base = ord('a') if is_lowercase else ord('A')
            decrypted_char = chr(((char_code - base - n) % 26) + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

headers = {
    'Content-Type': 'text/plain',
}

response = requests.get('http://finis.malba.cl/GetMsg', headers=headers)
msg_import = json.loads(response.text)

texto_decifrar = msg_import['msg']

clave_vigenere = 'aobkqolrzsrigpknkufezioer'

# Decifrar con rot -7
mensaje_root = rot(texto_decifrar, -7)
print("mensaje root: ", mensaje_root)

# Decifrar Vigenere
mensaje_vigenere = desencriptar(mensaje_root, clave_vigenere)
print("mensaje vigenere:", mensaje_vigenere)

# Decifrar con rot -15
mensaje_desencriptado = rot(mensaje_vigenere, -15)
print("texto desencriptado: ", mensaje_desencriptado)
