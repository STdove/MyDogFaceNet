import urllib
import re
from urllib import request
import os
import csv
import time
from tqdm import tqdm



# function area
# if there are no data folder, create a new one
def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print("build new data folder")
    else:
        print("find data folder")


# if there is no data.csv,create a new one,else return the data(type list) from data.csv
def getcsv(path,first_row):
    csvfile=os.path.isfile(path)
    print(path)
    if csvfile!=True:
        print("-----build new csv file-----")
        writecsv("",path,first_row)
        return []
    else :
        print("-----found csv file-----")
        return readcsv(path)


# get data from exist csv
def readcsv(path):
    csvlist=[]
    with open(path, "r")as f:
        reader = csv.DictReader(f)
        for row in reader:
            csvlist.append((row['picture'], row['title']))
    return csvlist


# get source of page from website
def urlprocess(url):
    response = request.urlopen(url)
    text = response.read().decode()
    if text=="<html><body>Access Denied - Zugriff verweigert</body></html>":
        print("Access to website is Denied,please wait or contact to manager")
        return False
    else :
        #wait 1 second each time we request for a page
        time.sleep(10)
    return text


# if there is no file, make a new one, else overwrite the data.
def writecsv(text,path,first_row):

    with open(path, "w", newline='')as f:
        writer = csv.writer(f)
        writer.writerow(first_row)
        writer.writerows(text)
    return


# compare data from page and data from csv, if there are data csv did not have,
# append it, also append it to process list and wait for process(download)
def comparedata(originaldata,compareddata,newdata):
    if originaldata!=[]:
        for ele in compareddata:
            if ele not in originaldata:
                newdata.append(ele)

    else:
        for i in compareddata:
            newdata.append(i)



# download pic from website
def loadpic(piclist,path,originaldata):
    # try:
        for elem in tqdm(piclist):
            img_url = 'https://file1.hpage.com/009942/44/bilder/' + elem[0]
            img_path = path+'/'+elem[0]
            # wait for 2 second when we download one image, to make sure server overload not
            urllib.request.urlretrieve(img_url, img_path)
            time.sleep(20)
            originaldata.append(elem)
    # except Exception as info:
    #     print(info)
    # finally:
    #     title_path = path + "/data.csv"
    #     first_row = ("picture", "title")
    #     writecsv(originaldata, title_path, first_row)
    #     print("-----some errors occurred, what we have done for now is saved, please try later-----")

def main():
    # set and define area,set necessary parameter,


    #set_url = "https://hundehof-meikeva.hpage.com/gallery459656.html"
    #to use this program you need to uncommen the code above,please be gentle to the website,access to fast may cause the crash of the website

    set_path = "./data/pictures"
    title_path = "./data/data.csv"
    first_row = ("picture", "title")

    # pic_info_web is pic info from the current page.it will compared with pic_info_csv,
    # which the last time we updated info from website into data.csv,if there are info not existed
    # in pic_info_csv,we will download the newest pic into data folder and update the new info into data.csv


    pic_info_process = []

    #check ob there are data folder and data.csv for pictures and titel
    mkdir(set_path)
    pic_info_csv=getcsv(title_path, first_row)


    first_page=urlprocess(set_url)
    try:
        if first_page!=False:

            # get page numbers from first page except page 0
            pattern_get_page=re.compile(r'<a href="/gallery459656.html\?pagination\[galleries\]\[459656\]=(\d*)">')#get 15,30,45,60,75... but without 0
            result_page_num=pattern_get_page.findall(first_page)

            #beacause we are in the first page ,we can only get other hrefs without first href 0 from first page, we need deal first page by ourself
            pattern = re.compile(r'href="https://file1.hpage.com/009942/44/bilder/(.*)" title="(.*)"')
            pic_info_web = pattern.findall(first_page)
            comparedata(pic_info_csv, pic_info_web, pic_info_process)

            # get all pictrues according to index 15,30,45,60    result_page_num
            print("-----check for update-----")
            for page in tqdm(result_page_num):
                current_url = "https://hundehof-meikeva.hpage.com/gallery459656.html?pagination[galleries][459656]=%s" %page
                response_page = urlprocess(current_url)
                pattern = re.compile(r'href="https://file1.hpage.com/009942/44/bilder/(.*)" title="(.*)"')
                pic_info_web = pattern.findall(response_page)
                comparedata(pic_info_csv,pic_info_web,pic_info_process)
            if(pic_info_process!=[]):
                print("-----information are updated,download now-----")
                loadpic(pic_info_process,set_path,pic_info_csv)
                print("-----all data are saved-----")
            else :
                print("-----all information is up to date-----")

        # #get all pictrues according to index 15,30,45,60result_all_page
        # for page in result_page_num:
        #     current_url ="https://hundehof-meikeva.hpage.com/gallery459656.html?pagination[galleries][459656]="+page+""
        #     response_page = urlprocess(current_url)
        #     pattern = re.compile(r'href="https://file1.hpage.com/009942/44/bilder/(.*)" title="(.*)"')
        #     result_pic = pattern.findall(response_page)
        #     for i in result_pic:
        #         img_url = 'https://file1.hpage.com/009942/44/bilder/' + i[0]
        #         img_path = set_path+'/'+i[0]
        #
        #         # wait for 2 second when we download one image, to make sure server overload not
        #         urllib.request.urlretrieve(img_url, img_path)
        #         time.sleep(2)
        #         print(i)
        #         all_pic.append(i)
    except Exception as info:
        print(info)
        print("-----some errors occurred, what we have done for now is saved, please try later-----")
    finally:

        # if there are some error occurred, it will save what have done for now,
        # so next time it will not start from begin
        writecsv(pic_info_csv,title_path,first_row)


if __name__=="__main__":
    main()