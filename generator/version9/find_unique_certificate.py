import pandas as pd

#  i am using the card numbers in unique_strategies.csv to find its transform string and then i combined this with the
#  cells the card occupies for A, T, intersection of A_i

def get_unique_certificate():

    df = pd.read_csv("generator/version9/unique_strategies.csv")
    cards = df['card'].to_list()
    pivots = df['pivots'].to_list()

    ind_list = [int(c) for c in cards]

    cert_df = pd.read_csv("generator/version9/h2_combos.csv")

    cert_df = cert_df[cert_df.index.isin(ind_list)].reset_index(drop=True)
    temp_df = pd.DataFrame(data=pivots, columns=["pivots"])

    cert_df = pd.concat([cert_df, temp_df], axis=1)

    df = pd.read_csv("generator/version9/unique_cards.csv")

    df = df[df["card"].isin(ind_list)].reset_index(drop=True)

    df = df[["A", "T", "inter_A"]]

    cert_df = pd.concat([cert_df, df], axis=1)

    cert_df.to_csv("generator/version9/unique_h2_certificate.csv")