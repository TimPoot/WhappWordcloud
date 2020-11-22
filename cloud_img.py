from nltk.corpus import stopwords 
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

frequency = dict()
stop_words = set(stopwords.words('dutch'))

cloud_mask = np.array(Image.open("cloud.png"))
colors= lambda *args, **kwargs: (95, 2, 31)

with open('cookies.txt', 'r') as file:
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
    min_font_size=4, 
    max_words=200, 
    background_color="white", 
    mask=cloud_mask).generate_from_frequencies(frequency)

plt.figure(figsize=(10,10), dpi=400)
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('cookies.png', format='png')