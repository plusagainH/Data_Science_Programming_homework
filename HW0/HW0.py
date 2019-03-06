import os
import pickle
import jieba
import operator
import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from datetime import datetime
from collections import Counter
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

#載入字型
font_path = 'msjh.ttc'
font = font_manager.FontProperties(fname='msjh.ttc',
                                   weight='bold',
                                   style='normal', size=16)

#載入爬蟲爬到的文章(pkl檔)，並存成list
with open('new_talk.pkl', 'rb') as f:
    data = pickle.load(f)
    
data = data[::-1]
contents = [news['content'] for news in data]   #文章本文

#stopwords是一些較無意義的詞
stopwords = []
with open('stopwords.txt', 'r', encoding='UTF-8') as file:
    for each in file.readlines():
        stopwords.append(each.strip())
    stopwords.append(' ')

#過濾出含有keyword的新聞文章
def news_containing_keyword(keyword, news_list):
    return list(filter(lambda news: keyword in news, news_list))

#從傳進的dictionary移除stopwords
def remove_stopwords_from_dict(word_dict, stopwords):
    for w in stopwords:
        word_dict.pop(w, word_dict)
    return word_dict

#移除標點符號，避免標點符號被算進字詞出現頻率
def remove_punctuation(content_string, user_pc=False):
    if(user_pc):
        punctuation = user_pc
    else:
        punctuation=list("!@#$%^&*()_+=-[]`~'\"|/\\abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;{}\r\xa0\u3000、，。「」！？；：<>")
        
    for p in punctuation:
        content_string = content_string.replace(p, " ")
    return(content_string)

#將jieba切好的文章字詞轉成dictionary(這個dictionary會記錄每個詞出現的次數)，且移除stopwords(較無意義的詞)
def lcut_to_dict(lcut):
    word_dict = dict(Counter(lcut))
    return(remove_stopwords_from_dict(word_dict, stopwords))

#利用jieba來分割傳入的文章，並且排除標點符號
def get_cutted_dict(list_of_news):
    cat = ' '.join(list_of_news)
    cat = remove_punctuation(cat)
    cutted = jieba.lcut(cat)
    return lcut_to_dict(cutted)

#藉由關鍵字和新聞內容輸出文字雲
def get_wordcloud_of_keywords(keywords, list_of_news, image_path=False):
    if type(keywords) == str:
        keywords = [keywords]
    #如果有傳入圖片則會以傳入的圖片為背景輸出文字雲，若沒有傳入圖片則會輸出方形文字雲
    if image_path:
        coloring = np.array(Image.open(os.path.join(image_path)))
        color_func = ImageColorGenerator(coloring)
        wc = WordCloud(max_font_size=30,
                       background_color="white",
                       mask=coloring,
                       color_func=color_func,
                       font_path=font_path,
                       width=1000, height=1000,
                      max_words=10000)
    else:
        wc = WordCloud(max_font_size=30,
                       background_color="white",
                       colormap='Set2',
                       font_path=font_path,
                       width=1000, height=300,
                      max_words=1000)
    
    keyword_news = news_containing_keywords(keywords, list_of_news)
    keyword_dict = get_cutted_dict(keyword_news)
    print(len(keyword_dict))   #印出關鍵字總數
    im = wc.generate_from_frequencies(keyword_dict)  
    return im

if __name__ == '__main__':
    tsai_wc = get_wordcloud_of_keywords('蔡英文', contents, 'tsai.png')
    tsai_wc.to_file('result.png')
