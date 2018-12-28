from PIL import Image
from DSAAPro.DSAAFinal.maincode import *


def thismain():
    root = tk.Tk()
    root.title('这是一个巨丑的小程序')

    canvas = tk.Canvas(root, width=620, height=420, bd=0, highlightthickness=0)
    imgpath = 'E:/Desktop/LOGO.png'
    img = PIL.Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)

    canvas.create_image(300, 200, image=photo)
    canvas.pack()

    Button(root, text='打开省市文件',command = getProvince).pack(side=LEFT, expand=YES, fill=X )
    Button(root, text='毕业去向统计', command = twoPic).pack(side=LEFT, expand=YES, fill=X)
    Button(root, text='国内深造统计', command = inChina).pack(side=LEFT, expand=YES, fill=X)
    Button(root, text='国外留学统计', command = inForeign).pack(side=LEFT, expand=YES, fill=X)
    Button(root, text='毕业工作统计', command = goWork).pack(side=LEFT, expand=YES, fill=X)
    #
    # text = Text(root, width=30, height=5)
    # text.pack()
    # text.insert(INSERT, 'I Love you\n')
    # text.insert(END, 'Teachers!')

    root.mainloop()

if __name__ == '__main__':
    thismain()