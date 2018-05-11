__all__ = [
        "rasterData",
        "compression",
        "bits_per_pixel"
        ]

__doc__ = """    rasterData(bits)
Returns the color (color), compression type (compression) and byte pixels (byte_pixels)


    compression
    
Returns the compression type ranging from: "no compression", "8bit RLE encoding" or "4bit RLE encoding"

    bits_per_pixel
    
Returns type of bits and the number of colours supported 
"""



def rasterData(bits):
    if bits == 1: return {'color':'black/white', 'compression':0, 'byte_pixels':8}
    elif bits == 4: return {'color':'16_color', 'compression':0, 'byte_pixels':2}
    elif bits == 8: return {'color':'256_color', 'compression':0, 'byte_pixels':1}
    else: raise Exception('UnrecordedError: This bit number is unknown or has not been recorded')

compression = { # Compression type and format
    0:('BI_RGB', 'no compression'), 
    1:('BI_RLE8', '8bit RLE encoding'), 
    2:('BI_RLE4', '4bit RLE encoding')}

bits_per_pixel = { # Type of bits and the number of colours supported
    1:{'type':'monochrome palette', 'NumColors':1},
    4:{'type':'4bit palletised', 'NumColors':16},
    8:{'type':'8bit palletised', 'NumColors':256},
    16:{'type':'16bit RGB', 'NumColors':65536},
    24:{'type':'24bit RGB', 'NumColors':16000000}}