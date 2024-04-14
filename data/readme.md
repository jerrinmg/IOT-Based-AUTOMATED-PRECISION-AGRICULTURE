# Data Folder README

## Overview
This project utilizes a dataset for training the machine learning model to classify potato diseases. Below are the details and instructions on how to access and use this data. This directory contains datasets used for the machine learning model that classifies images of potato diseases. The data is split into three subfolders:
- train/
- val/
- test/

## Description of Subfolders
- train/: Contains images used for training the model.
- val/: Contains images used for validating the model during training.
- test/: Contains images used to test the model after training.

## Source
Data was sourced from [Plant Village : Kaggle](https://www.kaggle.com/datasets/arjuntejaswi/plant-village)  
1000 Photos for potato late blight, 152 images for healthy plant and potato early blight is availble from the above source. 

## Pre-processing
Images are pre-processed as follows:
- Resized to 224x224 pixels.
- Normalized pixel values to the range [0, 1].

## Usage
Use the script `load_data.py` to load and preprocess the data for training and evaluation.
