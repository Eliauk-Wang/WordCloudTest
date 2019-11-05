#!/usr/bin/env python
# coding: utf-8

# In[82]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt
#导入所需库
f = open(r'C:\Users\WJ\Desktop\wordcloud\words.txt','r').read()
wordcloud = WordCloud(font_path="E:\资源\fonts\VIP和音液晶数字.ttf",background_color="#2d333d",width=1920, height=1080, margin=2).generate(f)

# width,height,margin可以设置图片属性
# generate 可以对全部文本进行自动分词,但是对中文支持不好
# 可以设置font_path参数来设置字体集
#background_color参数为设置背景颜色,默认颜色为黑色

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file(r'C:\Users\WJ\Desktop\wordcloud\wordcloud.png')
# 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存


# In[ ]:





# In[ ]:





# In[ ]:




