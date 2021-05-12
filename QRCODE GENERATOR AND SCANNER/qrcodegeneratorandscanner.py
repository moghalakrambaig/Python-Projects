import qrcode
# from pyzbar.pyzbar import decode
# from PIL import Image

qr = qrcode.make("Hey how r u This is akram")
qr.save("qrcode.png",scale=10)