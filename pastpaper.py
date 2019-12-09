# -*- coding:utf-8 -*-

import requests

import os #For file handling

'''
Dear Ms.Razia 
This is group 1: Tony David and Jimmy!
We are sorry that we have to change our project aim. 
We have done the card game's core algorithm but the tricky thing is that it has already taken more than a thousand lines, and small problems pop up all the time
Plus the GUI part, it is impossible for us to finish it before DDL
So we activated our plan B, which is a software that can download pastpaper 
The user input the subject, the paper number, years on a GUI, and the software will use the web coding to download the papers in that yaer range
This file is the core algorithm, the GUI part is in the other file
HAVE FUN

Roles:
Tony: Core algorithm and web programming
Jimmy: GUI
David: Because he's a new programmer, we didn't give him a coding task. 
        Instead, we gave him some guidiance and taught him about our codes for him to improve


ps. import this file in the GUI part like this:

from pastpaper import pastpaer

Sincerely,
Tony, David and Jimmy

'''

#created in class, so the codes can be used by any external files. In this case, GUI.py
class pastpaper:

    #This method initialises the variables I need throughout the whole class
    def __init__(self):

        #fake a header, the parameters are stored in a dictionary called headers.
        # Otherwise, the website will detect that this request is from a unreliable source, so the request will be denied
        self.headers={'Host': 'papers.gceguide.xyz','Connection': 'keep-alive','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.8',}


        self.start=''#Starting year e.g. 11(2011)
        self.stop=''#Stop year e.g. 15(2015)
        self.num=''#paper1 or 2 or 3?
        self.subject=''#e.g. Mathematics (9709)
        self.sub_num=''#e.g.9709
        self.paper_header=''#e.g. 9709_s15_ms_21
        self.paper_list=[]

        self.message_sucessful={'chn':'成功下载','eng':'Sucessfully downloaded - '}
        self.message_fail_save={'chn':'存储该文件失败：','eng':'Failed to save - '}
        self.message_fail_dl={'chn':'请检查您的网络或卷号，该试卷下载失败：','eng':'Please check your network connection or paper number, failed to download - '}

    ###----These methods would be used with the GUI----###
    def get_start(self,start):
        self.start=start


    def get_stop(self,stop):
        self.stop=stop


    def get_num(self,num):
        self.num=num


    def get_subject(self,subject):
        self.subject=subject# the input will be in standard forms like Mathematics (9709) since the user use a drop-down box to input their option
        self.subject=self.subject.replace(' ','%20')# so we need to change its form to create the url in order for the xtremepapers.com to locate the right pdf
        self.sub_num=self.subject[-5:-1]# extract subject code e.g. 9709

    ###------------------------------------------------###


    #This method is used to create the name for the target file and store everything in a list
    def get_paper_header(self):
        for season in ('s','w','m'):#s for May/June paper, w for Oct/Nov paper and m for Mar paper according to CIE
            for year in range(int(self.start),(int(self.stop)+1)):# use the staring and stopping year gathered from the GUI as iteration limits
                for type in ('qp','ms','in'):# qp for question paper, ms for marking scheme
                    for region in range (1,4):# there are usually 3 regions number avaible for CIE paper
                        self.paper_header=self.sub_num+'_'+season+str(year)+'_'+type+'_'+self.num+str(region)# create the target file names for downloading
                        self.paper_list.append(self.paper_header)# store the names in a list called paper_list

        return len(self.paper_list)

    #This is the JUICY part - downloading the PDFs
    #By using the info proccessed before, this method download the PDFs we want
    def crawler_al(self,lan,i):

        #depending on how many files are needed to be downloaded, the method will iterate for these many times

        url= r"https://papers.gceguide.xyz/A%20Levels/"+self.subject+ "/" +self.paper_list[i]+'.pdf'
        #https://pastpapers.papacambridge.com/Cambridge%20International%20Examinations%20(CIE)/AS%20and%20A%20Level/Geography%20(9696)/2017%20Jun/9696_s17_in_13.pdf
        
        #create the path for local storage
        path = r"./"+self.subject.replace('%20','_')+"/" + self.paper_list[i] + ".pdf"

        #create request, a web crawling method provided by the built-in library urllib. The faked header is used
        try:
            #the response is saved in the variable 'data'
            r = requests.get(url, headers=self.headers)
            varify= r.text
            if varify[0:4] =='%PDF':
                try:
                    #The downloaded papers are classified and stored in folders named with that subject
                    #e.g. 9709 papers goes into Mathematics_(9709)
                    b = os.path.exists(r"./"+self.subject.replace('%20','_')+"/")#To examine if there is a folder. If there is one, pass, otherwise, create one
                    if b:
                        pass
                    else:
                        os.mkdir(r"./"+self.subject.replace('%20','_')+"/")#create a folder

                    # save the pdf to that folder, if there exists such a file, the program skips and directly output the successful message
                    f = open(path, "ab")
                    f.write(r.content)
                    f.close()
                    print(self.message_sucessful[lan] + self.paper_list[i])#Message for user if successful
                except:
                    print(self.message_fail_save[lan]+self.paper_list[i])#Message for user if fail if any error occur during saving the files
            else:
                print(self.message_fail_dl[lan] + self.paper_list[i])  # if no connection or paper not found, show this

        except:
            print(self.message_fail_dl[lan]+self.paper_list[i])#if no connection or paper not found, show this

    def crawler_ig(self, lan, i):

        # depending on how many files are needed to be downloaded, the method will iterate for these many times

        url = r"https://papers.gceguide.xyz/IGCSE/" + self.subject + "/" + self.paper_list[i] + '.pdf'
        # https://pastpapers.papacambridge.com/Cambridge%20International%20Examinations%20(CIE)/AS%20and%20A%20Level/Geography%20(9696)/2017%20Jun/9696_s17_in_13.pdf

        # create the path for local storage
        path = r"./" + self.subject.replace('%20', '_') + "/" + self.paper_list[i] + ".pdf"

        # create request, a web crawling method provided by the built-in library urllib. The faked header is used
        try:
            # the response is saved in the variable 'data'
            r = requests.get(url, headers=self.headers)
            varify = r.text
            if varify[0:4] == '%PDF':
                try:
                    # The downloaded papers are classified and stored in folders named with that subject
                    # e.g. 9709 papers goes into Mathematics_(9709)
                    b = os.path.exists(r"./" + self.subject.replace('%20',
                                                                    '_') + "/")  # To examine if there is a folder. If there is one, pass, otherwise, create one
                    if b:
                        pass
                    else:
                        os.mkdir(r"./" + self.subject.replace('%20', '_') + "/")  # create a folder

                    # save the pdf to that folder, if there exists such a file, the program skips and directly output the successful message
                    f = open(path, "ab")
                    f.write(r.content)
                    f.close()
                    print(self.message_sucessful[lan] + self.paper_list[i])  # Message for user if successful
                except:
                    print(self.message_fail_save[lan] + self.paper_list[
                        i])  # Message for user if fail if any error occur during saving the files
            else:
                print(self.message_fail_dl[lan] + self.paper_list[i])  # if no connection or paper not found, show this

        except:
            print(self.message_fail_dl[lan] + self.paper_list[i])  # if no connection or paper not found, show this

'''
THIS PART IS FOR TESTING WITHOUT GUI COMPONENT 
TEST VALUES FILLED IN ALREADY
ERASE THE COMMENT MARKS TO USE
'''

'''
a=pastpaper()
a.get_start('15')
a.get_stop('15')
a.get_num('2')
a.get_subject('Mathematics (9709)')
length=a.get_paper_header()
for i in range(0, length):
    a.crawler('eng',i)
'''


