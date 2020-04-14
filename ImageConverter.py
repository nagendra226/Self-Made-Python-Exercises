import sys
import os
from PIL import Image


def image_converter(path_to_create, *args):
    '''

    :param path:  Path where you want to create the files
    :param args: Number of files you can pass
    :return:  create all the files passed in the args to png from jpeg
    '''
    image_lists = None
    file_name = None
    flag_png = 0
    i = 0
    val = None
    try:
        if (path_to_create):
            if not os.path.exists(path_to_create):
                os.makedirs(path_to_create)

        print(path_to_create)

        for img_value in args:
            # change the file names
            i = i + 1
            # get the file name form the path
            file_name = os.path.basename(img_value)
            image_lists = file_name.split('.')
            with Image.open(img_value) as image_open:
                val = path_to_create + image_lists[0] + '_' + str(i)
                print(val)
                print(image_lists[1])
                if image_lists[1] == 'png':
                    image_open.save(val+'.jpg','JPEG')
                    flag_png = 1
                elif image_lists[1] == 'jpg':
                    image_open.save(val+'.png','PNG')
                    flag_png = 0
    except IOError as err:
        return "Unable to create file path" + err
    except:
        return "Please correct your program"
    if flag_png == 0:
        return "Images are converted to PNG from JPEG Successfully."
    elif flag_png == 1:
        return "Images are converted to JPEG from PNG Successfully."


print(image_converter('D:\\Personal\\Python\\new\\',
                      'D:\\Personal\\Python\\Python2020\\Python Udemy Andrei\\PyCharm2\\Python Scripting\\pussy.png',
                      'D:\\Personal\\Python\\Python2020\\Python Udemy Andrei\\PyCharm2\\Python Scripting\\dlc3.png',
                      'D:\\Personal\\Python\\Python2020\\Python Udemy Andrei\\PyCharm2\\Python Scripting\\hp3.png',
                      'D:\\Personal\\Python\\Python2020\\Python Udemy Andrei\\PyCharm2\\Python Scripting\\hp4.png'))
