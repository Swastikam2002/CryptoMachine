# Create the encryption dictionary
encryption_dict = {
    'A': 'QW!',
    'B': 'ER@',
    'C': 'TY#',
    'D': 'UI$',
    'E': 'OP%',
    'F': 'AS^',
    'G': 'DF&',
    'H': 'GH*',
    'I': 'JK~',
    'J': 'LZ!',
    'K': 'XC#',
    'L': 'VN$',
    'M': 'BQ%',
    'N': 'WE^',
    'O': 'RT&',
    'P': 'YU*',
    'Q': 'IO~',
    'R': 'PA!',
    'S': 'SD@',
    'T': 'FG#',
    'U': 'HJ$',
    'V': 'KL%',
    'W': 'ZX^',
    'X': 'CV&',
    'Y': 'NB*',
    'Z': 'MK~',
    ' ': 'QWE',
    ',': 'ASD',
    '.': 'ZXC',
    '?': 'IOP',
    '!': 'JKL',
    '/': 'BNM',
    '1': 'HGH',
    '2': 'KOK',
    '3': 'FGF',
    '4': 'TYT',
    '5': 'OKO',
    '6': 'NVN',
    '7': 'SDS',
    '8': 'ERE',
    '9': 'XCX',
    '0': 'CIC',
}

decryption_dict = {}
for keys, values in encryption_dict.items():
    for i in range(0, len(values), 3):
        decryption_dict[values[i:i+3]] = keys

# user input
message = input("Enter your secret message: ")
message = message.upper()
mode = input("Crypto Mode : Encode(E) OR Decode(D): ")

#encode and decode
if mode.upper() == 'E':
    key = input("Enter a 4 digit key (remember key while decrypting): ")
    newMessage = ''.join([encryption_dict[letter] if letter in encryption_dict else letter for letter in message])
    providedKey = ''.join([encryption_dict[k] for k in key])
    finalMessage = newMessage + providedKey
    print(finalMessage.capitalize())

elif mode.upper() == 'D':
     key = input("Enter 4 digit key: ")
     correctKey = ''
     n=12
     while n>0:
       correctKey += message[-n]
       n=n-1
     finalKey = ''.join([decryption_dict[correctKey[i:i+3]] for i in range(0, len(correctKey), 3)])
     if finalKey == key:
       finalMessage = ''.join([decryption_dict[message[i:i+3]] if message[i] not in ';:<>~!@#$%^&*(){}[]-_+=' else message[i] for i in range(0, len(message)-12, 3)])
       print(finalMessage.capitalize())
     else:
        print("Sorry! Key does not match")

else:
    print("Please try again, wrong choice entered")