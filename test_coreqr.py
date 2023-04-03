from coreqr import encod_data ,decode_data 

location = {
  "latitude": 50.3183202730564860,
  "longitude": 3.5105228796591064,
  "orientation":1

}
encoded_data=encod_data(location["latitude"],location["longitude"],location["orientation"])

def testencod_data():
    encoded_data=encod_data(location["latitude"],location["longitude"],location["orientation"])
    lat=bytes(list(encoded_data[:8]))
    lon=bytes(list(encoded_data[8:16]))
    ori=bytes(list(encoded_data[16:]))

    assert(location["latitude"])in decode_data(decoded_lat=lat,decoded_lon=lon,decoded_ori=ori)
    assert(location["longitude"])in decode_data(decoded_lat=lat,decoded_lon=lon,decoded_ori=ori)
    assert(location["orientation"])in decode_data(decoded_lat=lat,decoded_lon=lon,decoded_ori=ori)
    
testencod_data()
a=1
