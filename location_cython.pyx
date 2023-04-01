
cdef union Converter:
    char[16] char_value 
    double  float_value




def from_float2char(double value):
    cdef Converter converter = Converter(float_value=value)
    return [converter.char_value[0],
    converter.char_value[1],
    converter.char_value[2],
    converter.char_value[3],
    converter.char_value[4],
    converter.char_value[5],
    converter.char_value[6],
    converter.char_value[7]]

def from_float2char2(double value):
    cdef Converter converter = Converter(float_value=value)
    return bytes(converter.char_value[:8])




def from_char2flaot(value :char[8]):
    cdef Converter converter=Converter(float_value=0)
    converter.char_value[0] = value[0]
    converter.char_value[1] = value[1]
    converter.char_value[2] = value[2]
    converter.char_value[3] = value[3]
    converter.char_value[4] = value[4]
    converter.char_value[5] = value[5]
    converter.char_value[6] = value[6]
    converter.char_value[7] = value[7]
    return converter.float_value


