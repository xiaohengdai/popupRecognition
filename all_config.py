# -*- coding: UTF-8 -*-


# close_popup_image shape
IMG_ROW, IMG_COL = 50, 50

# model train
batch_size = 30
num_classes = 2
epochs = 10

# model name
model_name = "model/trained_model_1.h5"

# close_popup_image path
CLOSE_POPUP_IMAGE_PATH = "close_popup_image/"
ABNORMAL_PAGE_IMAGE_PATH="abnormal_page_image/"
# IMAGE_PATH = "ios_update/good/"
TRAIN_PATH = "train/"
# TRAIN_PATH = "ios_update/"
PREDICT_PATH = "predict/"

# selective search
SCALE = 2.0
SIGMA = 0.8
MIN_SIZE = 80

# augmentation size for one class
augmentation_size = 350
