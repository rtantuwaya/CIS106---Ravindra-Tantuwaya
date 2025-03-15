fibSeqA = 1
fibSeqB = 1
print(fibSeqA)
print(fibSeqB)
for fibSeq in range(1, 20 + 1, 1):
    fibSeqC = fibSeqA + fibSeqB
    print(fibSeqC)
    fibSeqA = fibSeqB
    fibSeqB = fibSeqC
