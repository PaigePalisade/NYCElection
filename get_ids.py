import pickle

with open("ballots.pickle", 'rb') as file:
    ballots = pickle.load(file)

ids = set()

for b in ballots:
    for i in range(5):
        ids.add(b[i])

ids.remove('overvote')
ids.remove('undervote')
ids.remove('Write-in')


print(ids)