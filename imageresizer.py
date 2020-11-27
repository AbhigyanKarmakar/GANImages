# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:06:48 2020

@author: Abhigyan
"""
import cv2
import argparse
import os

def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename), cv2.IMREAD_UNCHANGED)
        if img is not None:
            images.append(img)
            filenames.append(str(folder)+str(filename))
    return filenames , images

def resize(w, images, prefix, verbosity):

    for i in range(len(images)):
        img=images[i]
        print('\nOriginal Dimensions : ',img.shape)
        scale_percent = (w*100)/img.shape[1]
        width = w
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
    
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
         
        print('Resized Dimensions : ',resized.shape)
         
        if (verbosity):
            cv2.imshow("Resized image", resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows() 
        print("Writing : ",os.getcwd()+"\\"+str(i)+prefix+"_resized.jpg")
        cv2.imwrite(os.getcwd()+"\\"+str(i)+prefix+"_resized.jpg",resized)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--content_image", type=str, help="\t\t\t\tContent image name", default="content.jpg")
    parser.add_argument("--verbosity", type=int, help="\t\t\t\tWhether to show each processed image", default=0)
    parser.add_argument("--imgwidth", type=int, help="\t\t\t\tImage width after resizing", default=700)
    parser.add_argument("--imgloc", type=str, help="\t\t\t\tImage folder", default=str(os.getcwd()))
    parser.add_argument("--nameprefix", type=str, help="\t\t\t\tPrefix name for images", default="resized")
    
    args = parser.parse_args()
	
    filenames, images = load_images_from_folder(args.imgloc)
    resize(args.imgwidth, images, args.nameprefix, args.verbosity)
    