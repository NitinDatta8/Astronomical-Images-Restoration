# python preprocessing.py --path "C:\Users\movva\Desktop\ML\Research Papers\Astronomy\TF_pix2pix"

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path',type=str, help='path for folder')

opt = parser.parse_args()
PATH = opt.path
real_path = PATH+'/real_images/'
conv_path = PATH+'/conv_images/'
rgb_path = PATH+'/RGB_images/'
comb_path = PATH+'/combined_images/'
if not os.path.exists(rgb_path):
    os.makedirs(rgb_path)
if not os.path.exists(rgb_path+"/train"):
	os.makedirs(rgb_path+"/train")
if not os.path.exists(rgb_path+"/test"):
	os.makedirs(rgb_path+"/test")	
if not os.path.exists(comb_path):
    os.makedirs(comb_path)
if not os.path.exists(comb_path+"/train"):
	os.makedirs(comb_path+"/train")
if not os.path.exists(comb_path+"/test"):
	os.makedirs(comb_path+"/test")

sub_path = ['train','test']

for sub in sub_path:
    for i in os.listdir(real_path+sub):
#         print(real_path+sub+'/'+i)
        img = cv2.imread(real_path+sub+'/'+i,cv2.IMREAD_GRAYSCALE) 
        backtorgb = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
#         plt.imshow(backtorgb)
        cv2.imwrite(rgb_path+sub+'/'+i, backtorgb)
    conv = os.listdir(conv_path+sub)
    tar = os.listdir(rgb_path+sub)
    conv.sort()
    tar.sort()
    for i,j in zip(conv,tar):
        p1 = conv_path+sub+'/'+i
        p2 = rgb_path+sub+'/'+j
        img1 = cv2.imread(p1)
        img2 = cv2.imread(p2)
        vis = np.concatenate((img1, img2), axis=1)
        cv2.imwrite(comb_path+sub+'/'+i, vis)    

