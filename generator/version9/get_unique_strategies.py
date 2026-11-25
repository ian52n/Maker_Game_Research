import pandas as pd

# this was the creative pruning method i mentioned in email. i was thinking that if you had two cards
#  and they have the same T shape then possibly the overlapping of their intersections of A_i
#  might give a possible pivots and i could collpase all the same T cards to just one. For example,
#  if there were say 10 cards with the same T but they all shared a common cell in thier intersection of A_i
#  then that overlapping cell would be the pivot and i would keep the first one and get rid of the others.
#  probably not technically sound but is just an experiment for right now

def get_unique_strategies():

    df = pd.read_csv("generator/version9/copies.csv")
    df2 = pd.read_csv("generator/version9/unique_cards.csv")
    n = len(df2)
    original_list = []
    copy_set = set()

    for i in range(n):

        copies = df[df['parent_copy'] == i].reset_index(drop=True)
        

        if len(copies) > 0:

            flag = True

            original_pivots = set(copies.iloc[0]['pivots'].split())

            for j in range(len(copies)):

                if not original_pivots == set(copies.iloc[j]['pivots'].split()):

                    flag=False

            if flag:

                for c in copies['card'].to_list():

                    copy_set.add(c)

                if i not in copy_set:

                    original_list.append([df2.iloc[i]['card'] , copies.iloc[0]['pivots']])

    new_df = pd.DataFrame(data=original_list, columns=["card", "pivots"])

    new_df.to_csv("generator/version9/unique_strategies.csv")

    
