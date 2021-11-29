import cv2 
import random 
import math
import numpy as np 
import os
from tqdm import tqdm

def random_erasing(img, mean = [0.4914, 0.4822, 0.4465],sl = 0.02,sh = 0.05,r1 = 0.3):
        """sl: min erasing area
        sh: max erasing area
        r1: min aspect ratio
        mean: erasing value"""

        img = img.copy()
        

        for attempt in range(100):
            area = img.shape[0] * img.shape[1]
        
            target_area = random.uniform(sl, sh) * area
            aspect_ratio = random.uniform(r1, 1/r1)

            h = int(round(math.sqrt(target_area * aspect_ratio)))
            w = int(round(math.sqrt(target_area / aspect_ratio)))

            if w < img.shape[1] and h < img.shape[0]:
                x1 = random.randint(0, img.shape[0] - h)
                y1 = random.randint(0, img.shape[1] - w)
                if img.shape[2] == 3:
                    img[ x1:x1+h, y1:y1+w , 0] = mean[0]
                    img[x1:x1+h, y1:y1+w, 1] = mean[1]
                    img[ x1:x1+h, y1:y1+w, 2] = mean[2]
                else:
                    img[ x1:x1+h, y1:y1+w,0] = mean[0]
                return img

        return img

path = 'divide/'
output_path = 'output/'
imgs = os.listdir(path)

for img_name in tqdm(imgs):
    if img_name[-4:] in ['.png','.jpg','.jpeg']:
        img = cv2.imread(os.path.join(path,img_name))
        imgAug = random_erasing(img)

        cv2.imwrite(os.path.join(output_path,img_name),imgAug)

