#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import PIL
from tkinter import *
from PIL import ImageTk, Image

#解决不显示中文的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

df = pd.read_csv('E:\Desktop\ProjectData18.csv')
df.dropna(axis=0,thresh=10,inplace=True)


#获取地区分布情况
def getProvince():
    path = 'E:\desktop\savefile2\province.txt'
    doc = open(path,'w+',encoding="utf-8")
    provincelist = df['省']

    #用字典计数
    dict = {}
    for province in provincelist:
        dict[province] = dict.get(province, 0) + 1


    citylist = df['市']
    districtlist = df['区县']
    print('Total '+str(len(provincelist))+'\n', file=doc)
    for key, value in zip(dict.keys(), dict.values()):
        cities = list(set(citylist[df['省']==key]))
        # print (cities)
        print(key + ' (' + str(value) + ')',file=doc)
        print(key + ' (' + str(value) + ')')
        for city in cities:
            print('----'+city+' (' + str(citylist.tolist().count(city))+ ')', file=doc)
            print('----'+city+' (' + str(citylist.tolist().count(city))+ ')')
            districts = list(set(districtlist[df['市'] == city]))
            for district in districts:
                print('-----------' + str(district) + '(' + str(districtlist.tolist().count(district)) + ')',file=doc)
                print('-----------' + str(district) + '(' + str(districtlist.tolist().count(district)) + ')')
        print('\n',file=doc)
        print('\n')
    print('Save to doc success')
    doc.close()

    root = Tk()
    root.title('省市区统计')
    root.geometry('500x400')
    text = Text(root, font='SimHei')

    # filename = 'E:\desktop\savefile2\province.txt'
    with open(path, encoding='utf-8') as f:
        for line in f:
            text.insert(END, line)
            # print (line, end='')

    text.pack()
    root.mainloop()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2. - 0.2, 1.03 * height, '%s' % float(height))


