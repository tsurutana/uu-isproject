import cv2 as cv
# 数値計算ライブラリnumpyをnpという名前で使用
import numpy as np
# データ可視化ライブラリmatplotlibから図を作成するpyplotモジュールを読み込む
from matplotlib import pyplot as plt

# 画像の読み込み
img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
# メディアンフィルターによるノイズ除去
img = cv.medianBlur(img,5)

# しきい値処理
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)

# 出力図に用いるタイトル
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

# 出力する画像のリスト（配列）
images = [img, th1, th2, th3]

# 画像を並べて一つの図を作る
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
 
# 図を表示
plt.show()