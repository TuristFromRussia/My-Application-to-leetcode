def convert():
    s = "Hellomydearfriendiloveyou"
    numRows = 8

    m = 0
    n = 0
    siter = 0
    way = True
    between1d = []
    between2d = []

    for i in range(numRows):
        between1d.append(0)

    between2d.append(between1d)
    between1d = []


    while siter < len(s):

        if n < numRows and way:

            between2d[m][n] = s[siter]
            siter +=1
            n += 1
            if n == numRows:
                n -=1
                way = False

        if n > 0 and way == False:
            for i in range(numRows):
                between1d.append(0)
            between2d.append(between1d)
            between1d = []
            n -= 1
            m += 1
            between2d[m][n] = s[siter]
            siter +=1
            if n == 0:
                way = True
                n +=1


    stroka = ''
    result = ""
    i = 0

    for i in range(numRows):
        
        for j in range(len(between2d)):


            if between2d[j][i] != 0:
                result += between2d[j][i]
                stroka += between2d[j][i] + ' '
            else: 
                stroka += '  '
        
        print(stroka)
        stroka = ''


    print(result)