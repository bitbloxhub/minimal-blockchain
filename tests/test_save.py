import os
import minimal_blockchain as bc

chain=bc.blockchain(genisisdata="hello blockchain world")
chain.save("/tmp/blockchain.json")
del chain
chain=bc.blockchain(loadfile="/tmp/blockchain.json")
print(chain.getblock(0))
