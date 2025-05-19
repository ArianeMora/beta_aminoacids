
import sys
from docko.boltz import *
from docko.chai import run_chai
import os
os.environ['MKL_THREADING_LAYER'] = 'GNU'
import pandas as pd


base_dir = 'boltz'
seq = 'MTPSDIPGYDYGRVEKSPITDLEFDLLKKTVMLGEEDVMYLKKAADVLKDQVDEILDLAGGWVASNEHLIYYFSNPDTGEPIKEYLERVRARAGAWVLDTTCRDYNREWLDYQYEVGLRHHRSKKGVTDGVRTVPNTPLRYLIAGIYPITATIKPLLAEKGGSPEDIEGMYNAWLKSVVLQVAIWSHPYTKENDWLEHHHHHH'
substrate = str(r"O=C(OC)CCC1=CC=CC=C1.[O-]C(CCC1=C(C)/C2=C/C(C(C=C)=C/3C)=NC3=C/C4=C(C=C)C(C)=C5/C=C(C(C)=C6CCC([O-])=O)\N=C6/C=C1\N2[Fe]N45)=O")
df = pd.read_csv(f'../lineage_summary.csv')
for seq, lin, name in df[['AA', 'linage', 'name']].values:
    seq = seq.replace('*', '')
    run_boltz(f'{lin}_{name}',seq, substrate, base_dir)

# run_chai('PARENT', # name
#                     seq, # sequence
#                     substrate, # ligand as smiles
#                     'chai/')