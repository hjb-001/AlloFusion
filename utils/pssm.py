import math
import numpy as np
import pickle
import os
import pandas
import subprocess
import pandas as pd

def gene_PSSM(pssmdir,pdbid):
    df=pandas.read_csv(f'./{pssmdir}/{pdbid}.csv',header=None)
    pdb_name=df[0]
    seq=df[1]

    for i in (range(0,len(pdb_name))):
        f = open('Temporary.fasta', 'w')
        f.write(pdb_name[i] + '\n')
        f.write(seq[i])
        f.close()
        psiblast_cmd = [
            'psiblast',
            '-query', 'Temporary.fasta',
            '-db', '"D:/Program files/blast-2.15.0+/db/swissprot/swissprot"',
            '-evalue', '0.001',
            '-num_iterations', '3',
            '-out_ascii_pssm', f'E:/pssm/Case_Study/{pdb_name[i].split(">")[1]}.pssm'
        ]
        
      
        try:
            result = subprocess.run(psiblast_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"Error: psiblast command failed for {pdb_name[i]}")
            print(f"stdout: {e.stdout.decode()}")
            print(f"stderr: {e.stderr.decode()}")



def getPSSM(pssmdir,pdbid, window_size=3):
    gene_PSSM(pssmdir,pdbid)
    df = pd.read_csv(f'./{pssmdir}/{pdbid}.csv',header=None)
    pdb_names = df[0]
    seqs = df[1]
    pssms = []
    pdb_ids = []

    for i in range(len(pdb_names)):
        pdb_name = pdb_names[i].split(">")[1]
        seq = seqs[i]
        pssm_path = os.path.join('E:/pssm/Case_Study', f'{pdb_name}.pssm')
        
        if not os.path.exists(pssm_path):
            print(f"Error: {pssm_path} not found")
            pdb_ids.append(pdb_name)
            pssms.append(np.array([0] * 20))
            continue
        
        with open(pssm_path, 'r') as fin:
            fin_data = fin.readlines()
            pssm_begin_line = 3
            pssm_end_line = 0
            for j in range(1, len(fin_data)):
                if fin_data[j] == '\n':
                    pssm_end_line = j
                    break
            
            raw_pssm = np.zeros((pssm_end_line - pssm_begin_line, 20))
            for j in range(pssm_begin_line, pssm_end_line):
                raw_pssm[j - pssm_begin_line] = [float(x) for x in fin_data[j].split()[2:22]]
            
            # let raw_pssm in range [0, 1]
            raw_pssm = 1 / (1 + np.exp(-raw_pssm))
            
            # calculate window pssm
            window_pssm = []
            half_window = window_size // 2
            for j in range(len(seq)):
                start = max(0, j - half_window)
                end = min(len(seq), j + half_window + 1)
                window = raw_pssm[start:end]
                window_mean = np.mean(window, axis=0)
                window_pssm.append(window_mean)
            
            window_pssm = np.array(window_pssm)
            
            if len(window_pssm) == len(seq):
                pdb_ids.append(pdb_name)
                pssms.append(window_pssm)
            else:
                print(f"Error: {pdb_name} pssm length not match")

    # save pssm features
    with open(f'./{pssmdir}/{pdbid}_pssm_features.pkl', 'wb') as f:
        pickle.dump({"pdb_name": pdb_ids, "pssms": pssms}, f)
