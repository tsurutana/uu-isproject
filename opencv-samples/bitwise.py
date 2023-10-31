import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 左に白い円が描いてある画像を生成
left = np.zeros((200, 300), dtype="uint8")
cv.circle(left, (100, 100), 80, 255, -1)
# 右に白い円が描いてある画像を生成
right = np.zeros((200, 300), dtype="uint8")
cv.circle(right, (200, 100), 80, 255, -1)

# 各種の論理演算
bitwise_and = cv.bitwise_and(left, right)
bitwise_or = cv.bitwise_or(left, right)
bitwise_xor = cv.bitwise_xor(left, right)
bitwise_not = cv.bitwise_not(bitwise_xor)

# 出力図に用いるタイトル
titles = ['Img 1', 'Img 2', 'AND', 'OR', 'XOR', 'NOT']

# 出力する画像のリスト（配列）
images = [left, right, bitwise_and, bitwise_or, bitwise_xor, bitwise_not]

# 画像を並べて一つの図を作る
for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

# 図を表示
plt.show()