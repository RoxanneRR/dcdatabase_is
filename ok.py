import requests,re,time,os,shutil
from bs4 import BeautifulSoup
import bs4


filethepath=os.getcwd()+"\\dcdatabase\\"
if not os.path.exists(filethepath):
        os.makedirs(filethepath)


##########################################功能1：下载文件

def downlist(forurl,urname):

    allmember_list=[]
    forurl=forurl
    i=1
    j=1

    
    while j:

        print("爬取第",i,"页……")
    
        r=requests.get(forurl)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        
        html = r.text

        
        soup = BeautifulSoup(html,"html.parser")
        member_list = soup.find_all('a',{"class": "category-page__member-link"})

        for member in member_list:
                #print(member['href'])
                print(member['title'],end="")
                member['href'] = "https://dc.fandom.com"+member['href']
                #opname= member['title']
        
        allmember_list = allmember_list + member_list


         
        
        ifnext = soup.find_all('a',{"class": "category-page__pagination-next wds-button wds-is-secondary"})
        #print(ifnext)
        if ifnext:

                print("【！】……页面较多……",i,"并不是最后一页……【！】")
                print("准备爬取下一页",ifnext[0]["href"])
                forurl=ifnext[0]["href"]
                print("【！】（以防爬取太快给dcdaabase服务器造成压力）程序将休眠20秒，请耐心等待……【！】")
                time.sleep(20)
                i=i+1
                
        else:

                print("全部爬取完成！")
                j=0
 
    print("…………共",i,"页………………")
    
    print("…………共",str(len(allmember_list)),"条………………")
    
    urname = filethepath+ urname+"_"+str(len(allmember_list))+"_list.html"


    print(allmember_list,file=open(urname,"w",encoding="utf-8"))
        
    print("文件【"+urname+"】已经生成！你可以随意修改它的名字！")
    print("===============================================================================================")


    print("===============================================================================================")

    print(">>按任意键继续>>")

    anyk=input("===============================================================================================")




##########################################功能2：查重交集




def interlist(wjlist,newname):

    ch_list=[]

    
    fr1 = open(filethepath+wjlist[0], 'r+', encoding='utf-8')
    html1 = fr1.read()
    soup1 = BeautifulSoup(html1,"html.parser")
    member1_list = soup1.find_all('a',{"class": "category-page__member-link"})

    ch_list = member1_list
    

    
    for wj in wjlist[1:]:
        fr2 = open(filethepath+wj, 'r+', encoding='utf-8')
        html2 = fr2.read()
        soup2 = BeautifulSoup(html2,"html.parser")
        member2_list = soup2.find_all('a',{"class": "category-page__member-link"})
        
        ch_list=list(set(ch_list) & set(member2_list)) 

   

    newname =filethepath+ newname+"_"+str(len(ch_list))+"_list.html"

    print(ch_list,file=open(newname,"w",encoding="utf-8"))  

    print("===============================================================================================")

    
    print("所查询的【"+newname+"】重合列表如下：")
    for ch in ch_list:
        print(ch["title"])
 
    if ch_list==[]:
        print("居然没有任何重合！")

    else:
        print("查重得到",len(ch_list),"条！")
 


    
    print("文件【"+newname+"】已经生成！你可以随意修改它的名字！")

    print("===============================================================================================")

    print(">>按任意键继续>>")

    anyk=input("===============================================================================================")


##########################################功能3：合并并集




def unionlist(wjlist,newname):

    ch_list=[]

    
    fr1 = open(filethepath+wjlist[0], 'r+', encoding='utf-8')
    html1 = fr1.read()
    soup1 = BeautifulSoup(html1,"html.parser")
    member1_list = soup1.find_all('a',{"class": "category-page__member-link"})

    ch_list = member1_list
    

    
    for wj in wjlist[1:]:
        fr2 = open(filethepath+wj, 'r+', encoding='utf-8')
        html2 = fr2.read()
        soup2 = BeautifulSoup(html2,"html.parser")
        member2_list = soup2.find_all('a',{"class": "category-page__member-link"})
        
        ch_list=list(set(ch_list) | set(member2_list)) 

   

    newname =filethepath+ newname+"_"+str(len(ch_list))+"_list.html"

    print(ch_list,file=open(newname,"w",encoding="utf-8"))  

    print("===============================================================================================")

    
    print("所查询的【"+newname+"】合并（去重）列表如下：")
    for ch in ch_list:
        print(ch["title"])
 
    if ch_list==[]:

        print("居然合并起来是0零zero！")

    else:
        print("合并后共",len(ch_list),"条！")
 


    
    print("文件【"+newname+"】已经生成！你可以随意修改它的名字！")

    print("===============================================================================================")

    print(">>按任意键继续>>")

    anyk=input("===============================================================================================")
    
