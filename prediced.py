
'''
    Predicting Allosteric Site Residues in Proteins
    Input: Feature vector of the protein sequence
    Output: Residue IDs and probabilities of allosteric site residues

'''
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_score 
import warnings
import pickle 
import os
from matplotlib import pyplot
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import tensorflow.keras.layers as tfl

def predict_allosteric_sites(pdb_id, chain_id):
    # number of features
    feat_shape = 0

    with open("features_data/diversity/train_dataset_1.pkl", 'rb') as file:
        positive_set = pickle.load(file)

    with open("features_data/diversity/train_dataset_0.pkl", 'rb') as file:
        negative_set_entire = pickle.load(file)
    column_names = ['pdb_name','residue','features','label']
    # 确保 positive_set 和 negative_set_entire 是 DataFrame
    if isinstance(positive_set, dict):
        positive_set = pd.DataFrame.from_dict(positive_set)
    if isinstance(negative_set_entire, dict):
        negative_set_entire = pd.DataFrame.from_dict(negative_set_entire)

    Negative_Samples = negative_set_entire.sample(n=round(len(positive_set)*14), random_state=42)

    # combine positive and negative sets to make the final dataset
    Train_set = pd.concat([positive_set, Negative_Samples], ignore_index=True, axis=0)

    # collect the features and labels of train set
    np.set_printoptions(suppress=True)
    X_val = [0]*len(Train_set)
    for i in range(len(Train_set)):
        feat = Train_set['features'][i]
        X_val[i] = feat
    X_train_orig = np.asarray(X_val)

    # Generate a random order of elements with np.random.permutation and simply index into the arrays Feature and label 
    idx = np.random.permutation(len(X_train_orig))
    X_train = X_train_orig[idx]
    scaler = StandardScaler()
    scaler.fit(X_train) # fit on training set only
    X_train = scaler.transform(X_train) # apply transform to the training set

    with open(f"./Case Study/{pdb_id}_{chain_id}_dataset.pkl", 'rb') as file:
        test_set_entire = pickle.load(file)
    if isinstance(test_set_entire, dict):
        test_set = pd.DataFrame.from_dict(test_set_entire)
  

    X_independent = [0] * len(test_set)
    for i in range(len(test_set)):
        feat1 = test_set['features'][i]
        X_independent[i] = feat1
    X_test = np.asarray(X_independent)
    X_test = scaler.transform(X_test)
    feat_shape = X_test[0].size

    # CNN model
    def CNN_Model(feat_shape):
        model = tf.keras.Sequential()
        model.add(tfl.Conv1D(32, 3, padding='same', activation='relu', input_shape=(feat_shape,1)))
        model.add(tfl.BatchNormalization())
        model.add(tfl.Dropout(0.2)) 

        model.add(tfl.Conv1D(128, 3, padding='same',activation='relu'))
        model.add(tfl.BatchNormalization())
        model.add(tfl.Dropout(0.3)) 

        model.add(tfl.Conv1D(32, 5, padding='same',activation='relu'))
        model.add(tfl.BatchNormalization()) 
        model.add(tfl.Dropout(0.2)) 

        model.add(tfl.Conv1D(32, 3, padding='same',activation='relu'))
        model.add(tfl.BatchNormalization()) 
        model.add(tfl.Dropout(0.3)) 

        model.add(tfl.Flatten())
        model.add(tfl.Dense(128, activation='relu'))

        model.add(tfl.Dense(32, activation='relu'))
        model.add(tfl.Dense(1, activation='sigmoid'))
        
        return model

    cnn_model = CNN_Model(feat_shape)

    # load the trained weights
    cnn_model.load_weights('myModel/all.h5')
    Inde_test_prob = cnn_model.predict(X_test)
  

    afr_sites=[]
    for i, prob in enumerate(Inde_test_prob):
        if(prob[0]>0.5):
            # print resid
            # print(f"african_sites:{test_set['label'][i]}: Probability of being positive class = {prob[0]}")
            afr_sites.append(test_set['label'][i])

    # write the allosteric residues to a file
    with open(f'Case Study/{pdb_id}_allosteric_residues.txt', 'w') as f:
        afr_sites_str = ",".join(afr_sites)
        f.write("AlloFusion Allosteric Site Forming Residues:\n")
        f.write("Residues: ( Chain "+ chain_id +" and resid "+afr_sites_str+" )")

    # generate pml file
    def generate_pml_content(pdb_code, chain_name, prediction_data):
        pml_content = f"# PyMOL script to highlight allosteric sites in {pdb_code}\n"
        pml_content += f"fetch {pdb_code}\n"
        pml_content += "hide everything\n"
        pml_content += f"show cartoon, chain {chain_name}\n"
        pml_content += f"color spectrum, chain {chain_name}\n"
        
        # Process only the first prediction ("1")
        for res_num in prediction_data:
            pml_content += f"select resi {res_num} and chain {chain_name}\n"
            pml_content += f"show surface, resi {res_num} and chain {chain_name}\n"
            pml_content += f"color red, resi {res_num} and chain {chain_name}\n"
            pml_content += f"set transparency, 0.2, resi {res_num} and chain {chain_name}\n"
        
        pml_content += f"zoom chain {chain_name}\n"
        return pml_content

    pml_content = generate_pml_content(pdb_id, chain_id, afr_sites)
    # save pml file
    pml_file_path = f'Case Study/{pdb_id}_allosteric_sites.pml'
    with open(pml_file_path, 'w') as f:
        f.write(pml_content)

# Example usage:
# predict_allosteric_sites('5xjy', 'A')