# Python-Bitmap
A (nearly) dependency free library to read bitmap images. 

Example usage:

     from bitmap import Image
     
     with open('test.bmp') as file:
         a = Image(file.read())
     
     print('Width: ', a.getBitmapWidth()) # Return width of image in pixels
     print('Height: ', a.getBitmapHeight()) # Return height of image in pixles
     
     print('Data:\n\n', a.getPixels()) # Get total pixels
     
     print('Pixel RGB value at value X, Y:', a.getPixels()[0][19]) # Return the RGB value as a list (note that the first pixel starts on 0 and not 1)
     
     ----
       

Convert to grid:

    x  = open('test1.bmp', 'rb').read()
    import bitmap
    a = bitmap.grid(x)

Convert from grid back to image:

    b = bitmap.reform(a)

Get colour value:
     
     import bitmap.colors
     print(bitmap.colors.fromRGB(a[2][3]))
