import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = open("by_mun.txt").read()
font_path = 'C:/Users/Reina/BareunDotum1.ttf'
cloud = WordCloud(font_path=font_path, background_color='white').generate(text)

plt.figure(figsize=(12, 12))
plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()

