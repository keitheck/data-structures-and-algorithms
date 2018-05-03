from hash_table import HashTable


def left_join(hash1, hash2):
    """
    This functions takes two hashmaps with word strings as
    keys and performs a left join into a list.
    """

    joined = HashTable()

    keys1 = hash1.__iter__()
    # keys2 = hash2.__iter__()

    for key in keys1:
        joinkey = key
        val1 = hash1.get(key)
        val2 = hash2.get(key)

        joined.set(joinkey, [val1, val2])

    return joined
