# Python-Bitmap
A dependency free library to read bitmap images. 

Example usage:

     from PythonBitmap import Image
     
     with open('test.bmp') as file:
         a = Image(file.read())
     
     print('Width: ', a.getBitmapWidth()) # Return width of image in pixels
     print('Height: ', a.getBitmapHeight()) # Return height of image in pixles
     
     print('Data:\n\n', a.getPixels())
     
       
