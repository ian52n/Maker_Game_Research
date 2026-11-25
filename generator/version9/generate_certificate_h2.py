import pandas as pd

# Generating all possible combinations of two basis. i and j represent different bases. k and m represent different rotations.
# p and q are translations. if p or q is negative then i shifted the first basis in the positive sense instead of shifting the 
# second basis

def generate_combinations():

    str_list = []

    card = 0

    for i in range(6):

        for j in range(6):

            for k in range(8):

                for m in range(8):

                    for p in range(-8, 8):

                        for q in range(-8, 8):

                            (x1, y1, x2, y2) = (0, 0, 0, 0)

                            if p < 0:

                                x1 = abs(p)

                            else:

                                x2 = p

                            if q < 0:

                                y1 = abs(q)

                            else:

                                y2 = q

                            my_str = str(card) + " " + str(i) + ":" + str(k) + str(x1) + str(y1) + " " + str(j) + ":" + str(m) + str(x2) + str(y2)

                            str_list.append(my_str)

                            card += 1

    return str_list

def save_cards(str_list):

    df = pd.DataFrame(data=str_list, columns=["construction"])

    df.to_csv("generator/version9/h2_combos.csv")

def generate():

    str_list = generate_combinations()

    save_cards(str_list)