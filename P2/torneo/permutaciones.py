
permutaciones = []

i=0
for a0 in range(0,10):
    for a1 in range(0, 10):
        for a2 in range(0, 10):
            for a3 in range(0, 10):
                for a4 in range(0, 10):
                    for a5 in range(0, 10):
                        for a6 in range(0, 10):
                            for a7 in range(0, 10):
                                for a8 in range(0, 10):
                                    unique=set()
                                    unique.add(a0)
                                    unique.add(a1)
                                    unique.add(a2)
                                    unique.add(a3)
                                    unique.add(a4)
                                    unique.add(a5)
                                    unique.add(a6)
                                    unique.add(a7)
                                    unique.add(a8)
                                    if (len(unique)!=10):
                                        continue
                                    # permutaciones.append([a0,a1,a2,a3,a4,a5,a6,a7,a8])
                                    i+=1
                                    if i==1000000:
                                        print([a0,a1,a2,a3,a4,a5,a6,a7,a8])
                                        exit()



