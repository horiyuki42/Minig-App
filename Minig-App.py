from hashlib import sha256
MAX_NONCE = 100000000000
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def main(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"\nYay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"\nCould not find correct has after trying {MAX_NONCE} times")

if __name__=='__main__':
    transactions='''
    A->B->20,
    B->A->20
    '''
    difficulty = 5
    import time
    start = time.time()
    print("Start mining")
    new_hash = main(5, transactions, 'horiyuki42', difficulty)
    total_time = str((time.time() - start))
    print(f"End minig. Minig took: {total_time} seconds\n")
    print(new_hash)
    input(f"\nPress Enter to exit.")