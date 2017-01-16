import string
import structure


def ReplaceChooseOne(key):
    c = ''
    d = ''
    for i in range(0, 28):
        c = c + key[structure.C0[i] - 1]
        d = d + key[structure.D0[i] - 1]
    return c + d


def ReplaceChooseTwo(c, d):
    tmp = c + d
    subKey = ''
    for i in range(0, 48):
        subKey = subKey + tmp[structure.PC[i] - 1]
    return subKey


def MoveLeft(key, i):
    newKey = key[structure.LEFT[i]:] + key[:structure.LEFT[i]]
    #print 'i=', structure.LEFT[i]
    return newKey


def SubKeyGenerator(key):
    if len(key) != 64:
        print('The key is invalid. Please try again.')
        exit()
    else:
        subKeySet = []
        key = ReplaceChooseOne(key)
        c = key[0: 28]
        d = key[28: 56]
        for i in range(0, 16):
            c = MoveLeft(c, i)
            d = MoveLeft(d, i)
            #print (c, d)
            subKeySet.append(ReplaceChooseTwo(c, d))
        return subKeySet

# =============================================================================


def ChoiceExpand(data):
    new_data = ''
    for i in range(0, 48):
        new_data = new_data + data[structure.E[i] - 1]
    return new_data


def ChoiceShrink(data):
    new_data = ''
    for i in range(0, 32):
        new_data = new_data + data[structure.P[i] - 1]
    return new_data


def SChange(data, i):
    row = int(data[1: 5], 2)
    line = int(data[0] + data[5], 2)
    new_data = str(bin(structure.S[int(i / 6)][line][row]).replace('0b', ''))
    return new_data.zfill(4)



def EncryptFunction(data, subKey):
    if len(data) != 32:
        print('In Encrypt Function, the data input is invalid.')
        exit()
    else:
        data = ChoiceExpand(data)
        data = bin(int(data, 2) ^ int(subKey, 2)).replace('0b', '').zfill(48)
        new_data = ''
        for i in range(0, 48, 6):
            new_data = new_data + SChange(data[i: i + 6], i)
        new_data = ChoiceShrink(new_data)
        return new_data


def InitIP(data):
    new_data = ''
    for i in range(0, 64):
        new_data = new_data + data[structure.IP[i] - 1]
    return new_data


def ReverseIP(data):
    new_data = ''
    for i in range(0, 64):
        new_data = new_data + data[structure.IP_1[i] - 1]
    return new_data


def DESencrypt(text, key):
    if len(text) != 64 or len(key) != 64:
        print('Invalid Input')
        exit()
    else:
        subKey = SubKeyGenerator(key)
        text = InitIP(text)
        l = text[0 :32]
        r = text[32: 64]
        for i in range(0, 15):
            new_l = r
            new_r = bin(int(EncryptFunction(r, subKey[i]), 2) ^ int(l, 2)).replace('0b', '').zfill(32)
            l = new_l
            r = new_r
        new_l = r
        new_r = bin(int(EncryptFunction(r, subKey[15]), 2) ^ int(l, 2)).replace('0b', '').zfill(32)
        secret = ReverseIP(new_r + new_l)
        return secret


def DESdecrypt(secret, key):
    subKey = SubKeyGenerator(key)
    subKey.reverse()
    secret = InitIP(secret)
    l = secret[0:32]
    r = secret[32: 64]
    for i in range(0, 15):
        new_l = r
        new_r = bin(int(EncryptFunction(r, subKey[i]), 2) ^ int(l, 2)).replace('0b', '').zfill(32)
        l = new_l
        r = new_r
    new_l = r
    new_r = bin(int(EncryptFunction(r, subKey[15]), 2) ^ int(l, 2)).replace('0b', '').zfill(32)
    text = ReverseIP(new_r + new_l)
    return text


def ThreeDESencrypt(text, key):
    k1 = key[: 64]
    k2 = key[64:]
    return DESencrypt(DESdecrypt(DESencrypt(text, k1), k2), k1)


def ThreeDESdecrypt(secret, key):
    k1 = key[: 64]
    k2 = key[64:]
    return DESdecrypt(DESencrypt(DESdecrypt(secret, k1), k2), k1)

'''
def main():
    #text = '0011000000110001001100100011001100110100001101010011011000110111'
    #key = '0011000100110010001100110011010000110101001101100011011100111000'
    #secret = '1000101110110100011110100000110011110000101010010110001001101101'
    #print DESencrypt(text, key)
    #print DESdecrypt(secret, key)
    text = '0011000000110001001100100011001100110100001101010011011000110111'
    key = '00110001001100100011001100110100001101010011011000110111001110001000101110110100011110100000110011110000101010010110001001101101'
    secret = '1100011110110111110101010010000011111110011101101100111010001101'
    #print ThreeDESencrypt(text, key)
    print ThreeDESdecrypt(secret, key)


if __name__ == '__main__':
    main()
'''