##########################################功能4：减去差集




def differlist(wjlist,newname):

    ch_list=[]

    
    fr1 = open(filethepath+wjlist[0], 'r+', encoding='utf-8')
    html1 = fr1.read()
    soup1 = BeautifulSoup(html1,"html.parser")
    member1_list = soup1.find_all('a',{"class": "category-page__member-link"})

    ch_list = member1_list
    

    
    for wj in wjlist[1:]:
        fr2 = open(filethepath+wj, 'r+', encoding='utf-8')
        html2 = fr2.read()
        soup2 = BeautifulSoup(html2,"html.parser")
        member2_list = soup2.find_all('a',{"class": "category-page__member-link"})
        
        ch_list=list(set(ch_list) - set(member2_list)) 

   

    newname =filethepath+ newname+"_"+str(len(ch_list))+"_list.html"

    print(ch_list,file=open(newname,"w",encoding="utf-8"))  

    print("===============================================================================================")

    
    print("所查询的【"+newname+"】差集列表如下：")
    for ch in ch_list:
        print(ch["title"])
 
    if ch_list==[]:

        print("很遗憾，没有剩下的了！")

    else:

        print("做完减法后还剩",len(ch_list),"条！")
 


    
    print("文件【"+newname+"】已经生成！你可以随意修改它的名字！")

    print("===============================================================================================")

    print(">>按任意键继续>>")

    anyk=input("===============================================================================================")
    

##########################################【目录页】 

    

#####功能1目录

def checkpage():
    while True:
        print('==========请输入dcdatabase的角色出场界面==========')
        print('e.g.【https://dc.fandom.com/wiki/Category:Timothy_Drake_(New_Earth)/Appearances】')
        forurl = input('>>' )
        if forurl == "back":
            urname="0"
            return forurl,urname
        rightinput = r'^https://dc.fandom.com/wiki/Category:(.*)/Appearances$'
        op = re.match(rightinput,forurl)
        if not op:
            print("格式错误！请输入正确网址！返回上级请输入back")
        else:
            print("你输入了【"+forurl+'】')
            urname=op.group(1)
            print(urname)
            return forurl,urname
    return forurl,urname


#####功能2目录

def checkinter(htmlist):
    wjlist=[]
    newname=""
    while True:
        print('==========请输入当前目录中有的文件==========')
        print('e.g.【某某某_list.html】,返回上级输入back，删除列表输入dele,选择完毕后输入ok')
        wjname = input('>>'+str(wjlist))
        if wjname == "back":
            break
        elif wjname == "dele":
            wjlist = wjlist[0:-1]
        elif wjname == "ok":
            if not wjlist ==[]:
                for wj in wjlist:
                    try:
                        wjf=re.match(r"(.*?)_(.*)",wj).group(1)
                    except:
                        wjf=wj
                    #print('wj=',wj,'wjf=',wjf,'newname=',newname)                
                    newname=newname+"&"+wjf
                print("===============================================================================================")
                print("你要查询的是【"+newname+"】，再次输入ok确认，否则取消。")
                justdo = input(">>【"+newname+"】>>")
                if justdo == "ok":
                    return wjlist,newname
                else:
                    #wjlist=[]#取消清空表格，没必要
                    newname=""#取消重置名字，有必要

        elif not wjname in htmlist:
            print("格式错误！请输入目录中的文件名！返回上级输入back，删除列表输入dele,选择完毕后输入ok")
        else:
            wjlist.append(wjname)
            print(">>","表格喜+1！")


  
    return wjlist,newname   

  
#####功能3目录

def checkunion(htmlist):
    wjlist=[]
    newname=""
    while True:
        print('==========你需要合并内容吗？例如将某角色的p52和n52两个文件合并在一起==========')
        print('e.g.【某某某_list.html】,返回上级输入back，删除列表输入dele,选择完毕后输入ok')
        wjname = input('>>'+str(wjlist))
        if wjname == "back":
            break
        elif wjname == "dele":
            wjlist = wjlist[0:-1]
        elif wjname == "ok":
            if not wjlist ==[]:
                for wj in wjlist:
                    try:
                        wjf=re.match(r"(.*?)_(.*)",wj).group(1)
                    except:
                        wjf=wj
                    newname=newname+"+"+wjf
                print("===============================================================================================")
                print("你要合并的是【"+newname+"】，再次输入ok确认，否则取消。")
                justdo = input(">>【"+newname+"】>>")
                if justdo == "ok":
                    return wjlist,newname
                else:
                    #wjlist=[]#取消清空表格，没必要
                    newname=""#取消重置名字，有必要
            

        elif not wjname in htmlist:
            print("格式错误！请输入目录中的文件名！返回上级输入back，删除列表输入dele,选择完毕后输入ok")
        else:
            wjlist.append(wjname)
            print(">>","表格喜+1！")

  
    return wjlist,newname



  
