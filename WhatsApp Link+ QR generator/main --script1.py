import time
#direct whatsapp contact creator no need to save contact,, :)

contact_no=int(input('enter valid mobile number here,*put country code also in beginning of it*'))
x=str(contact_no)
if len(x)==10:
    print("you didn't entered valid number,maybe you forgot to enter country code")
elif len(x)==12:
    print('genrating link...')
    time.sleep(1.5)
    print('open whatsapp web and just click link below')
    print('https://wa.me/',contact_no,sep='')
    time.sleep(2)
else:
    None