#统计毕业去向
def graduation():
    gras = df['毕业去向'].tolist()
    print ('Total ', len(gras))
    gra = list(set(gras))
    # result = pd.value_counts(gras)
    # print(result)
    count = []
    for i in gra:
        count.append(gras.count(i))
    # print (count)
    # print (gra)

    # plt.figure(figsize=(9,7))
    labels = gra
    fracs = count
    explode = [0,0,0,0]
    plt.axes(aspect=1)
    plt.pie(x=fracs, labels=labels, explode=explode, autopct = '%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
    plt.legend()
    plt.savefig('E:\desktop\savefile2\graduatePie.png')
    print('Save image success!')
    plt.show()


#平均GPA统计
def meanGPA():
    # df_mean = df.groupby('毕业去向')['毕业GPA'].mean()
    # gras = df['毕业去向'].tolist()
    gra = list(set(df['毕业去向'].tolist()))
    mean = []
    for i in gra:
        meangpa = df['毕业GPA'][df['毕业去向']==i].mean()
        mean.append(meangpa)
    print(gra,'\n',mean)
    a = plt.bar(gra, mean, label='Average GPA')
    # plt.legend()
    autolabel(a)
    plt.ylim((0,4.0))
    plt.xlabel('毕业去向')
    plt.ylabel('平均GPA')
    plt.title('OKKKKKK')
    plt.savefig('E:\desktop\savefile2\meanGPA.png')
    print ('Save image success')
    plt.show()


#毕业去向人数分布以及毕业去向平均GPA
def twoPic():
    gras = df['毕业去向'].tolist()
    gra = list(set(gras))
    count = []
    mean = []
    for i in gra:
        count.append(gras.count(i))

    for i in gra:
        meangpa = df['毕业GPA'][df['毕业去向'] == i].mean()
        mean.append(meangpa)
    # print (mean)


    plt.figure(1,figsize=(10,5))
    ax1 = plt.subplot(1,2,1)
    ax2 = plt.subplot(1,2,2)
    plt.sca(ax1)
    a = plt.bar(gra, count, label='Number')
    autolabel(a)
    plt.ylim((0,42))
    plt.title('毕业去向人数分布')
    plt.sca(ax2)
    b = plt.bar(gra, mean, label='Average GPA',fc = 'r')
    autolabel(b)
    plt.ylim((2.5,4.0))
    plt.title('毕业去向平均GPA对比')
    plt.savefig('E:\desktop\savefile2\GPA_Count.png')
    print('Save image success!')
    plt.show()



#工作统计
def goWork():
    work = df[['姓名', '性别', '毕业GPA', '工作省份', '工作城市', '工作单位', '月薪']][df['毕业去向']=='毕业工作']
    cities = list(set(work['工作城市']))
    print (cities)
    count = []
    for city in cities:
        count.append(work['工作城市'].tolist().count(city))
    print (count)

    danwei = df['工作单位'][df['毕业去向'] == '毕业工作'].dropna()
    worktype = pd.value_counts(danwei)
    wt = worktype.index.tolist()
    wn = worktype.tolist()

    plt.figure(1, figsize=(14,6))

    ax1 = plt.subplot(1,3,1)
    plt.sca(ax1)
    a = plt.bar(cities, count)
    autolabel(a)
    plt.ylim((0,19))
    plt.xlabel('City')
    plt.ylabel('Number')
    plt.title('预计工作城市')

    ax2 = plt.subplot(1,3,2)
    plt.sca(ax2)
    plt.pie(x = wn, labels=wt, startangle=90, autopct = '%3.1f %%', shadow=True,
             labeldistance=1.1, pctdistance=0.6)
    plt.title('工作类型')

    ax3 = plt.subplot(1,3,3)
    plt.sca(ax3)
    salary = df['月薪'][df['毕业去向'] == '毕业工作']
    plt.hist(salary, bins=6, fc = 'pink')
    plt.title('期待月薪分布')

    plt.savefig('E:\desktop\savefile2\goWork.png')
    print('Save image success!')
    plt.show()


#国内读研统计
def inChina():
    univers = df['大学'][df['毕业去向']=='内地读研']
    attrs = pd.value_counts(univers).index
    nums = pd.value_counts(univers).tolist()

    degree = df['深造学位'][df['毕业去向'] == '内地读研']
    attrs1 = pd.value_counts(degree).index
    nums1 = pd.value_counts(degree).tolist()

    label = str(len(univers)) + '人中选择的读研大学'
    plt.figure(figsize=(16,9))
    ax1 = plt.subplot(1,2,1)
    plt.sca(ax1)
    a = plt.bar(attrs, nums, fc = 'r')
    # plt.xlim((0,10))
    plt.ylim((0,9))
    plt.title(label)
    autolabel(a)
    ax2 = plt.subplot(1,2,2)
    plt.sca(ax2)
    b = plt.bar(attrs1, nums1)
    plt.ylim((0,16))
    plt.title('深造学位情况')
    autolabel(b)

    plt.savefig('E:\desktop\savefile2\inChina.png')
    print('Save image success!')
    plt.show()
    # print (len(china))



#国外留学统计
def inForeign():
    path = 'E:\desktop\savefile2\goForeign.txt'
    doc1 = open(path, 'w+', encoding="utf-8")
    countries = df['留学地'][df['毕业去向'] == '出国留学'].tolist()
    print ('Total '+ str(len(countries))+'\n', file=doc1)
    print ('Total ', len(countries))
    country = list(set(countries))
    # university = list(set(df['留学大学'].dropna()))
    # print (university)
    for i in country:
        print (i+' ('+str(countries.count(i))+')', file=doc1)
        print (i+' ('+str(countries.count(i))+')')
        for j in list(set(df['留学大学'][df['留学地']==i])):
            print ('----------'+j+' ('+str(df['留学大学'].tolist().count(j))+')', file=doc1)
            print ('----------'+j+' ('+str(df['留学大学'].tolist().count(j))+')')
        print ('\n', file=doc1)
        print ('\n')
    # print (country)
    doc1.close()

    root = Tk()
    root.title('国外留学统计')
    root.geometry('500x400')
    text = Text(root, font='SimHei')

    # filename = 'E:\desktop\savefile2\province.txt'
    with open(path, encoding='utf-8') as f:
        for line in f:
            text.insert(END, line)
            # print (line, end='')

    text.pack()
    root.mainloop()


def getCity():
    city = pd.value_counts(df['市'])
    l = df['市'].tolist()
    c=l.count('重庆')
    print (c)


# print (dict.keys())
# province = pd.value_counts(df['省'])

def test():
    # hello = df['市'][df['省']=='广东']
    # print (hello)
    # testlist = [1,2,1,2,1,4,5]
    # nlist = list(set(testlist))
    # print (nlist)

    # df = pd.read_csv('E:\Desktop\ProjectData18.csv')
    # df.dropna(axis=0, thresh=10, inplace=True)
    # print (df)

    # df_mean = df.groupby('毕业去向')['毕业GPA'].mean()
    # print (df_mean.index.tolist())
    # print (df_mean.tolist())

    # gras = df['毕业去向'].tolist()
    # result = pd.value_counts(gras)
    # df_mean = df.groupby('毕业去向')['毕业GPA'].mean()
    # print (list(set(gras)))
    # print(result.tolist())
    # print (df_mean)

    # danwei = df['工作单位'][df['毕业去向']=='毕业工作'].dropna()
    # worktype = pd.value_counts(danwei)
    # wt = worktype.index.tolist()
    # wn = worktype.tolist()
    # print (wt,wn)

    # df_mean = df.groupby('毕业去向')['毕业GPA'].mean()
    # print (df_mean)

    salary = df['月薪'][df['毕业去向']=='毕业工作']
    plt.hist(salary, bins=6)
    plt.show()


def main():
    # getProvince()
    # graduation()
    # meanGPA()
    # twoPic()
    # test()
    # meanGPA()
    # inChina()
    # inForeign()
    # goWork()

    root = tk.Tk()
    root.title('这是一个巨丑的小程序')

    canvas = tk.Canvas(root, width=620, height=420, bd=0, highlightthickness=0)
    imgpath = 'E:/Desktop/sustc1.jpeg'
    img = PIL.Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)

    canvas.create_image(300, 200, image=photo)
    canvas.pack()

    # Button(root, text='打开省市区文件').pack(side=LEFT, expand=YES, fill=BOTH)
    # Button(root, text='毕业去向统计', command = graduation).pack(side=TOP, expand=YES, fill=BOTH)
    # Button(root, text='国内深造统计').pack(side=TOP, expand=YES, fill=BOTH)
    # Button(root, text='国外留学统计').pack(side=TOP, expand=YES, fill=BOTH)
    # Button(root, text='毕业工作统计').pack(side=TOP, expand=YES, fill=BOTH)

    root.mainloop()

if __name__ == '__main__':
    main()