import json
import hashlib
import time
import copy


class block:
    def __init__(self,prevhash,stored):
        self.block={
            "prevhash":prevhash,
            "data": stored,
            "timestamp":time.time()
        }

    def hash(self):
        string_object = json.dumps(self.block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

class blockchain:
    def __init__(self,genisisdata=None,loadfile=None):
        self.chain=[]
        if not loadfile:
            # new chain
            self.chain.append(block("genisisblock",genisisdata))
        else:
            # load from file
            chainfromfile=json.load(open(loadfile,"r"))
            realchain=[]
            for cblock in chainfromfile:
                b=block(None,None) #placeholders that allow us to create the block object
                b.block=copy.deepcopy(cblock)
                realchain.append(b)
            self.chain=copy.deepcopy(realchain)

    def newblock(self,stored):
        self.chain.append(block(self.lastblock.hash(),stored))

    def lastblock(self):
        return self.chain[-1]

    def verify(self):
        rv=None
        rchain=list(reversed(self.chain))
        for idx in range(0,len(rchain)):
            if idx != 0 and rv != False and rchain[idx].block["prevhash"] == rchain[idx-1].hash():
                rv=True
            else:
                rv=False

        if rv != False or len(rchain)==1:
            return True
        else:
            return False

    def getblock(self,blockidx):
        return self.chain[blockidx].block

    def save(self,savefile):
        savedat=[]
        for cblock in self.chain:
            savedat.append(cblock.block)
        json.dump(savedat,open(savefile,"w"))
