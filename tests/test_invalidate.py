import minimal_blockchain as bc

ch=bc.blockchain("genisis data")
print(ch.verify())
ch.chain.append(bc.block("tampered hash","data"))
print(ch.verify())
