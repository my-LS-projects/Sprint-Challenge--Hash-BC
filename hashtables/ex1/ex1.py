#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # weights = list of weights
    # length = how many weights
    # limit = weight limit
    # return tuple answer with two weights (highest weight, second weight)

    for i in range(length):
        # hashtable, key, value
        hash_table_insert(ht, weights[i], i)

    for j in range(length):
        # ht, key
        diff = hash_table_retrieve(ht, limit - weights[j])

        if value is not None:
            return (diff, j)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
