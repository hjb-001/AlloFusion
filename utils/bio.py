import os
import numpy as np
import pandas as pd
import pickle
import math
from prody import *
from matplotlib.pyplot import *
from utils.sequence_indices import sequence_indices
ion()

def BuildFeatureDictionary(feature_np_1D):
    Feature_table = feature_np_1D
    max_Feature = np.amax(Feature_table)
    min_Feature = np.amin(Feature_table)
    normolized_Feature_table = (Feature_table - min_Feature) / (max_Feature - min_Feature) ##归一化[0,1]

    Feature_dict = {}
    Feature_dict['A'] = normolized_Feature_table[0]
    Feature_dict['M'] = normolized_Feature_table[1]
    Feature_dict['C'] = normolized_Feature_table[2]
    Feature_dict['N'] = normolized_Feature_table[3]
    Feature_dict['D'] = normolized_Feature_table[4]
    Feature_dict['E'] = normolized_Feature_table[5]
    Feature_dict['Q'] = normolized_Feature_table[6]
    Feature_dict['F'] = normolized_Feature_table[7]
    Feature_dict['R'] = normolized_Feature_table[8]
    Feature_dict['G'] = normolized_Feature_table[9]
    Feature_dict['H'] = normolized_Feature_table[10]
    Feature_dict['T'] = normolized_Feature_table[11]
    Feature_dict['I'] = normolized_Feature_table[12]
    Feature_dict['V'] = normolized_Feature_table[13]
    Feature_dict['K'] = normolized_Feature_table[14]
    Feature_dict['L'] = normolized_Feature_table[15]
    Feature_dict['P'] = normolized_Feature_table[16]
    Feature_dict['S'] = normolized_Feature_table[17]
    Feature_dict['W'] = normolized_Feature_table[18]
    Feature_dict['Y'] = normolized_Feature_table[19]
    Feature_dict['X'] = normolized_Feature_table[20]

    return Feature_dict

# calculate zscore
def ESSA_zscore(dir,pdb_file, chain):
    # load pdb file
    file_path = f"./{dir}/{pdb_file}.pdb"
    ag = parsePDB(file_path, compressed=False)
    essa = ESSA()
    essa.setSystem(ag, chain=chain, lowmem=True)
    essa.scanResidues()

    essa.writeESSAZscoresToPDB()
    return extract_zscore(f'{pdb_file}_gnm_zs.pdb')

# extract zscore
def extract_zscore(pdb_file):
    # load pdb file
    with open(pdb_file, 'r') as f:
        lines = f.readlines()
    residue_b_factors = {}
    # extract zscore
    for line in lines:
        if line.startswith('ATOM'):
            res_id= (line[22:26].strip())
            z = float(line[60:66].strip())
            residue_b_factors[res_id] = z
    return residue_b_factors

def getzScore(dir,pdb_id,chain_id):
    df = pd.read_csv(f'./{dir}/{pdb_id}.csv',header=None)
    seqs=df[1].tolist()
    pdb_ids=df[0].tolist()

    pdb_names=[]
    z_scores = []
    for i in (range(0,len(pdb_ids))):
        res_s=[]
        pdb_file = pdb_ids[i].split('_')[0].split('>')[1]
        pdb_names.append(pdb_ids[i].split('>')[1].strip())
        chain = pdb_ids[i].split('_')[1]
        res_index= sequence_indices(pdb_file, chain)
        res_scores=ESSA_zscore(dir,pdb_file, chain)
        seq=seqs[i]
       
        for key in res_index.keys():
            if key in res_scores:
                res_s.append(res_scores[key])
            else:
                res_s.append(0)
  
        if len(res_s) != len(seq):
            res_s = [0 for i in range(len(seq))]
            for key in res_scores.keys():
                res_s[int(key)]=res_scores[key]
        res_s = np.array(res_s)
        # let zscore in [0,1]
        res_s = (res_s - np.min(res_s)) / (np.max(res_s) - np.min(res_s))
        # round to 4 decimal places
        res_s = [round(i, 4) for i in res_s]
        z_scores.append(res_s)

    # save zscore
    with open(f'./{dir}/{pdb_id}_zScore.pkl', 'wb') as f:
        pickle.dump(z_scores,f)

def getBio(dir,pdb_id,chain_id):
    # The hydrophobicity of each amino acid
    feature4_np_1D = np.array(
        [1.8,1.9,2.5,-3.5,-3.5,-3.5,-3.5,2.8,-4.5,-0.4,-3.2,-0.7,4.5,4.2,-3.9,3.8,-1.6,-0.8,-0.9,-1.3,0.0])
    # The solvent-accessible surface area (SASA) of each amino acid residue
    feature5_np_1D = np.array(
        [129,224,167,195,193,223,225,240,274,104,224,172,197,174,236,201,159,155,285,263,0])
    features = [feature4_np_1D,feature5_np_1D]
    seq_fn = f'./{dir}/{pdb_id}.csv'
    df=pd.read_csv(seq_fn,header=None)
    seqs=df[1].tolist()
    getzScore(dir,pdb_id,chain_id)
    Zscore = pickle.load(open(f'./{dir}/{pdb_id}_zScore.pkl', 'rb'))
    # build feature dictionary
    Feature_dict4 = BuildFeatureDictionary(feature4_np_1D)
    Feature_dict5 = BuildFeatureDictionary(feature5_np_1D)
    features=[]
    for k,seq in enumerate(seqs):
        seq = seq.upper()
        seq_len = len(seq)
        feature4 = np.zeros((seq_len, 1))
        feature5 = np.zeros((seq_len, 1))
        feature6 = np.zeros((seq_len, 1))
        for i in range(seq_len):
            key_res=seq[i]
            if seq[i] not in Feature_dict4.keys():
                key_res = "X"
            feature4[i] = Feature_dict4[key_res]
            feature5[i] = Feature_dict5[key_res]
            feature6[i] = Zscore[k][i]
        feature = np.concatenate((feature4,feature5), axis=1)
        feature = np.concatenate((feature,feature6),axis=1)
        features.append(feature)
    # save bio features
    with open(f'./{dir}/{pdb_id}_bio_features.pkl', 'wb') as f:
        pickle.dump(features, f)



