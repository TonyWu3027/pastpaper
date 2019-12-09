# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import ttk
from pastpaper import pastpaper

# Fields
titleEng = "Past Paper Downloader Ver 3.0"
content = ["Mathematics (9709)",
           "Computer Science (9608)",
           "Geography (9696)",
           "Economics (9708)",
           "Physics (9702)",
           "Chemistry (9701)",
           "Biology (9700)",
           "Chemistry (9701)",
           "Geography (0460)",
           'Mathematics - Further (9231)'
           ]


strEng = "Starting Year"
stoEng = "Stoping Year"
numEng = "Paper Number"
nameEng = "Past Paper Explorer"
titleCh = "考卷下载器 版本 3.0"
strCh = "开始年份"
stoCh = "停止年份"
numCh = "试卷号"
nameCh = "考卷下载器"
sbjEng='Subject'
sbjCh='科目'
msg_1={'eng':'Error! Starting/stopping year should be 2 digits','chn':'错误！起始/结束年份应该是两位整数'}
msg_2={'eng':'Error! Paper Number should be a digit','chn':'错误！卷号应该是一位整数'}
msg_3={'eng':'Finished - Please check in the console','chn':'完成 - 请到Console中查看状况'}


'''
The GUI is programmed using python Tkinter library, all strings are stored in fields
'''
def check(num,length):
    flag=False
    if len(num)==length and num.isdigit():
        flag=True

    return flag


def varification(start,stop,pnum,lan):
    start_status=check(start,2)
    stop_status=check(stop,2)
    pnum_status=check(pnum,1)

    if start_status==False or stop_status==False:
        return False,msg_1[lan]

    elif pnum_status==False:
        return False,msg_2[lan]

    else:
        return True,msg_3[lan]

def ENG_ver():
    root = Tk()
    root.title(titleEng)#The title is stored in titleEng

    statusTxt = StringVar()
    statusTxt.set("")

    headLine = Label(root, text=nameEng).grid(row=0)

    # an entry for starting year
    var_start = StringVar()
    start = Entry(root, textvariable=var_start)
    start.grid(row=2, column=1)

    #An entry for stoping year
    var_stop = StringVar()
    stop = Entry(root, textvariable=var_stop)
    stop.grid(row=2, column=2)

    #An entry for paper number
    papernum = StringVar()
    paper = Entry(root, textvariable=papernum)
    paper.grid(row=4, column=1)

    #Messages shown on the GUI
    startTxt = Label(root, text=strEng).grid(row=1, column=1)
    stopTxt = Label(root, text=stoEng).grid(row=1, column=2)
    NumTxt = Label(root, text=numEng).grid(row=3, column=1)
    SbjTxt=Label(root,text=sbjEng).grid(row=1,column=0)

    # Scroll menu
    number = StringVar()
    subject = ttk.Combobox(root, width=18)
    subject['values'] = content
    subject.grid(row=2, column=0)
    subject.current(0)

    statuslb=Label(root,text='Status:').grid(row=5,column=0)
    StatusBar = Label(root)
    StatusBar['text']='Welcome'
    StatusBar.grid(row = 6, column = 0)

    def change_status(msg):
        StatusBar.configure(text=msg)

    def OnButtonDown():  # Link to Tony's class, start crawler

        #obtain the user's entry
        sta = start.get()
        sto = stop.get()
        pnum = paper.get()
        subj = subject.get()

        #send the user's entry to varification module
        status,msg=varification(sta,sto,pnum,'eng')
        #error message if needed
        change_status(msg)

        #calling the core algorithm
        if status==True:
            pp = pastpaper()
            pp.get_start(sta)
            pp.get_stop(sto)
            pp.get_num(pnum)
            pp.get_subject(subj)
            count=pp.get_paper_header()
            for i in range(0,count):
                pp.crawler_al('eng',i)#crawling


    # Launch button call the OnButtonDown() function
    launchButton = Button(root, text="Launch")
    launchButton['command'] = OnButtonDown
    launchButton.grid(row=4, column=2)


    root.mainloop()


#The Chinese version is the same as the English version except for the language for the messages
def CHN_ver():
    root=Tk()
    root.title(titleCh)

    statusTxt = StringVar()
    statusTxt.set("")

    headLine = Label(root, text=nameCh).grid(row=0)

    # Starting year, stopping year and  past paper number
    var_start = StringVar()
    start = Entry(root, textvariable=var_start)
    start.grid(row=2, column=1)

    var_stop = StringVar()
    stop = Entry(root, textvariable=var_stop)
    stop.grid(row=2, column=2)

    papernum = StringVar()
    paper = Entry(root, textvariable=papernum)
    paper.grid(row=4, column=1)

    startTxt = Label(root, text=strCh).grid(row=1, column=1)
    stopTxt = Label(root, text=stoCh).grid(row=1, column=2)
    NumTxt = Label(root, text=numCh).grid(row=3, column=1)
    SbjTxt = Label(root, text=sbjCh).grid(row=1, column=0)

    # Scroll menu
    number = StringVar()
    subject = ttk.Combobox(root, width=18, textvariable=number)
    subject['values'] = content
    subject.grid(row=2, column=0)
    subject.current(0)

    statuslb=Label(root,text='状态:').grid(row=5,column=0)
    StatusBar = Label(root)
    StatusBar['text']='欢迎'
    StatusBar.grid(row = 6, column = 0)

    def change_status(msg):

        StatusBar.configure(text=msg)

    def OnButtonDown():  # Link to Tony's class, start crawler

        sta = start.get()
        sto = stop.get()
        pnum = paper.get()
        subj = subject.get()

        status,msg=varification(sta,sto,pnum,'chn')
        if status==True:
            change_status(msg)
            pp = pastpaper()
            pp.get_start(sta)
            pp.get_stop(sto)
            pp.get_num(pnum)
            pp.get_subject(subj)
            count=pp.get_paper_header()
            for i in range(0,count):
                pp.crawler_al('chn',i)
                #change_status(i)
        else:
            change_status(msg)

    # Launch button call the OnButtonDown() function
    launchButton = Button(root, text="开始")
    launchButton['command'] = OnButtonDown
    launchButton.grid(row=4, column=2)

    root.mainloop()
    
def main():
    langWin = Tk()
    langWin.title("Language Selection Window")

    prompt = Label(langWin, text="Please choose the language/ 请选择语言").grid(row=0, column=1)

    engButton = Button(langWin, text="English")
    engButton["command"] = ENG_ver
    engButton.grid(row=1, column=0)

    chButton = Button(langWin, text="中文")
    chButton["command"] = CHN_ver
    chButton.grid(row=1, column=2)

    langWin.mainloop()
main()