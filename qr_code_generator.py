import qrcode
url = "https://preview--warsaw-coder-adventures.lovable.app/"
qr = qrcode.make(url)
qr.save("site_qr_kode.png")
