import matplotlib.pyplot as plt
import csv

def plot(file):
    wojcount = 0
    shamscount = 0
    woj = []
    shams = []
    wdate = ["2022-06-30"]
    sdate = ["2022-06-30"]
    wq = "2022-06-30"
    sq = "2022-06-30"

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] == 'woj':
                if wq == row[0]:
                    wojcount += 1
                else:
                    wdate.append(row[0])
                    woj.append(wojcount)
                    wojcount += 1
                    wq = row[0]
            if row[1] == 'woj':
                if sq == row[0]:
                    shamscount += 1
                else:
                    sdate.append(row[0])
                    shams.append(shamscount)
                    shamscount += 1
                    sq = row[0]

    print(woj)
    print(wdate)
    print(shams)
    # plt.plot(wdate, woj, color = "#444444", label="Woj Bombs")
    # plt.show()

plot("finale.csv")
        
