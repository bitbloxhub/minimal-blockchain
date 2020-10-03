import minimal_blockchain as bc

#hi branch

ch=bc.blockchain("genisis data")
print(ch.verify())
ch.chain.append(bc.block("tampered hash","data"))
print(ch.verify())
