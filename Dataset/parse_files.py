
import numpy as np

def parse_hmm(fname):
    f = open(fname)
    line=f.readline()
    while line[0]!='#':
        line=f.readline()   
    f.readline()
    f.readline()
    f.readline()
    f.readline()    
    seq = []
    extras = np.zeros([0,10])
    prob = np.zeros([0,20])
    line = f.readline()
    while line[0:2]!='//':
        lineinfo = line.split()
        seq.append(lineinfo[0])  
        probs_ = [2**(-float(lineinfo[i])/1000) if lineinfo[i]!='*' else 0. for i in range(2,22)]
        prob = np.concatenate((prob,np.matrix(probs_)),axis=0)
        
        line = f.readline()
        lineinfo = line.split()
        extras_ = [2**(-float(lineinfo[i])/1000) if lineinfo[i]!='*' else 0. for i in range(0,10)]
        extras = np.concatenate((extras,np.matrix(extras_)),axis=0)
        
        line = f.readline()
        assert len(line.strip())==0
        
        line = f.readline()
    return (''.join(seq),prob,extras)



def parse_pssm(fname):
    f = open(fname)
    # the 4th line should be the start of the PSSM data
    f.readline()
    f.readline()
    f.readline()
    seq = []
    lprob = np.zeros([0,20])
    prob = np.zeros([0,20])
    extra = np.zeros([0,2])
    line = f.readline()
    while len(line.strip())>0:
        lineinfo = line.split()
        seq.append(lineinfo[1])
        lprobs_ = [float(lineinfo[i]) for i in range(2,22)]
        lprob = np.concatenate((lprob,np.matrix(lprobs_)),axis=0)
        probs_ = [float(lineinfo[i])/100 for i in range(22,42)]
        prob = np.concatenate((prob,np.matrix(probs_)),axis=0)
        extras_ = [float(lineinfo[i]) for i in range(42,44)]
        extra = np.concatenate((extra,np.matrix(extras_)),axis=0)
        line = f.readline()

    return (''.join(seq),prob,lprob,extra)
