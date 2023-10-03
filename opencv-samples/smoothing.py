import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src = cv.imread('opencv-logo.jpg')
assert src is not None, "file could not be read, check with os.path.exists()"

# チャンネルの変換（OpenCVはBGR、matplotlibはRGBで順序が異なるため）
img = cv.cvtColor(src, cv.COLOR_BGR2RGB)

# すべての要素が1/25である5x5行列
kernel = np.ones((5,5),np.float32)/25

# 畳み込みフィルターにより画像を生成
dst = cv.filter2D(img,-1,kernel)

# matplotlibにより描画
plt.subplot(121)
plt.imshow(img)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(dst)
plt.title('Averaging')
plt.xticks([])
plt.yticks([])
plt.show()