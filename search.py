import torch
import clip
from PIL import Image
import cv2
import os
import argparse

device = "cuda" if torch.cuda.is_available() else "cpu"

if device == "cuda":
    torch.cuda.empty_cache()
    
model, preprocess = clip.load("ViT-B/32", device=device)

parser = argparse.ArgumentParser(description='Image Search')
parser.add_argument('-p', '--path', type=str, default='images/', help='Path to Image folder')
parser.add_argument('-q', '--query', type=str, default='Green hills', help='Search Query')
parser.add_argument('-c', '--count', type=int, default=3, help='Number of images to return')

args = parser.parse_args()

images_path = None

def read_images(path):
    global images_path
    images_path = os.listdir(path)
    images = torch.empty((len(images_path),3,224,224))
    
    for i, img_path in enumerate(images_path):
        img = Image.open(path+img_path)
        images[i] = preprocess(img)
        
    images = images.to(device)
    return images

def tokenize_text(search_query):
    search_query = clip.tokenize(search_query).to(device)
    return search_query

def find_images(images, search_query, result_count):
    with torch.no_grad():
        img_probs, query_probs = model(images, search_query)
        idxs = (-query_probs).argsort().cpu().numpy()[0][:result_count]
    
    for idx in idxs:
        print(images_path[idx])
        img = cv2.imread(args.path+images_path[idx])
        img_resize = cv2.resize(img, (500,500))
        cv2.imshow(images_path[idx], img_resize)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

images = read_images(args.path)
search_query = tokenize_text(args.query)

find_images(images, search_query, args.count)