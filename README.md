# DATASET ENGINEER

This repository can be used to data preparation such as: video to frame, Labeling Image  Please update requirement if you have change any method for this Dataset Engineer folder. Thank You :)

## Features
- Labeling Image with LabelImg or CVAT
- Preparation Data for Training 
-- Video to Frame 
-- Train Test Split Data
-- Edit classes Labeling TXT (Change, Swap, Delete)
-- Counter object classes
-- Random Erasing
-- Augmentor 
- Training and Testing (YoloV4 and YoloR)

### Labeling Image 
Labeling Image digunakan untuk Anotasi Image, bisa menggunakan dua tools berikut:
- [LabelImg](https://github.com/tzutalin/labelImg) for offline Anotation
- [CVAT]() for online Annotation

### Preparation Data for Training
#### _A. Video to Frame_
digunakan untuk mengubah video menjadi frame, untuk langkah-langkahnya dapat diikuti sebagai berikut: 
1. Ubah directory _videoPath_ sesuai dengan path directory yang akan diubah 
```sh
videoPath = "Directory Path"
```
2. Sesuaikan extension file video yang akan diubah (mp4, avi) 
```sh
data_path = os.path.join(videoPath,'*mp4') #extension video
```
3. Ubah durasi count sesuai dengan FPS yang terdapat di video
__Contoh__ : video memiliki durasi 24 FPS. Maka dengan menggunakan count 12, setiap detik yang diambil kurang lebih 2 frame 
```sh
if count%12==0:
```
4. Ubah extension frame file sesuai yang dibutuhkan (jpg, jpeg, png)
```sh
cv2.imwrite( pathOut + "%03d.png" % name, image) #extension frame 
```
5. Pastikan directory path di line code berikut sudah disesuaikan untuk menyesuaikan path output yang sama dengan lokasi input videonya
```sh
 os.mkdir("Directory Path/%s" % tailname)
        dir="Directory Path/%s/" % tailname
```
6. Ubah "change_name" setiap menjalankan program ini, untuk menghindari adanya kesamaan nama file dalam proses data training
```sh
 name=extractImages(f,dir+"change_name"+str(i),c)
```
7. Program dapat dijalankan.

#### _B. Train Test Split Data_
Fitur ini digunakan untuk membagi data Train dan Test sebelum masuk proses ke dalam proses Training. Sebelum menjalankan program ini pastikan untuk Gambar dan TXT/XML (labeling result) dijadikan dalam satu folder.
Berikut adalah cara untuk menjalankan program ini:
1. Ubah lokasi directory path folder sesuai dengan lokasi folder yang akan di training
```sh
current_dir = 'Directory Path/all_images/'
```
2. Code Line ini digunakan untuk menentukan jumlah Test yang akan digunakan, dengan begitu jika yang digunakan test=20, maka untuk data trainingnya adalah 80%
__Note__: Biasanya yang digunakan umumnya adalah test=20% dan training=80%, ataupun test=10% dan training=90%, tergantung dari jumlah data ataupun instruksi AI Engineer.
```sh
# Percentage of images to be used for the test set
percentage_test = 20
```
3. Tentukan lokasi path untuk membuat file train dan test 
__Note__: Lokasi disamakan saja dengan folder gambar training
```sh
file_train = open('Directory Path/train.txt', 'w')
file_test = open('Directory Path/test.txt', 'w')
```
4. Sesuaikan extension file gambar yang digunakan (jpg, jpeg, png)
```sh
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpeg")):
```
5. Sesuaikan dengan directory path gambar yang ada, dan extension file gambar yang sama 
```sh
file_test.write("Directory Path/all_images" + "/" + title + '.jpeg' + "\n")
file_train.write("Directory Path/all_images" + "/" + title + '.jpeg' + "\n")
```
6. Program dapat dijalankan 

#### _C. Edit Classes for TXT File_
terdapat beberapa fitur yang bisa digunakan dalam program ini untuk mengedit nilai class atau pun array dalam format YOLO Txt. 
1. Change Class = Mengganti nilai kelas 
```sh
python all-edit-txt.py -i "Directory Input Path" -c -o "Nilai Kelas Lama" -n "Nilai Kelas Baru"
```
2. Swap Class = Menukar nilai kelas
```sh
python all-edit-txt.py -i "Directory Input Path" -s -o "Nilai Kelas yang akan ditukar" -n "Dengan Nilai yang baru akan ditukar"
```
4. Delete Class = Menghapus nilai kelas
```sh
python all-edit-txt.py -i "Directory Input Path" -d -dc "Nilai Kelas yang akan dihapus" 
```
5. Add Class = Menambah nilai kelas 
```sh
python all-edit-txt.py -i "Directory Input Path" -a -ac "Jumlah nilai yang akan ditambahkan"
```
__*Note__: Yang dimaksud Nilai adalah nilai array kelas yang terdapat diurutan classes


#### _D. Counter Object Classes_
Program ini digunakan untuk menghitung jumlah objek class yang akan di Training, gunanya untuk memudahkan dalam pemrataan jumlah setiap Class Objek yang digunakan 
Berikut command line yang digunakan 
```sh
python counter.py -i "Directory_Path" -c 0*
```
__*Note__: Untuk Classes (-c) disesuaikan dengan objek class yang akan dihitung

#### _E. Random Erasing_
Program ini digunakan untuk memberikan objek hitam di image untuk menambahkan augmentasi data 
**tambahin fotonya**
yang perlu diubah dalam program ini adalah:
- mengubah directory path inputnya 
```sh
path = 'divide/'
```
- mengubah directory path outputnya 
```sh
output_path = 'output/'
```
__*Note__: dalam program ini masih perlu membuat folder outputnya secara manual 

#### _F. Augmentor_
untuk menambahkan jumlah variasi data gambar dapat menggunakan "Widya Image Augmentor" yang dapat ditemukan di GitLab Perusahaan, atau
Menggunakan program Augmentor Offline yang terdapat beberapa fitur 
- Flip
- Blur
- Salt and Pepper

Yang perlu diperhatikan dalam menggunakan program ini perlu diganti adalah 
INPUT_PATH dan OUTPUT_PATH 
untuk menggunakan fitur yang ingin digunakan hanya perlu menjalankan cells yang akan digunakan 


### Training dan Testing YOLO 
___Setup and Instalation___
- For YoloV4 
-- Downloading github [YoloV4](https://github.com/AlexeyAB/darknet.git)
-- How to install YoloV4, you can following this [steps](https://robocademy.com/2020/05/01/a-gentle-introduction-to-yolo-v4-for-object-detection-in-ubuntu-20-04/).
- For YoloR 
-- Dowloading github [YoloR](https://github.com/WongKinYiu/yolor.git)
-- How to install YoloR, you can following this [steps](https://blog.roboflow.com/train-yolor-on-a-custom-dataset/).

___How to Train and Test___
- YoloV4 
-- For Training using YoloV4, you can following this [steps](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects).
-- 


