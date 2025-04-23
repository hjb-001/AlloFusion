# -*- coding: utf-8 -*-
"""

@author: hjb
"""
import warnings
warnings.filterwarnings('ignore')

import argparse
from utils.sequence_indices import sequence_indices
from utils.extract_sequence import extract_sequence
import os
import pandas as pd
import numpy as np
import pickle
from utils.download_pdb import download_pdb
from prediced import predict_allosteric_sites
from utils.embedding import get_embedding
from utils.pssm import getPSSM
from utils.bio import getBio
parser = argparse.ArgumentParser(description='Extract sequence from PDB file')
# Main parameters
parser.add_argument("--PDBID", type=str, help="Four-character pdbid (no .pdb required)", required=True)
parser.add_argument("--CHAIN", type=str, default=False, help="Protein chain",required=True)

def extract_seq(pdb_id,chain_id):
    pdb_dir=f'./Case Study/{pdb_id}.pdb'
    if not os.path.exists(pdb_dir):
        # download PDB files from the PDB database.
        download_pdb(pdb_id, './Case Study')
    seq=extract_sequence(pdb_dir,chain_id)
    seq_indices = sequence_indices(pdb_id, chain_id)
    return seq,seq_indices


if __name__ == "__main__":
    args = parser.parse_args()
    pdb_id = args.PDBID
    chain_id = args.CHAIN

    # extract sequence from PDB file
    seq,seq_indices=extract_seq(pdb_id, chain_id)
    seq_indices= '" ' + ', '.join([f'{key}' for key in seq_indices.keys()]) + ' " '
    id='>'+pdb_id+'_'+chain_id
    csv_file=f'Case Study/{pdb_id}.csv'
    with open(csv_file, 'w') as f:
        f.write(f'{id},{seq.strip()},{seq_indices}\n')

    # 1-1 （Embedding）
    get_embedding(pdb_id)
    print('Embedding done!')
    # 1-2 （pssm）
    getPSSM('Case Study',pdb_id)
    print("PSSM done!")
    # #1-3 （bio）
    getBio('Case Study',pdb_id,chain_id)
    print("Bio done!")
    # load embeddings
    with open(f'./Case Study/{pdb_id}_T5.pkl', 'rb') as f:
        embeddings = pickle.load(f)
  
    # read csv file
    df = pd.read_csv(f'./Case Study/{pdb_id}.csv', header=None)

    seqs=df[1].tolist()
    pdb_ids=df[0].tolist()
    labels=df[2].tolist()[0].split(',')
    pdb_names=[]
    residues=[]
    res_features=[]
    res_lables=[]
    # load Z-scores
    with open(f'./Case Study/{pdb_id}_bio_features.pkl', 'rb') as f:
        bio=pickle.load(f)

    # load pssm_features
    with open(f'./Case Study/{pdb_id}_pssm_features.pkl', 'rb') as f:
        pssm_features = pickle.load(f)
    pdb_names1 = pssm_features['pdb_name']
    pssm_features = pssm_features['pssms']

    i=0
    pdb_ids[i]=pdb_ids[i].split('>')[1].strip()
    seqs[i]=seqs[i].strip()

    for j in range(len(seqs[i])):
        pdb_names.append(pdb_ids[i])
        residues.append(seqs[i][j])
        res_features.append(np.concatenate((embeddings[i][j],pssm_features[i][j], bio[i][j])))
        res_lables.append(labels[j])

    with open(f'./Case Study/{pdb_id}_{chain_id}_dataset.pkl', 'wb') as f:
        pickle.dump({"pdb_name":pdb_names,"residue":residues,"features":res_features,"label":res_lables},f)

    #2 predict allosteric sites
    predict_allosteric_sites(pdb_id, chain_id)


    