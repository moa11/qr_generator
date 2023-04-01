import qrcode
import location_cython


def encod_data(lati, lon):
    lati = location_cython.from_float2char2(lati)
    lon = location_cython.from_float2char2(lon)
    return lati + lon


def make_qr(encode_data, name: str):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(encode_data)
    qr.make(fit=True)

    # Save the QR code image as a PNG file
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("{}.png".format(name))
    return img


def decode_data(qrcodes):
    data_enc = qrcodes[0].data.decode("utf8")
    decoded_lat = bytes(list(map(ord, data_enc[:8])))
    decoded_lon = bytes(list(map(ord, data_enc[8:])))

    lat = location_cython.from_char2flaot(decoded_lat)
    lon = location_cython.from_char2flaot(decoded_lon)
    return lat, lon
