# simple qr code generator

# import qrcode
# qr = qrcode.make('https://bmaithya.vercel.app')
# qr.show()


#advanced qr code generator

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://bmaithya.vercel.app')
qr.make(fit=True)

img = qr.make_image(fill_color="purple", back_color="white")

img.show()