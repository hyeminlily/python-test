import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = open("by_mun.txt")
text = file.read()
file.close()

font_path = 'C:/Users/Reina/BareunDotum1.ttf'
cloud = WordCloud(font_path=font_path, background_color='white', width=800, height=600).generate(text)
cloud.words_

plt.imshow(cloud)
plt.axis('off')
plt.show()
