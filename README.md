# DATASET ENGINEER

This repository can be used to data preparation such as: video to frame, Labeling Image  Please update requirement if you have change any method for this Dataset Engineer folder.

## Features
- Labeling Image with LabelImg or CVAT
- Preparation Data for Training 
-- Video to Frame 
-- Train Test Split Data
-- Edit classes Labeling TXT (Change, Swap, Delete)
-- Counter object classes
- Training and Testing (YoloV4 and YoloR)

### Labeling Image 
Labeling Image digunakan untuk Anotasi Image, bisa menggunakan dua tools berikut:
- [LabelImg](https://github.com/tzutalin/labelImg) for offline Anotation
- [CVAT]() for online Annotation

### Preparation Data for Training
#### _Video to Frame_
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

#### _Train Test Split Data_
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

#### _Edit Classes for TXT File_
== SKIP == 
programnya ada yang mau diedit

#### _Counter Object Classes_
Program ini digunakan untuk menghitung jumlah objek class yang akan di Training, gunanya untuk memudahkan dalam pemrataan jumlah setiap Class Objek yang digunakan 
Berikut command line yang digunakan 
```sh
python counter.py -i "Directory_Path" -c 0*
```
__*Note__: Untuk Classes (-c) disesuaikan dengan objek class yang akan dihitung

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


Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech

Dillinger uses a number of open source projects to work properly:

- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
