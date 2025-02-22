import qrcode

# Create an instance of QRCode
qr_code = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 = 21x21 matrix)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Border thickness (default is 4)
)

# Add data to the QR code
qr_code.add_data("Hello world")
qr_code.make(fit=True)

# Create an image from the QR code
img = qr_code.make_image(fill="black", back_color="white")
img.save("qrcode/hello.png")

print("QR code saved as hello.png")
