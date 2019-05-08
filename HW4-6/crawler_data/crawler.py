import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import pickle

data1=list()

for i in range(296,347):  #296~346

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data1.append({'novel':'天龙八部','title':title_str, 'text':article_str})
    print(i)
with open('1.pkl', 'wb') as f:
    pickle.dump(data1, f)
    
data2=list()   
for i in range(349,389):  #349~388

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data2.append({'novel':'笑傲江湖','title':title_str, 'text':article_str})
    print(i)
with open('2.pkl', 'wb') as f:
    pickle.dump(data2, f)

data3=list()   
for i in range(391,392):  #391

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data3.append({'novel':'越女剑','title':title_str, 'text':article_str})
    print(i)
with open('3.pkl', 'wb') as f:
    pickle.dump(data3, f)

data4=list()
for i in range(394,414):  #394~413

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data4.append({'novel':'书剑恩仇录','title':title_str, 'text':article_str})
    print(i)
with open('4.pkl', 'wb') as f:
    pickle.dump(data4, f)

data5=list()
for i in range(416,428):  #416~427

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data5.append({'novel':'连城诀','title':title_str, 'text':article_str})
    print(i)
with open('5.pkl', 'wb') as f:
    pickle.dump(data5, f)

data6=list()    
for i in range(430,431):  #430

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data6.append({'novel':'白马啸西风','title':title_str, 'text':article_str})
    print(i)
with open('6.pkl', 'wb') as f:
    pickle.dump(data6, f)

data7=list()    
for i in range(432,452):  #432~451

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data7.append({'novel':'碧血剑','title':title_str, 'text':article_str})
    print(i)
with open('7.pkl', 'wb') as f:
    pickle.dump(data7, f)

data8=list()    
for i in range(455,463):  #455~462

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data8.append({'novel':'雪山飞狐','title':title_str, 'text':article_str})
    print(i)
with open('8.pkl', 'wb') as f:
    pickle.dump(data8, f)

data9=list()    
for i in range(464,484):  #464~483

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data9.append({'novel':'飞狐外传','title':title_str, 'text':article_str})
    print(i)
with open('9.pkl', 'wb') as f:
    pickle.dump(data9, f)

data10=list()    
for i in range(485,525):  #485~524

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data10.append({'novel':'神雕侠侣','title':title_str, 'text':article_str})
    print(i)
with open('10.pkl', 'wb') as f:
    pickle.dump(data10, f)

data11=list()    
for i in range(527,549):  #527~548

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data11.append({'novel':'侠客行','title':title_str, 'text':article_str})
    print(i)
with open('11.pkl', 'wb') as f:
    pickle.dump(data11, f)

data12=list()    
for i in range(550,551):  #550

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data12.append({'novel':'鸳鸯刀','title':title_str, 'text':article_str})
    print(i)
with open('12.pkl', 'wb') as f:
    pickle.dump(data12, f)

data13=list()    
for i in range(552,602):  #552~601

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data13.append({'novel':'鹿鼎记','title':title_str, 'text':article_str})
    print(i)
with open('13.pkl', 'wb') as f:
    pickle.dump(data13, f)

data14=list()    
for i in range(605,645):  #605~644

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data14.append({'novel':'射雕英雄传','title':title_str, 'text':article_str})
    print(i)
with open('14.pkl', 'wb') as f:
    pickle.dump(data14, f)

data15=list()   
for i in range(649,689):  #649~688

    URL='https://www.xiaoshuokan.com/haokan/7540/2365'+str(i)+'.html'
    
    resp=requests.get(URL)
    soup=BeautifulSoup(resp.text, 'html.parser',from_encoding='utf-8')
    
    #print(soup)
    title=soup.find_all('title')
    title_str=title[0].text
    #print(title_str)
    article=soup.find_all('div',style="margin:3px auto;padding:0px;width:100%;line-height:55px")
    #print((article[0].text)) #本文
    article_str=article[0].text
    data15.append({'novel':'倚天屠龙记','title':title_str, 'text':article_str})
    print(i)
with open('15.pkl', 'wb') as f:
    pickle.dump(data15, f)
    
for i in range(1,16):
    print(data[i]['novel'])


with open('1.pkl', 'rb') as f:
    first = pickle.load(f)
df=pd.DataFrame.from_dict(first)
for i in range(2,16):
    with open(''+str(i)+'.pkl', 'rb') as f:
        all_data = pickle.load(f)
    df1=pd.DataFrame.from_dict(all_data)
    df=df.append(df1,ignore_index=True)

def remove_someword(string):
    string=re.sub('金庸作品集-','',string)
    string=re.sub('-金庸-都市小说','',string)
    return string
    
df.title=df.title.apply(remove_someword)

with open('Jing_yong_novel.pkl', 'wb') as f:
    pickle.dump(df, f)
