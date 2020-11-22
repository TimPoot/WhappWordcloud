from nltk.corpus import stopwords 
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

frequency = dict()
stop_words = set(stopwords.words('dutch'))
filter_words = set(["weggelaten", "audio", "video", "‎afbeelding"])

cloud_mask = np.array(Image.open("cloud.png"))
colors= lambda *args, **kwargs: (128,0,128)

with open('cookies_groot.txt', 'r') as file:
    for line in file:
        split_line = line.split(']')[-1].split(':')
        if len(split_line) == 2:
            content = split_line[1].strip().lower()
            for word in content.split():
                if word not in stop_words and word not in filter_words:
                    if word not in frequency.keys():
                        frequency[word] = 1
                    else:
                        frequency[word] += 1

cloud = WordCloud(width=1000, 
    height=1000,
    min_font_size=6, 
    max_words=300, 
    background_color="white",
    mask=cloud_mask).generate_from_frequencies(frequency)

plt.figure(figsize=(10,10), dpi=400)
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('cookies_groot.png', format='png')