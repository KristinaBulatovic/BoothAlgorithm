D = [0,0,1,1] #3
C = [0,1,1,1] #7
A = [0,0,0,0]
d = 0

def siftovanje():
    global D, C, A, d
    ADd = A + D
    ADd.append(d)
    ADd2 = [0,0,0,0,0,0,0,0,0]
    for i in range(9):
        try:
            ADd2[i+1] = ADd[i]
        except:
            ADd2[0] = ADd[0]
            A = ADd2[0:4]
            D = ADd2[4:8]
            d = ADd2[8]
            return

def sabiranje_oduzimanje(sab):
    global A, C
    if(sab == 0):
        C2 = C
    if(sab == 1):
        C2 = oduzimanje()
    A2 = [0, 0, 0, 0]
    a = 0
    for i in range(3, -1, -1):
        if(A[i] == C2[i] == 0):
            A2[i] = 0
            if(a == 1):
                A2[i] = 1
                a = 0
        elif(A[i] == C2[i] == 1):
            if(a == 1):
                A2[i] = 1
            else:
                A2[i] = 0
                a = 1
        elif(A[i] > C2[i]):
            A2[i] = 1
            if(a == 1):
                A2[i] = 0
        elif(A[i] < C2[i]):
            A2[i] = 1
            if(a == 1):
                A2[i] = 0
    A = A2

def oduzimanje():
    C2 = C
    C3 = [0, 0, 0, 0]
    C4 = [0, 0, 0, 0]
    for i in range(4):
        if(C2[i] == 0):
            C3[i] = 1
        elif(C2[i] == 1):
            C3[i] = 0

    a = 1
    for i in range(3, -1, -1):
        if(C3[i] == 0):
            C4[i] = 0
            if(a == 1):
                C4[i] = 1
                a = 0
        elif(C3[i] == 1):
            C4[i] = 1

    return C4

i = 0
while(i < 4):
    if(D[-1] == d):
        print("preskace: ", A, D, d, C)
        siftovanje()
    elif(D[-1] > d):
        print("oduzimanje: ", A, D, d, C)
        sabiranje_oduzimanje(1)
        i += 1
        print("sifrovanje: ", A, D, d, C)
        siftovanje()
        i += 1
    elif(D[-1] < d):
        print("sabiranje: ", A, D, d, C)
        sabiranje_oduzimanje(0)
        print("sifrovanje: ", A, D, d, C)
        siftovanje()
        i += 1