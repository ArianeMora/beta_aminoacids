import sys
from enzymetk.dock_boltz_step import Boltz
from enzymetk.save_step import Save
import pandas as pd
import os
os.environ['MKL_THREADING_LAYER'] = 'GNU'

output_dir = 'boltz_26062025'
num_threads = 5
id_col = 'name'
seq_col = 'aa_sequence'
substrate_col = 'Substrate'
intermediate_col = 'Intermediate'
df = pd.read_csv('../output/LevSeq_unique_variants.csv')
df[substrate_col] = "O=C(OC)CCC1=CC=CC=C1"
df[intermediate_col] = str(r"CC1=C(/C2=C/C3=N/C(C(C)=C3CCC(O)=O)=C\C4=C(C(C=C)=C(/C=C5N=C(C(C=C)=C\5C)/C=C1\N26)N4[Fe]6=N)C)CCC(O)=O")
df = df.head(20)

df << (Boltz(id_col, seq_col, substrate_col, intermediate_col, f'{output_dir}', num_threads) >> Save(f'{output_dir}filenames.pkl'))

# base_dir = 'boltz_all'
# seq = 'MTPSDIPGYDYGRVEKSPITDLEFDLLKKTVMLGEEDVMYLKKAADVLKDQVDEILDLAGGWVASNEHLIYYFSPDTGEPIKEYLERVRARAGAWVLDTTCRDYNREWLDYQYEVGLRHHRSKKGVTDGVRTVPNTPLRYLIAGIYPITATIKPLLAEKGGSPEDIEGMYNAWLKSVVLQVAIWSHPYTKENDWLEHHHHHH'
# substrate_h2noh = str(r"[O-]C(CCC1=C(C)/C2=C/C(C(C=C)=C/3C)=NC3=C/C4=C(C=C)C(C)=C5/C=C(C(C)=C6CCC([O-])=O)\N=C6/C=C1\N2[Fe]N45)=O")
# substrate_nopiv = str(r"O=C(OC)CCC1=CC=CC=C1.[O-]C(CCC(C1=CC2=[N]3C(C(C)=C2CCC([O-])=O)=CC4=C(C(C=C)=C5N4[Fe]36N1C7=CC(C(C=C)=C8C)=[N]6C8=C5)C)=C7C)=O")
# # (label: str, seq: str, smiles: str, output_dir: str, cofactor_smiles: str
# intermediate = str(r"CC1=C(/C2=C/C3=N/C(C(C)=C3CCC(O)=O)=C\C4=C(C(C=C)=C(/C=C5N=C(C(C=C)=C\5C)/C=C1\N26)N4[Fe]6=N)C)CCC(O)=O")
# run_boltz_affinity(f'test_h2noh_new_boltz_intermediate', seq, "O=C(OC)CCC1=CC=CC=C1", base_dir, intermediate)
#O=C(OC)CCC1=CC=CC=C1.
#  WARNING: RDKit ETKDGv3 failed to generate a conformer for molecule C=CC1=C(C)C2=Cc3c(C=C)c(C)c4[n]3[Fe]35<-[N]2=C1C=c1c(C)c(CCC(=O)[O-])c([n]13)=CC1=[N]->5C(=C4)C(C)=C1CCC(=O)[O-].COC(=O)CCc1ccccc1,

# df = pd.read_csv(f'../all_variants.csv')
# for seq, lin, name in df[['AA', 'linage', 'name']].values:
#     seq = seq.replace('*', '')
#     if 'LEHHHHHH' not in seq:
#         # Add on the his tag incase we didn't include it in the DNA seq.
#         seq = seq + 'LEHHHHHH'
#     if lin == 'H2NOH':
#         print(f'{lin}_{name}')
#         run_boltz(f'{lin}_{name}', seq, substrate_h2noh, base_dir)
#     else:
#         print(f'{lin}_{name}')
#         run_boltz(f'{lin}_{name}', seq, substrate_nopiv, base_dir)
        
# # df = pd.read_csv(f'../lineage_summary.csv')
# for seq, lin, name in df[['AA', 'linage', 'name']].values:
#     if lin == 'H2NOH' and name in ['G4', 'G5', 'G6', 'G7']:
#         seq = seq.replace('*', '')
#         print(f'{lin}_{name}')
#         run_boltz(f'{lin}_{name}',seq, substrate, base_dir)