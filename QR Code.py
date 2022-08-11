import qrcode


qr = qrcode.QRCode(version =2,
                   box_size = 20,
                   border = 5)

img = qrcode.make("Ate")
img.save("New.jpg")