import pandas as pd
import numpy as np
import tensorflow as tf

csv = pd.read_csv("bmi.csv")

# 학습시키기 위하여 label의 종류 3가지(fat, normal, thin)를 one-hot Encoding
# print(csv['height'].max(), csv['height'].min())   # 200 / 120
# print(csv['weight'].max(), csv['weight'].min())   # 80 / 35

# 키와 몸무게 기본값들이 170, 57 등으로 값의 부피가 크므로 정규화 (값의 범위를 0~1 사이의 값으로 줄임)
csv['height'] = csv['height'] / 200         # 키의 최대값이 200
csv['weight'] = csv['weight'] / 100         # 몸무게가 최대값이 80을 넘지 않기 때문

# print(csv['height'].max(),csv['height'].min())   # 1.0 / 0.6
# print(csv['weight'].max(),csv['weight'].min())   # 0.8 / 0.35

# 답의 종류를 직접 01로 바꿈 (레이블을 배열로 변환)
bclass = {"thin": [1, 0, 0], "normal": [0, 1, 0], "fat": [0, 0, 1]}
csv["label_pat"] = csv["label"].apply(lambda x : np.array(bclass[x]))

# 테스트를 위한 데이터 분류
test_csv = csv[15000:20000]
test_pat = test_csv[["weight", "height"]]
test_ans = list(test_csv["label_pat"])

# 데이터 플로우 그래프 구출
# 플레이스 홀더 선언
x = tf.placeholder(tf.float32, [None, 2])       # 키와 몸무게 데이터 넣기
y_ = tf.placeholder(tf.float32, [None, 3])      # 정답 레이블 넣기

# 변수 선언 (0으로 채움)
W = tf.Variable(tf.zeros([2, 3]))       # 가중치: [피쳐수 / 답의 수]
b = tf.Variable(tf.zeros([3]))          # bias: [답의 수]

# 소프트맥스 회귀 정의 (자동으로 가중치와 기준치를 만듦)
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 모델 훈련
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(cross_entropy)

# 정답 구하기
predict = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

# 세션 시작
sess = tf.Session()
sess.run(tf.global_variables_initializer())     # 변수 초기화

# 학습 시키기 (W와 b를 알기 위함, feature 마다 가중치가 얼마인지 bias는 얼마인지를 알기 위함)
for step in range(3500):
    i = (step * 100) % 14000            # i는 0, 100, 200 ~ 14900
    rows = csv[1 + i : 1 + i + 100]     # i번째부터 100개씩

    x_pat = rows[["weight", "height"]]
    y_ans = list(rows["label_pat"])
    fd = {x: x_pat, y_: y_ans}
    sess.run(train, feed_dict=fd)

    if step % 500 == 0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x: test_pat, y_: test_ans})
        print("step = ", step, "cre = ", cre, "acc = ", acc)

# 최종 정답률 구하기
acc = sess.run(accuracy, feed_dict={x: test_pat, y_: test_ans})
print("정답률 = ", acc)

# 데이터 177, 61, normal 테스트
w1 = sess.run(W)          # 구해진 값을 y = Wx + b에 대입이 가능함
b1 = sess.run(b)

x1 = np.array([[61/100, 177/200]], np.float32)        # weight / height 순서로 (단, 마찬가지로 정규화 과정이 필요함!)
y1 = tf.matmul(x1, w1) + b1         # 행렬 곱을 수행하는 함수

predict1 = tf.argmax(y1, 1)         # 나온 결과를 argmax로 만들어줌 (반환값은 0, 1, 2로 자리값을 나타냄)
print(sess.run(predict1))
sess.close()

