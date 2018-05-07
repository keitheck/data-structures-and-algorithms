from hash_table import HashTable


def left_join(hash1, hash2):
    """
    This functions takes two hashmaps with word strings as
    keys and performs a left join into a list.
    """
    if type(hash1) is not HashTable or type(hash2) is not HashTable:
        raise TypeError('Arguments must be HashTables')
        
    joined = HashTable()

    keys1 = hash1.return_k_v()
    keys2 = hash2.return_k_v()

    for key in keys1:
        # import pdb ; pdb.set_trace()
        val1 = hash1.get(key)
        if hash2.get(key):
            val2 = hash2.get(key)
        else: 
            val2 = None  

        joined.set(key, [val1, val2])

    return joined