#####功能4目录

def checkdiffer(htmlist):
    wjlist=[]
    newname=""
    while True:
        print('==========只想看甲出场而不想看到乙？也不想看到丙？==========')
        print('e.g.【某某某_list.html】,返回上级输入back，删除列表输入dele,选择完毕后输入ok')
        wjname = input('>>'+str(wjlist))
        if wjname == "back":
            break
        elif wjname == "dele":
            wjlist = wjlist[0:-1]
        elif wjname == "ok":
            if not wjlist ==[]:
                for wj in wjlist:
                    try:
                        wjf=re.match(r"(.*?)_(.*)",wj).group(1)
                    except:
                        wjf=wj
                    newname=newname+"-"+wjf
                print("===============================================================================================")
                print("你要查询是【"+newname+"】，以第一个为主体，再次输入ok确认，否则取消。")
                justdo = input(">>【"+newname+"】>>")
                if justdo == "ok":
                    return wjlist,newname
                else:
                    #wjlist=[]#取消清空表格，没必要
                    newname=""#取消重置名字，有必要
            

        elif not wjname in htmlist:
            print("格式错误！请输入目录中的文件名！返回上级输入back，删除列表输入dele,选择完毕后输入ok")
        else:
            wjlist.append(wjname)
            print(">>","表格喜+1！")

  
    return wjlist,newname

##########################################【主目录】 

def checkhtml():

    htmlist=[]   
    for root, dirs, files in os.walk(filethepath):  
        for file in files:  
            if os.path.splitext(file)[1] == '.html':  
                htmlist.append(os.path.join(file))
    #print(htmlist)
    print("===============================================================================================")
    if htmlist == []:
        print("第一次使用？当前目录下没有任何角色出场文件！")
    else:
        print('==========当前拥有角色出场文件包括==========')
        for ht in htmlist:
            print (ht)

    return htmlist


def main():
    s1='''==========欢迎使用dcdatabase出场查询机by江江==========
==========建议将本exe放置在单独文件夹中！==========
==========文件储存在子目录dcdatabase中=========='''
    s2='''==========请选择功能==========
1>>第一次使用，生成单人角色出场汇总文件（前置功能，需联网，可能稍微耗时）
2>>比较两个及以上单人出场汇总文件，得出实际共同出场刊物（实际主要功能，交集）
3>>你需要合并内容吗？例如将某角色的p52和n52两个文件合并在一起（补充功能，并集）
4>>只想看甲出场而不想看到乙？也不想看到丙？（补充功能，补集）'''


    print(s1)
    while True:
        htmlist = checkhtml()
        print(s2)
        option = input('==========请选择功能>>1 or 2 or 3 or 4 or quit?\n>>' )
        
        if option is '1':
            print('11111')
            forurl,urname=checkpage()
            if not forurl =="back":
                print("运行程序1")
                print(forurl,urname)
                try:
                    downlist(forurl,urname)
                except:
                    print("【！】【！】【！】网络错误！请稍后再试！请检查网络连接！请检查输入网址！【！】【！】【！】")
                    print("【！】【！】【！】可能是：1)请求太频繁，2)你的信号不好，3)输入网址有误！【！】【！】【！】")
                    
        elif option is '2':
            print('22222')
            wjlist,newname=checkinter(htmlist)
            print(wjlist,newname)
            if not wjlist ==[]:
                print("运行程序2")
                interlist(wjlist,newname)
                #break
                
        elif option is '3':
            print("3333")
            wjlist,newname=checkunion(htmlist)
            print(wjlist,newname)
            if not wjlist ==[]:
                print("运行程序3")
                unionlist(wjlist,newname)

        elif option is '4':
            print("44444")
            wjlist,newname=checkdiffer(htmlist)
            print(wjlist,newname)
            if not wjlist ==[]:
                print("运行程序4")
                differlist(wjlist,newname)
                
        elif option == 'quit':
            return False
        else:
            gooutt = input('选择无效，如果想退出程序，请输入quit或直接点击直接点右上角>>')
            if gooutt == 'quit':
                return False

    print("不填break就不会跳出来")        
        

main()
#addtwolist("1.html","2.html")

#downlist("https://dc.fandom.com/wiki/Category:Timothy_Drake_(New_Earth)/Appearances","timtest")
