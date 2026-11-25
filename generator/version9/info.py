import pandas as pd

df = pd.read_csv("generator/version9/unique_cards.csv")

a1 = df['A1'].to_list()
a2 = df['A2'].to_list()

targ_list = [len(set(a1[i].split()) & set(a2[i].split())) for i in range(len(a1))]

for i in range(2,7,1):

    print(targ_list.count(i))