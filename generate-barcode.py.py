from pdf417 import encode, render_image

# FULL AAMVA FORMAT DRIVER LICENSE DATA (REALISTIC STRUCTURE)
data = """
@
ANSI 636026080102DL00410288ZA03290015DLDAQF236180520600
DCSDONALD
DACFOSTER
DAD
DBD20250220
DBB19520220
DBA20300220
DBC1
DAU180
DAYBRO
DAZ150 lb
DAG2900 SW 127TH AVE
DAIMIAMI
DAJFL
DAK33165
DCF12345678901234567890
DCGUSA
DCHClass D
DCLNONE
DCIUSA
DCJNONE
DCK12345678900000000000
DDB20250220
DDCFL
DDD20200220
"""

# Generate barcode
codes = encode(data.strip(), columns=6, security_level=5)

# Render to image
img = render_image(codes, scale=3, ratio=3, padding=10)

# Save the image
img.save("driver_license_barcode.png")

print("✅ Barcode saved as 'driver_license_barcode.png'")
