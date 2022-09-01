import csv
import numpy as np
import pandas as pd

#Jank cleansing formula
lower = ['Free', 'Italian', 'So', 'RFA', 'After', 'Four-time', 'Teams', 'Year', 'Deal', 'Pick', 'Top', 'As', 'The', 'ESPN', 'Total', 'Restricted', 'ESPN,', 'GM', 'WME', 'CEO', 'NBA', 'All', 'Two-time', 'All-NBA', 'Star', 'Sources:', 'Two', 'ESPN.', 'MVP', 'G', "F", 'C', 'F/C', 'No.', 'All-Star', 'Australian']
agh = 'Atlanta Hawks Boston Celtics Brooklyn Nets Charlotte Hornets Chicago Bulls Cleveland Cavaliers Dallas Mavericks Denver Nuggets Detroit Pistons Golden State Warriors Houston Rockets Indiana Pacers Los Angeles Clippers Los Angeles Lakers Memphis Grizzlies Miami Heat Milwaukee Bucks Minnesota Timberwolves New Orleans Pelicans New York Knicks Oklahoma City Thunder Orlando Magic Philadelphia 76ers Phoenix Suns Portland Trail Blazers Sacramento Kings San Antonio Spurs Toronto Raptors Utah Jazz Washington Wizards'
teams = agh.split()

def ligma(file1, file2):
    #combines to dataframes into one csv
    df = pd.concat(map(pd.read_csv, [file1, file2]), ignore_index=True)
    df.to_csv(df.to_csv (fr'C:\Users\User\Desktop\code\personal\wojvshams webscraping\zerobraincells.csv', index = False, header=True))
    file = 'zerobraincells.csv'

    new_content = []
    new_user = []
    new_date = []
    count = 0

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            content = row[2]
            words = content.split()
            
            date = row[0]

            #lowercases all unuseful words in tweets
            for a in range(len(words)):
                if "â€" in words[a]:
                    index = words[a].find("â€")
                    words[a] = words[a][0:index]

                if words[a] in lower or "@" in words[a]:
                    words[a] = words[a].lower()

            plz = []

            for a in words:
                cap = False
                digit = False
                isTeam = False

                for x in teams:
                    if x in a:
                        isTeam = True

                for i in a:
                    if i.isupper():
                        cap = True
                    if i.isdigit():
                        digit = True
                
                if cap == True and digit == False and isTeam == False:
                    plz.append(a)

            two = []
            index = 0
            if len(plz) >= 2:
                while index < 2:
                    if "," in plz[index]:
                        plz[index] = plz[index][:len(plz[index]) - 1]
                    two.append(plz[index])
                    index += 1
            else:
                pass
            
            content = ' '.join(two)
            
            user = row[1]

            #generalizes users for readability
            if "shams" in user.lower():
                user = "shams"
            elif "woj" in user.lower():
                user = "woj"

            if count > 0:
                new_content.append(content)
                new_user.append(user)
                new_date.append(date)
            count += 1
        
        d = {'date': new_date, 'user': new_user, 'content': new_content}
        df = pd.DataFrame(data = d)
        df.to_csv(df.to_csv (fr'C:\Users\User\Desktop\code\personal\wojvshams webscraping\zerobraincells.csv', index = False, header=True))



ligma('ShamsCharania.csv', 'wojespn.csv')