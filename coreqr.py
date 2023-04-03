import qrcode
import cypthon_file.location_cython as location_cython


def encod_data(lati,lon,ori):
    lati =  location_cython.from_float2char2(lati)
    lon =  location_cython.from_float2char2(lon)
    if ori >0 :
        ori = ori.to_bytes(1, 'little',signed="False")
        print(ori)
    else :
        ori = ori.to_bytes(1, 'little',signed="True")
        print(ori)
    return lati+lon+ori


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


def decode_data(decoded_lat,decoded_lon,decoded_ori):
    lat=location_cython.from_char2flaot(decoded_lat)
    lon=location_cython.from_char2flaot(decoded_lon)
    ori=int.from_bytes(decoded_ori, 'little',signed="true")
    return lat,lon,ori

def get_data(qrcodes):
    data_enc=qrcodes[0].data.decode('utf8')
    decoded_lat = bytes(list(map(ord,data_enc[:8])))
    decoded_lon = bytes(list(map(ord,data_enc[8:16])))
    decoded_ori=bytes(list(map(ord,data_enc[16:])))
    return decoded_lat,decoded_lon,decoded_ori
