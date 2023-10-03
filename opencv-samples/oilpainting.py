import cv2 as cv

img = cv.imread('shoebill.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

# 油絵風フィルター
oil = cv.xphoto.oilPainting(img, size=7, dynRatio=1)

# 画像の表示（OpenCVのGUI機能を使用）
cv.imshow("Display window", oil)

# キー入力受付
k = cv.waitKey(0)
if k == ord("s"):
    # フィルター後の画像を保存
    cv.imwrite("shoebill-oilpainted.jpg", oil)