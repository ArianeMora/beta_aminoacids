import sys
from enzymetk.dock_boltz_step import Boltz
from enzymetk.save_step import Save
import pandas as pd
import os
os.environ['MKL_THREADING_LAYER'] = 'GNU'
import time
start = time.time()

output_dir = 'boltz_26062025/'
num_threads = 5
id_col = 'name'
seq_col = 'aa_sequence'
substrate_col = 'Substrate'
intermediate_col = 'Intermediate'
df = pd.read_csv('../output/LevSeq_unique_variants_todo.csv')
df[substrate_col] = "O=C(OC)CCC1=CC=CC=C1"
df[intermediate_col] = str(r"CC1=C(/C2=C/C3=N/C(C(C)=C3CCC(O)=O)=C\C4=C(C(C=C)=C(/C=C5N=C(C(C=C)=C\5C)/C=C1\N26)N4[Fe]6=N)C)CCC(O)=O")

df << (Boltz(id_col, seq_col, substrate_col, intermediate_col, f'{output_dir}', num_threads) >> Save(f'{output_dir}filenames.pkl'))
end = time.time()
print(end - start)