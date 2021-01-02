import pyqrcode as df
import png

inpp = 'Msg Inside QR Code'
a = df.create(inpp)
nam = input('Enter Name Of File To Save: ')
a.png(nam+'.png')
print('QR Code Generated Successfully')