from openpyxl import load_workbook
from os import listdir
import pickle

name_sheet = load_workbook(filename="2021P_CandidacyID_To_Name.xlsx").active

id2name = {}
index2id = [
    217572,
    219469,
    219978,
    218127,
    218491,
    217796,
    217605,
    221141,
    221183,
    218117,
    218922,
    217654,
    221458
]

n = len(index2id)

voteMatrix = [[0 for c in range(n)] for r in range(n)]

id2index = {k: v for (k,v) in zip(index2id, range(len(index2id)))}

for row in name_sheet.iter_rows(min_row=2, max_col=2):
    id2name[str(row[0].value)] = row[1].value

with open("ballots.pickle", 'wb') as f:
    ballots = pickle.load(f)



with open("ballots.pickle", 'rb') as file:
    ballots = pickle.load(file)

