#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    # origin has source of None
    # final destination has value of None
    # connect where starting = destination of previous

    # insert all tickets
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    for j in range(length):
        print(f"j: {j}")
        print(f"route - 1: {route[j - 1]}")
        if route[j - 1] is not None:
            # get matching destination to origin
            route[j] = hash_table_retrieve(hashtable, route[j - 1])
        else:
            route[j] = hash_table_retrieve(hashtable, "NONE")
        print("route", route)
    return route[:-1]
