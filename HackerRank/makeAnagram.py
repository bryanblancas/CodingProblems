def makeAnagram(a, b):
    count = 0
    ht1 = {}
    ht2 = {}

    for i in a:
        if(i in ht1):
            ht1[i] += 1
        else:
            ht1[i] = 1

    for i in b:
        if(i in ht2):
            ht2[i] += 1
        else:
            ht2[i] = 1

    for i in ht1:
        if(i in ht2):
            count += abs(ht1[i] - ht2[i])
            del ht2[i]
        else:
            count += ht1[i]

    for i in ht2:
        if(i in ht1):
            count += abs(ht2[i] - ht1[i])
            del ht1[i]
        else:
            count += ht2[i]

    return count


if __name__ == '__main__':

    print(makeAnagram("cd", "cd"))