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
$ ls -l ~/
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

- filename : `changeImage.py`
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

- filename : `example_upload.py`
- goals:
  - upload a file using requests module
  - file upload url [http://localhost/upload/]
  - grant executable permission to this file and run it
  - file check url [http://localhost/media/images]

```zsh
$ sudo chmod +x ~/example_upload.py
$ ./example_upload.py
# check if file is uploaded to the web server using file check url
```

### upload supplier images to web server

- filename : `supplier_image_upload.py`
- goals:
  - upload all processed jpeg files to web server fruit catalog
  - grant executable permission to this file and run it

```zsh
$ sudo chmod +x ~/supplier_image_upload.py
$ ./supplier_image_upload.py
# refresh the file check url and check for uploaded images
```

## Upload description of the images

- goals:
  - check url [http://locahost/]
  - upload url [http://localhost/fruits]
  - enter test fruit content into content field in fruit catalog web-server
  - click on post button and visit check url for uploaded fruit

```json
{
  "name": "Test Fruit",
  "weight": 100,
  "description": "This is the description of my test fruit",
  "image_name": "icon.sheet.png"
}
```

### Create script to automate uploading descriptions

- filename : `run.py`
- goals:
  - script should return data in a json dictionary
  - convert lines int .txt file to following fields
  - fields: name, weight, description and image_name
  - iterate over all images and post them to web-server via upload url
  - grant executable permission to this file and run it

```zsh
$ sudo chmod +x ~/run.py
$ ./run.py
# check for uploaded descriptions in web-server at check url
```

## Generate PDF and Send to an email

- filename: `reports.py`
- goals:
  - generate a pdf file to send to supplier once images & descriptions are uploaded to web-server using reportlab module/library
  - complete the script
  - content should look like:

```txt
<b>Processed Update on <Today's date></b>
[blank line]
name: Apple
weight: 500 lbs
[blank line]
name: Avocado
weight: 200 lbs
[blank line]
...
```

### Process supplier fruit description data

- filename: `emails.py`
- goals:
  - create script with following email methods:
    - generate_email() -> email with attachment
    - generate_error_email() -> email without attachment
    - send_email() -> sends message to configured SMTP server

- filename: `report_email.py`
- goals:
  - to process this use os, datetime and reports libraries
  - text data from descriptions to above mentioned content format
  - generate summary for sending mail and semd email
  - grant executable permission and run 

```zsh
$ sudo chmod +x ~/report_email.py
$ ./report_email.py
# check webmail for new messages with attachment
```