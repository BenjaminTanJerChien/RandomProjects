#qr code endcoder and decoder 
import qrcode as qr
from PIL import Image
#from pyzbar.pyzbar import decode


action = input("Encode / Decode ? ")

if action == "Encode":
    data = input("QR text / data: ")
    filename = input("Filename: ")
    img = qr.make(data)
    img.save(f"C:/Users/jerch/Pictures/QR codes/{filename}.png")
    print(img)

'''else:
    img = input("Filepath: ")
    img = Image.open(img)
    result = decode(img)
    print(result)'''
