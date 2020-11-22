from nltk.corpus import stopwords 
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

frequency = dict()
stop_words = set(stopwords.words('dutch'))

colors= lambda *args, **kwargs: (128,0,128)

with open('vlant.txt', 'r') as file:
    for line in file:
        split_line = line.split(':')
        if len(split_line) == 3:
            content = split_line[2].strip().lower()
            if content != "<media weggelaten>":
                for word in content.split():
                    if word not in stop_words:
                        if word not in frequency.keys():
                            frequency[word] = 1
                        else:
                            frequency[word] += 1

cloud = WordCloud(width=1000, 
    height=1000,
    min_font_size=6, 
    max_words=1000, 
    background_color="white", 
    color_func=colors).generate_from_frequencies(frequency)

plt.figure()
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('vlant.png')