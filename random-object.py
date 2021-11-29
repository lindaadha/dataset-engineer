import cv2

image_path='object/acc40035.png'
label_path ='object/acc40035.txt'
img = cv2.imread(image_path)
dh, dw, _ = img.shape

fl = open(label_path,'r')
data = fl.readlines()
fl.close()

for datas in data:
    _, x, y, w, h = map(float, datas.split(' '))

    l = int((x - w / 2) * dw)
    r = int((x + w / 2) * dw)
    t = int((y - h / 2) * dh)
    b = int((y + h / 2) * dh)
    
    if l < 0: #left
        l = 0
    if r > dw - 1: #right
        r = dw - 1
    if t < 0: #top
        t = 0
    if b > dh - 1: #bottom
        b = dh - 1

    cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)

cv2.imshow('out',img)
cv2.waitKey(0)
cv2.destroyAllWindows()