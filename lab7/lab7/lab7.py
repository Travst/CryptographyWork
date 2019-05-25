
import hashlib
import time
import tkinter as tk
from tkinter import filedialog

import pyperclip


def fileHash(fileName):
    m = hashlib.sha512()
    n = 1024 * 4                
    with open(fileName,'rb') as file:     #'rb'以二进制的格式打开一个文件
        while True:
            data=file.read(n)      #read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
            if not data:
                break
            m.update(data)            #Continue hashing of a message by consuming the next chunk of data.
    return m.hexdigest()

def chooseFile():
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()     # 选择打开什么文件，返回文件名
    return filename
    
def pyperClip():
    filename=chooseFile()
    start = time.process_time()
    filehash = fileHash(filename)
    end = time.process_time()
    print('Running time: %0.8fs Seconds' % (end - start))
    pyperclip.copy(filehash)
    print(filehash)

pyperClip()
