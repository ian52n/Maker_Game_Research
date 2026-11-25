from generate_certificate_h2 import generate
from generate_card_cells import get_data
from prune import prune
from find_card_transformations import generate_card_transforms
from remove_duplicates import remove_duplicates
from find_unique_certificate import get_unique_certificate
from find_copies import find_copies
from get_unique_strategies import get_unique_strategies
import time

# runs all the main methods in each script. runs quickly except for 
# unique strategies. it will give the length of the df and the numbers printed
#  tells where in the df its at by index. i used sleep to make sure the csv was generated
#  before it was used in another method

def run():

    generate()
    print("certificate generated")
    time.sleep(5)

    get_data()
    print("certificate cells found")
    time.sleep(5)

    prune()
    print("cards have been pruned")
    time.sleep(5)

    generate_card_transforms()
    print("card transforms found")
    time.sleep(5)

    remove_duplicates()
    print("unique strategies found")
    time.sleep(5)

    find_copies()
    print("finding unique strategies with intersecting A")
    time.sleep(5)

    get_unique_strategies()
    print("reduced unique strategies with intersecting A to 1")
    time.sleep(5)

    get_unique_certificate()
    print("generated unique certificate")

if __name__ == "__main__":

    run()



    