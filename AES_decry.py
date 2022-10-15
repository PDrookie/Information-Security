from Crypto.Cipher import AES
import base64



def decry(key):
    cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
    plain_text = cipher.decrypt(base64.b64decode("1ㄌ6zvA3lnMuWHoE5PpaJheQ==")).rstrip(b"\0").decode("utf8")
    return plain_text

key = "s{}hv{}4z*{}7d*t{}Ce"

key_texts = '''!"#$%&\\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''

temp = 0
total = 81450625

ans = []


for key_text1 in key_texts:
    for key_text2 in key_texts:
        for key_text3 in key_texts:
            for key_text4 in key_texts:
                try:
                    temp += 1
                    print('\r' + '[Progress]:[%s%s]%.2f%%;' % (
                    '█' * int(temp*20/total), ' ' * (20-int(temp*20/total)),
                    float(temp/total*100)), end='')
                    plain = decry(key.format(key_text1,key_text2,key_text3,key_text4))
                    if "Ho" in plain:
                        ans.append((plain, key.format(key_text1,key_text2,key_text3,key_text4)))
                except:
                    pass
print(ans)