# CourseraFinalProject

Final Project in Automation Real-World Tasks with Python

## Introduction

You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

When the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.

## What you’ll do

- Write a script that summarizes and processes sales data into different categories
- Generate a PDF using Python
- Automatically send a PDF by email
- Write a script to check the health status of the system

## Fetch supplier data

```zsh
$ sudo chmod +x download_bucket_file.sh
$ ./download_bucket_file.sh
$ ls
... supplier-data.tar.gz
```

## Extract supplier data

```zsh
$ tar xf ~/supplier-data.tar.gz
$ ls
... supplier-data
$ ls supplier-data/
... descriptions images
```

## Work with supplier images

- filename : changeImage.py
- goals:
  - size : 3000x2000 to 600x400 pixel
  - format : .tiff to .jpeg
  - grant executable permission to this file and run it

```zsh
$ sudo chmod +x ~/changeImage.py
$ ./changeImage.py
# check the specification of images
$ file ~/supplier-data/images/003.jpeg
...
```

## Upload Images to web server

- filename : example_upload.py
- goals:
  - upload a file using requests module
  - file upload url 'http://localhost/upload/'
  - grant executable permission to this file and run it
  - file check url 'http://localhost/media/images'

```zsh
$ sudo chmod +x ~/example_upload.py
$ ./example_upload.py
# check if file is uploaded to the web server using file check url 
```
