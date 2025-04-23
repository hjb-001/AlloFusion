import requests
import os
# pdb urls
rcsb_download = "https://files.rcsb.org/download/"
rcsb_structure = "https://www.rcsb.org/structure/"

# download pdb file
def download_pdb(pdb_id, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    pdb_file = os.path.join(save_dir, pdb_id + ".pdb")
    if not os.path.exists(pdb_file):
        url = rcsb_download + pdb_id + ".pdb"
        r = requests.get(url)
        with open(pdb_file, "wb") as f:
            f.write(r.content)