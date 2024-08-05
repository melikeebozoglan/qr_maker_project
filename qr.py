import qrcode

code = qrcode.QRCode(
	version = 1,
	error_correction = qrcode.constants.ERROR_CORRECT_L,
	box_size = 8,
	border = 4, 
)

code.add_data('https://melikesultanbozoglan.onrender.com')
code.make(fit = True)

image = code.make_image(fill_color = "black", back_color = "white")
image.save('./qr.png')