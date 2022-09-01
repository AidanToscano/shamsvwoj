import csv
import pandas as pd

#final consolidation list
def points(file):
    final_date = []
    final_user = []
    final_content = []
    count = 0

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            match = False
            if count == 0:
                pass
            elif not final_date:
                final_date.append(row[0])
                final_user.append(row[1])
                final_content.append(row[2])
            else:
                for i in range(len(final_content)):
                    repeat = False
                    if row[2] == final_content[i]:
                        repeat = True
                        if final_date[i] > row[0]:
                            final_date[i] = row[0]
                            final_user[i] = row[1]
                            final_content[i] = row[2]
                            break
                        else:
                            break

                if repeat == False and row[2] != "":
                    final_date.append(row[0])
                    final_user.append(row[1])
                    final_content.append(row[2])
            
            count += 1
        
        for i in range(len(final_date)):
            final_date[i] = final_date[i][0:11]

        d = {'date': final_date, 'user': final_user, 'content': final_content}
        df = pd.DataFrame(data = d)
        df.to_csv(df.to_csv (fr'C:\Users\User\Desktop\code\personal\wojvshams webscraping\finale.csv', index = False, header=True))

#tallies the points and prints the results
def count(file):
    shams = 0
    woj = 0

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] == 'woj':
                woj += 1
            elif row[1] == 'shams':
                shams += 1

    print(shams)
    print(woj)

points('zerobraincells.csv')
count('finale.csv')


