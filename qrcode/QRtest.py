import qrcode
img = qrcode.make('kenji yamakawa')
type(img)  # qrcode.image.pil.PilImage
img.save("qrcodetest.png")