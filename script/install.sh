#creating and activating conda env

conda create -n image_search
conda activate image_search

#installing pytorch and CLIP
conda install --yes -c pytorch pytorch=1.7.1 torchvision cudatoolkit=11.0
pip3 install ftfy regex tqdm
pip3 install git+https://github.com/openai/CLIP.git

#downloading one of the available clip model
python3 load_model.py