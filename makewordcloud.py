# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:19:37 2019
Mission:world cloud
@author: Lenovo
"""
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
def stop_words(text_word):
    words_list = []
    word_generator = jieba.cut(text_word, cut_all=False)  # 返回的是一个迭代器
    with open('./stopwords.txt') as f:
        unicode_text = f.read()
        f.close()  
    for word in word_generator:
        if word.strip() not in unicode_text:
            words_list.append(word)
    return ' '.join(words_list)  

back_color = plt.imread('background.jpg')  
wc = WordCloud(background_color='white',  
               max_words=1000,  
               mask=back_color,  
               max_font_size=100,  
               stopwords=STOPWORDS.add('蒋校长'),  
               font_path="C:/Windows/Fonts/simfang.ttf", 
               random_state=42,  
               )
text = open('./data.txt').read()
text = stop_words(text)
jieba.load_userdict('NoCut.txt')
wc.generate(text)
image_colors = ImageColorGenerator(back_color)
plt.imshow(wc)
plt.axis('off')
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('on')
wc.to_file('WordCloud_out.png') 