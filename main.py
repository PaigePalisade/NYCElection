from openpyxl import load_workbook
from os import listdir
import pickle

name_sheet = load_workbook(filename="2021P_CandidacyID_To_Name.xlsx").active

id2name = {}
index2id = [
    "217572",
    "219978",
    "219469",
    "218127",
    "218491",
    "217796",
    "217605",
    "221141",
    "221183",
    "218117",
    "218922",
    "217654",
    "221458"
]

n = len(index2id)

pairwiseMatrix = [[0 for c in range(n)] for r in range(n)]

id2index = {k: v for (k,v) in zip(index2id, range(len(index2id)))}

for row in name_sheet.iter_rows(min_row=2, max_col=2):
    id2name[str(row[0].value)] = row[1].value

with open("ballots.pickle", 'rb') as file:
    ballots = pickle.load(file)

for ballot in ballots:
    for i in range(5):
        # ballot is discarded after the first instance of an overvote
        if ballot[i] == 'overvote':
            break
        # undervotes are skipped and we are not counting write-in's for the purpose of this tabulation. if candidate is ranked twice, the second instance is skipped
        if ballot[i] != 'undervote' and ballot[i] != 'Write-in' and not ballot[i] in ballot[0:i]:
            # for every other candidate
            for j in range(n):
                # if they haven't been ranked already
                if index2id[j] not in ballot[0:i+1]:
                    # add their vote to the pairwise matrix
                    pairwiseMatrix[id2index[ballot[i]]][j] += ballots[ballot]


print(" " * 21, end="")

for i in range(n):
    print(f"{id2name[index2id[i]]:>21}", end="")

print()

for r in range(n):
    print(f"{id2name[index2id[r]]:20}", end="")
    for e in pairwiseMatrix[r]:
        print(f"{e:21}",end="")
    print()

diffMatrix = [[0 for c in range(n)] for r in range(n)]

for r in range(n):
    for c in range(n):
        diffMatrix[r][c] = pairwiseMatrix[r][c] - pairwiseMatrix[c][r]

print()
print(" " * 21, end="")

for i in range(n):
    print(f"{id2name[index2id[i]]:>21}", end="")

print()

for r in range(n):
    print(f"{id2name[index2id[r]]:20}", end="")
    for e in diffMatrix[r]:
        print(f"{e:21}",end="")
    print()