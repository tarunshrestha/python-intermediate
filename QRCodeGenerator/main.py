import qrcode as Q

data = input('Enter the Link: ')
name = input('Enter the QR name:')
img = Q.make(data)

img.save(f'{name}.png')
