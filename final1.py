import os
from collections import Counter
import re
import collections
from functools import reduce

def loadfile(plos, folder1, folder2):
    my_set = {}
    flag = 0

    for name in os.listdir(folder1):
        if flag == 150:
            break
        name1 = folder2 + name
        input2 = open(name1, 'r', encoding="latin1")
        jdmread = input2.read()
        input2.close()
        key = jdmread.split()
    #my_set.update({new : 0})
    #print(key)
        flag += 1
        #print(key)
        comarr = comparewords(key, plos, folder1)
        #print(comarr)
        #print(flag)

def comparewords(key, plos, folder1):
    #print("In Compare words")
    res = []
    for val in plos:
        if val in key:
            #print("1")
            res.append(1)
        else:
        #print("0")
            res.append(0)
    if folder1 == './plos':
        res.append("P")
    if folder1 == './jdm':
        res.append("J")
    if folder1 == './arxiv':
        res.append("A")
    #print(len(res))
    return(res)


def load_stop():
    #print("In load stop")
    words = []
    input = open('stoplist.txt', 'r')
    filecon = input.read()
    input.close()
    stp = filecon.split()
    #print(stp)
    return(stp)

def list_files(stop):
    #print("In list files for plos")
    flag = 0
    arxivwords = []
    res = {}
    res1 = {}
    for name in os.listdir('./plos'):

        if flag == 150:
            break
        name1 = "plos/" + name
        input2 = open(name1, 'r', encoding="latin1")
        arxivread = input2.read()
        input2.close()
        new = arxivread.split()
        flag += 1
        res1 = reduce(lambda d, c: d.update([(c, d.get(c, 0) + 1)]) or d, arxivread.split(), {})
        res.update(res1)
    #print(res)
    #print(len(res))

    for k in res.copy().keys():
        if k in stop:
            del res[k]

    #print(res)
    #print(len(res))

    for word, freq in res.items():
        freq1 = (float(freq) / 15865)
        res[word] = freq1
    #print(res)

    return(res)

def list_files1(stop):
    #print("In list files for jdm")
    flag = 0
    arxivwords = []
    res = {}
    res1 = {}
    for name in os.listdir('./jdm'):

        if flag == 150:
            break
        name1 = "jdm/" + name
        input2 = open(name1, 'r', encoding="latin1")
        arxivread = input2.read()
        input2.close()
        new = arxivread.split()
        flag += 1
        res1 = reduce(lambda d, c: d.update([(c, d.get(c, 0) + 1)]) or d, arxivread.split(), {})
        res.update(res1)
    #print(res)
    #print(len(res))

    for k in res.copy().keys():
        if k in stop:
            del res[k]

    #print(res)
    #print(len(res))

    for word, freq in res.items():
        freq1 = (float(freq) / 8483)
        res[word] = freq1
    #print(res)

    return(res)

def list_files2(stop):
    #print("In list files for arxiv")
    flag = 0
    arxivwords = []
    res = {}
    res1 = {}
    for name in os.listdir('./arxiv'):

        if flag == 150:
            break
        name1 = "arxiv/" + name
        input2 = open(name1, 'r', encoding="latin1")
        arxivread = input2.read()
        input2.close()
        new = arxivread.split()
        flag += 1
        res1 = reduce(lambda d, c: d.update([(c, d.get(c, 0) + 1)]) or d, arxivread.split(), {})
        res.update(res1)
    #print(res)
    #print(len(res))

    for k in res.copy().keys():
        if k in stop:
            del res[k]

    #print(res)
    #print(len(res))

    for word, freq in res.items():
        freq1 = (float(freq) / 11274)
        res[word] = freq1
    #print(res)

    return(res)

def classification(plos, jdm, arxiv, folder1, folder2):
    print("In classification:")
    readfile = []
    new1 = []
    jdm1 = []
    plos1 = []
    arxiv1 = []
    new =[]
    totalcounter = 0
    ploscounter = 0
    jdmcounter = 0
    arxivcounter = 0
    total = 0.0
    fcounter = 0


    for name in os.listdir(folder1):
         new.append(name)
    C = new[len(new) // 2:]
    # D = ['238.txt', '239.txt', '24.txt', '241.txt', '242.txt', '243.txt', '244.txt', '245.txt']
    for name in C:
        name1 = folder2 + name
        input3 = open(name1, 'r')
        readfile = input3.read()
        input3.close()

        new1 = readfile.split()
        readfile = (sorted(set(new1)))
        #print(readfile)

        #print("Comparing it with jdm")
        for val in jdm:
            if val in readfile:
                # print("1")
                jdm1.append(jdm[val])
            else:
                # print("0")
                jdm1.append(0)
        #print(jdm1)
        sumjdm = sum(jdm1)
        #print(sumjdm)

        #print("Comparing it with arxiv")
        for val in arxiv:
            if val in readfile:
                # print("1")
                arxiv1.append(arxiv[val])
            else:
                # print("0")
                arxiv1.append(0)
        #print(arxiv1)
        sumarxiv = sum(arxiv1)
        #print(sumarxiv)

        #print("Comparing it with plos")
        for val in plos:
            if val in readfile:
                # print("1")
                plos1.append(plos[val])
            else:
                # print("0")
                plos1.append(0)
        #print(plos1)
        sumplos = sum(plos1)
        #print(sumplos)

        classified = max(sumjdm, sumarxiv, sumplos)
        #print(classified)
        print("Actual class:")
        if folder2 == "arxiv/":
            print("ARXIV")
        if folder2 == "jdm/":
            print("JDM")
        if folder2 == "plos/":
            print("PLOS")

        print("Classified class:")
        if classified == sumjdm:
            print("JDM")
            jdmcounter += 1
        if classified == sumarxiv:
            print("ARXIV")
            arxivcounter += 1
        if classified == sumplos:
            print("PLOS")
            ploscounter += 1

        sumjdm == 0
        sumplos == 0
        sumarxiv == 0
        plos1 = []
        jdm1 = []
        arxiv1 = []
        totalcounter += 1

    if folder2 == "arxiv/":
        fcounter = arxivcounter
        class1 = "ARXIV"
    if folder2 == "jdm/":
        fcounter = jdmcounter
        class1 = "JDM"
    if folder2 == "plos/":
        fcounter = ploscounter
        class1 = "PLOS"

    print("-----------------------------")
    print("Total files processed:")
    print(totalcounter)
    print("Files classified correctly:")
    print(fcounter)

    print("Accuracy of below class in percentage:")
    print(class1)
    total = ((fcounter*100/totalcounter))
    print(total)
    print("------------------------------")

if __name__ == "__main__":
    print("In main function: Training is in progress....(Estimated time to process 2-3 mins)")
    stop = load_stop()
    plos = list_files(stop)
    jdm = list_files1(stop)
    arxiv = list_files2(stop)
    vocabulary = (Counter(plos) + Counter(jdm) + Counter(arxiv))

    folder1 = './plos'
    folder2 = "plos/"
    folder3 = './jdm'
    folder4 = "jdm/"
    folder5 = './arxiv'
    folder6 = "arxiv/"

    newarr = loadfile(plos, folder1, folder2)
    newarr1 = loadfile(jdm, folder3, folder4)
    newarr2 = loadfile(arxiv, folder5, folder6)

    print("Testing phase started:")
    classification(plos, jdm, arxiv, folder5, folder6)
    classification(plos, jdm, arxiv, folder1, folder2)
    classification(plos, jdm, arxiv, folder3, folder4)
