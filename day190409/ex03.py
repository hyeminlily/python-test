import matplotlib.pyplot as plt
from wordcloud import WordCloud

f = open("i_have_a_dream.txt")
data = f.read()
f.close()

# 단어별 빈도수를 워드클라우드로 표현
cloud = WordCloud().generate(data)
plt.imshow(cloud)     # 이미지 객체 생성
plt.axis('off')       # 차트의 축 없애기
plt.show()

