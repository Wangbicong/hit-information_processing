# -*- coding:utf-8 -*-
import struct
from PIL import Image


def load_gnt(file_name):
    f = open('LED-train.gnt','rb')
    images = []
    tags = []
    while f.read(1) != "":
        f.seek(-1, 1)
        length_bytes = struct.unpack('<I', f.read(4))[0]
        tag_code = struct.unpack('c', f.read(1))[0]
        f.read(1)
        width = struct.unpack('<H', f.read(2))[0]
        height = struct.unpack('<H', f.read(2))[0]
        img = Image.new('L', (width, height))
        img_array = img.load()
        for x in xrange(0, height):
            for y in xrange(0, width):
                pixel = struct.unpack('<B', f.read(1))[0]
                img_array[y, x] = pixel
        img.save(u'改变前.bmp')
        img = img.resize(size=(28, 28))
        img.save(u'改变后.bmp')
        images.append(map(ord, (img.tobytes())))
        tags.append(tag_code)
        print '图像的字节：',map(ord, (img.tobytes()))
        print '标签：', tag_code
    f.close()
    return images, tags

if __name__  == "__main__":
    load_gnt('LED-train.gnt')
