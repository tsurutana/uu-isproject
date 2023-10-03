import cv2 as cv
# 数値計算ライブラリnumpyをnpという名前で使用
import numpy as np
# データ可視化ライブラリmatplotlibから図を作成するpyplotモジュールを読み込む
from matplotlib import pyplot as plt

# 画像の読み込み
img = cv.imread('gradient.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# しきい値処理（127より大きい値に対して、決まった計算をする）
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

# 出力図に用いるタイトル
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']

# 出力する画像のリスト（配列）
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# 画像を並べて一つの図を作る
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
 
# 図を表示
plt.show()