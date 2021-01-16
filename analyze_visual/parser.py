'''
This script is used to predict video's class. 

Usage example:

python3 train.py -v dataset/trump.mp4 -v SVM

Available algorithms for traning: SVM, Decision_Trees, KNN, Adaboost,
Extratrees, RandomForest
'''
import sys
import pickle
import argparse
import os.path
from os import path
import numpy as np
sys.path.insert(0, '..')
from analyze_visual.analyze_visual import process_video

def parse_arguments():
    """Parse arguments for real time demo.
    """
    parser = argparse.ArgumentParser(description="Parser"
                                                 "Predict shot class")
    parser.add_argument("-f", "--file", required=True, nargs=None,
                        help="File")

    parser.add_argument("-m", "--model", required=True, nargs=None,
                        help="Model")

    return parser.parse_args()

def model_predict(features,model):
    """
    Loads pre-trained model and predict shot's class
    :param features: features
    :return:
    """
    loaded_model = pickle.load(open('trained_'+str(model)+'.sav', 'rb'))

    result = loaded_model.predict(features)

    print('This shot is: ', result)


if __name__ == "__main__":

    args = parse_arguments()
    shot = args.file
    model = args.model
    print(shot)

    if path.exists(str(shot)+'_shot_features.npy'):
        features_stats = np.load(str(shot)+'_shot_features.npy')
        features = features_stats.reshape(1,-1)
    else:
        features_stats = process_video(shot, 2, True, True, True)
        features = features_stats[0]
        features = features.reshape(1,-1)

    model_predict(features,model)



    

    