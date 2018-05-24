def toRGB(red:int, green:int, blue:int):
    """Convert red, green and blue values into a tuple that can be used to interfase with Python-Bitmap""" 
    return (red, green, blue)

def fromRGB(rgb):
    """Convert tuple or list to red, green and blue values that can be accessed as follows:

    a = fromRGB((255, 255, 255))
    a["red"]
    a["green"]
    a["blue"]
    """ 
    return {"red":rgb[0], "green":rgb[1], "blue":rgb[2]}


    



    
    
