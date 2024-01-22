import random
import PIL
import qrcode
from qrcode.image.pure import PyPNGImage

#this is enhanced version of python_day5 project :))

var_4=''
var_5=''
for i in range(0,3):
    x=random.randint(0,255)
    y=random.randint(0,255)
    # Convert to hexadecimal and pad with zeros if needed
    color1 = '{:02x}'.format(x)
    color2 = '{:02x}'.format(y)
    var_4+=color1
    var_5+=255-x

contact_no = int(input('enter valid mobile number here,*put country code also in beginning of it*'))
x = str(contact_no)
if len(x) == 12:
    contact_link = qrcode.QRCode(version=None, box_size=10, border=4)
    contact_link_data = 'https://wa.me/' + x
    contact_link.add_data(contact_link_data)
    contact_link.make(fit=True)
    img = contact_link.make_image(fill_color=('#'+var_4), back_color=('#'+var_5))
    img.save('qrcode' + 'code'+str(random.randint(0,100)) + '.png')


elif len(x) == 10 or len(x) != 12:
    print("you didn't entered valid number,maybe you forgot to enter country code")

print('thanks :)),everybody,,sayonara')

