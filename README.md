# **AlloFusion: Allosteric Site Prediction Based on Language Models and Multi-Feature Fusion**

The AlloFusion program is a method for protein allosteric site prediction. 



## Requirement
- python 3.11

- numpy  1.26.4

- pandas  2.2.3

- joblib  1.4.0

- ProDy  2.4.1

- torch  2.5.0+cu118

- tensorflow  2.12.0

- transformers  4.42.4

  
---


## To run the AlloFusion, you need to install the bioinformatics tools and download the corresponding databases.
（1）Download the prot_t5_xl_uniref50 model from the following link:
	 	https://huggingface.co/Rostlab/prot_t5_xl_uniref50/tree/main  

（2）Install blast+ for extracting PSSM(position-specific scoring matrix) profiles

​			To install blast-2.15.0+ and download NR database (ftp://ftp.ncbi.nlm.nih.gov/blast/db/) for psiblast, please refer to BLAST(https://www.ncbi.nlm.nih.gov/books/NBK52640/).



---
## 🔍 Model Download Instructions

Due to the large size of the trained model file (exceeding GitHub's file size limit), it has been uploaded to the [Releases](https://github.com/hjb-001/AlloFusion/releases) section of this repository.

Please visit the Releases page to download the full model file:

👉 [Click here to download the model from the Releases page](https://github.com/hjb-001/AlloFusion/releases)

After downloading, place the model file in the project root directory or the designated model folder to use it or reproduce the experimental results.

---
## 📁 Dataset Download Instructions

Due to the large size of the dataset (exceeding GitHub's file size limit), it has also been uploaded to the [Releases](https://github.com/hjb-001/AlloFusion/releases) section of this repository.

Please visit the Releases page to download the full dataset:

👉 [Click here to download the dataset from the Releases page](https://github.com/hjb-001/AlloFusion/releases)

After downloading, extract the dataset to the project root directory or the designated data folder to proceed with training or evaluation.


----
## How to run

**Step 1:** Extract protein sequence based on input pdbid and chain

**Step 2:** Residue feature extraction

**Step 3:** Combined residue characterization

**Step 4:** Loading the model for predicting AFRs



---

## Example

An allosteric protein with PDB ID "4ZSI" is used as an example to show the process. This PDB file is 4ZSI.pdb. Only the protein functional chain is preserved.

```python
python AlloFusionMain.py --PDBID [pdbid] --CHAIN [chain]
```

> for example:
```python
python AlloFusionMain.py --PDBID 4ZSI --CHAIN B
```

> The parameter [pdbid] is the PDB file name of the allosteric protein.

> The parameter [chain] is the functional chain of the target protein.

Then, AlloFusion program will perform the feature extraction and prediction process, which will take some time.

The final prediction result is a file containing the residue IDs of AFRs residues:

`4ZSI_allosteric_residues.txt`

```
AlloFusion Allosteric Site Forming Residues:
Residues: ( Chain B and resid 92, 95, 96, 97, 98, 99, 109, 111, 140, 142, 144, 152, 154, 156, 174, 175, 177, 193, 219, 221, 223, 232, 233, 234, 236, 238, 247)
```

and the script for viewing the allosteric sites composed of AFRs in PyMol: `4ZSI_allosteric_sites.pml`.
