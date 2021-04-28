# Image-Search

A python script to search an image in a folder by describing it in natural language. It uses [CLIP](https://github.com/openai/CLIP) to find the similar images as described in the search query.

## Installation

Clone the repository and change your working directory to project's root directory.

**_Note_:**
* _prior installation of [conda](https://www.anaconda.com/products/individual) is required_
* _Replace cudatoolkit=11.0 in the install.sh with the appropriate CUDA version on your machine or cpuonly when installing on a machine without a GPU._
```
cd script
./install.sh   
python search.py
```

Since the default query is 'Green hills', we now see three images containing hills with image name printed in terminal. You can pass your desired query to search for images in your custom directory.

## Arguments

|Arguments|Default|Description|
|---------|-------|-----------|
|-p, --path|images/|Path to Image folder|
|-q, --query|'Green hills'|Search Query|
|-c, --count|3|Number of images to return|

Hence, ```python3 search.py -p ~/py_works/notebooks/images/ -q 'Rainbow' -c 1``` returned a single image containing rainbow.

<img src="https://github.com/samiptimalsena/Image-Search/blob/master/demo.png" width="350" height="300" alt="demo image">
