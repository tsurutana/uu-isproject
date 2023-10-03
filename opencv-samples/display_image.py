# OpenCVライブラリを読み込み、cvという名前で使用するという宣言
import cv2 as cv

# 画像の読み込み
img = cv.imread("./lena.jpg")

if img is None:
    sys.exit("Could not read the image.")

# 画像の表示（OpenCVのGUI機能を使用）
cv.imshow("Display window", img)

# キー入力受付
k = cv.waitKey(0)
if k == ord("s"):
    # PNG形式で保存
    cv.imwrite("lena.png", img)
