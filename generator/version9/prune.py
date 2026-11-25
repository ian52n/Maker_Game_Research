import pandas as pd

#  pruning all the cards so that only the cards with intersecting A_is with an
#  order between 2 and 4 survive. Also only cards with two child cells survive

def prune():

    df = pd.read_csv("generator/version9/generated_A_T_cells.csv")

    a1 = df['A1'].to_list()
    a2 = df['A2'].to_list()
    t1 = df['T1'].to_list()
    t2 = df['T2'].to_list()

    a1_set = [set(s.split()) for s in a1]
    a2_set = [set(s.split()) for s in a2]
    t1_set = [set(s.split()) for s in t1]
    t2_set = [set(s.split()) for s in t2]

    order_int_Ai = [len(set(a1_set[i] & a2_set[i])) for i in range(len(df))]
    order_free_T = [len((t1_set[i] | t2_set[i]) - (a1_set[i] | a2_set[i])) for i in range(len(df))]

    remove_inds1 = [i for i,x in enumerate(order_int_Ai) if (x < 2) or (x > 4)]
    remove_inds2 = [i for i,x in enumerate(order_free_T) if not x == 2]

    remove_inds = set(remove_inds1 + remove_inds2)


    df = df.drop(remove_inds).reset_index(drop=True)

    df.to_csv("generator/version9/pruned_cards_by_interA.csv")