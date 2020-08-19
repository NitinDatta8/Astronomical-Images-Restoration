# Astronomical-Images-Restoration
This project is about generating nearly original images using convoluted images by using Pix-2-Pix GAN.

As the dataset is private I cannot share the images here. 

# Steps to run the project

1. We will create an environment to replicate the desired effects.
2. Place the file "tf.yml" in a directory.
3. In anaconda prompt go to the directory and run the command `conda env create -v -f tf.yml`
4. After the environment is created run the command `conda activate tf`
5. Run the command `pip install opencv-python` after step 4
6. Now navigate inside TF_pix2pix and run `preprocessing.py` with appropriate arguments to generate the necessary files required for training 
7. Run `pix2pix.py` with appropriate arguments for training the model

# Directory structure 
```
Astronomical-Images-Restoration
|
|----real_images # original images 
|	|
|	|----train # original training images
|	|
|	|----test # only 1 test image
|
|----conv_images # convoluted images
|	|
|	|----train # convoluted training images
|	|
|	|----test # only 1 test image
|
|----pix2pix.py # main training code 
|
|----preprocessing.py # preprocessing code 
|
|----tf.yml # file used to create new environment in anaconda with required specifications
```
