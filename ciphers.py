# ----------------------Index Sub Cipher----------------------
def encryptIndexSubstitutionCipher(text):
    result = ''
    for i in range(0, len(text)):
        if i != len(text) - 1:
            if ord(text[i]) - 96 < 10:
                result = result + '0' + str(ord(text[i]) - 96) + ' '
            else:
                result = result + str(ord(text[i]) - 96) + ' '
        else:
            if ord(text[i]) - 96 < 10:
                result = result + '0' + str(ord(text[i]) - 96)
            else:
                result = result + str(ord(text[i]) - 96)
    return result


def decryptIndexSubstitutionCipher(text):
    result = ''
    print(text.split(' '))
    for i in text.split(' '):
        result = result + chr(int(i) + 96)

    return result


# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}


def encryptMorseCode(text):
    result = ''
    for i in range(0, len(text)):
        for j in morseCode:
            if text[i] == j:
                if i != len(text) - 1:
                    result = result + morseCode[j] + ' '
                else:
                    result = result + morseCode[j]
    return result


def decryptMorseCode(text):
    result = ''
    for i in text.split(' '):
        for j in morseCode:
            if i == morseCode[j]:
                result = result + j
    return result


# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    orderedText = encryptIndexSubstitutionCipher(text)
    txt = ''
    for i in orderedText.split(' '):
        txt = txt + chr(((a * (int(i) - 1) + b) % 26) + 97)
    return txt


def decryptAffineCipher(text, a, b):
    orderedText = encryptIndexSubstitutionCipher(text)
    result = ''
    for i in orderedText.split(' '):
        result = result + chr((pow(a, -1, 26) * (int(i) - 1 - b)) % 26 + 97)
    return result


# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    result = ''

    for i in range(len(text)):
        if i % 2 == 0:
            if 48 <= ord(text[i]) <= 57:
                if ord(text[i]) + key1 % 10 > 57:
                    result += chr(47 + (ord(text[i]) + key1 % 10 - 57))
                else:
                    result += chr(ord(text[i]) + key1 % 10)
            elif 65 <= ord(text[i]) <= 90:
                if ord(text[i]) + key1 % 26 > 90:
                    result += chr(64 + (ord(text[i]) + key1 % 26 - 90))
                else:
                    result += chr(ord(text[i]) + key1 % 26)
            elif 97 <= ord(text[i]) <= 122:
                if ord(text[i]) + key1 % 26 > 122:
                    result += chr(96 + (ord(text[i]) + key1 % 26 - 122))
                else:
                    result += chr(ord(text[i]) + key1 % 26)
            else:
                result += text[i]
        else:
            if 48 <= ord(text[i]) <= 57:
                if ord(text[i]) + key2 % 10 > 57:
                    result += chr(47 + (ord(text[i]) + key2 % 10 - 57))
                else:
                    result += chr(ord(text[i]) + key2 % 10)
            elif 65 <= ord(text[i]) <= 90:
                if ord(text[i]) + key2 % 26 > 90:
                    result += chr(64 + (ord(text[i]) + key2 % 26 - 90))
                else:
                    result += chr(ord(text[i]) + key2 % 26)
            elif 97 <= ord(text[i]) <= 122:
                if ord(text[i]) + key2 % 26 > 122:
                    result += chr(96 + (ord(text[i]) + key2 % 26 - 122))
                else:
                    result += chr(ord(text[i]) + key2 % 26)
            else:
                result += text[i]

    return result


def decryptCaesarCipher(text, key1, key2):
    result = ''

    for i in range(len(text)):
        if i % 2 == 0:
            if 48 <= ord(text[i]) <= 57:
                if ord(text[i]) - key1 % 10 < 48:
                    result += chr(58 - (48 - (ord(text[i]) - key1 % 10)))
                else:
                    result += chr(ord(text[i]) - key1 % 10)
            elif 65 <= ord(text[i]) <= 90:
                if ord(text[i]) - key1 % 26 < 65:
                    result += chr(91 - (65 - (ord(text[i]) - key1 % 26)))
                else:
                    result += chr(ord(text[i]) - key1 % 26)
            elif 97 <= ord(text[i]) <= 122:
                if ord(text[i]) - key1 % 26 < 97:
                    result += chr(123 - (97 - (ord(text[i]) - key1 % 26)))
                else:
                    result += chr(ord(text[i]) - key1 % 26)
            else:
                result += text[i]
        else:
            if 48 <= ord(text[i]) <= 57:
                if ord(text[i]) - key2 % 10 < 48:
                    result += chr(58 - (48 - (ord(text[i]) - key2 % 10)))
                else:
                    result += chr(ord(text[i]) - key2 % 10)
            elif 65 <= ord(text[i]) <= 90:
                if ord(text[i]) - key2 % 26 < 65:
                    result += chr(91 - (65 - (ord(text[i]) - key2 % 26)))
                else:
                    result += chr(ord(text[i]) - key2 % 26)
            elif 97 <= ord(text[i]) <= 122:
                if ord(text[i]) - key2 % 26 < 97:
                    result += chr(123 - (97 - (ord(text[i]) - key2 % 26)))
                else:
                    result += chr(ord(text[i]) - key2 % 26)
            else:
                result += text[i]

    return result


# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    result = ''

    for i in range(0, key):
        for j in range(i, len(text), key):
            result += text[j]
    return result


def decryptTranspositionCipher(text, key):
    result = ''

    length = len(text)
    remaining = length % key
    jump = int(length / key)

    for i in range(jump):
        for j in range(i, (jump + 1) * (remaining + 1), jump + 1):
            result += text[j]

        for j in range(i + remaining * (jump + 1) + jump, length, jump):
            result += text[j]

    for i in range(0, len(text) % key):
        result += text[i * (jump + 1) + jump]

    return result


print(decryptTranspositionCipher('Ch oai 1!iePgmn-0prrrmg 1', 3))
print(decryptTranspositionCipher('adgbehcf', 3))
print(decryptTranspositionCipher('alpep', 3))
print(decryptTranspositionCipher('ALPEP', 3))
print(decryptTranspositionCipher('14253', 3))
