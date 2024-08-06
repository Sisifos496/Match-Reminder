from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Importing Libraries

teams_I_love = ['Paris Saint-Germain', 'Borussia Dortmund', 'Manchester United', 'Manchester City', 'Chelsea', 'Liverpool', 'Napoli', 'AS Roma', 'AC Milan', 'Barcelona', 'Tottenham Hotspur', 'Bayern Münich', 'Internazionale', 'Lazio', 'Juventus', 'Galatasaray', 'Arsenal', 'Real Madrid', 'Besiktas', 'Fenerbahce']
# A list of teams I love depends on your personal preferences

browser = webdriver.Safari()
# Opens the browser (Safari)

browser.get('https://www.espn.in/football/fixtures')
# Opens the website

time.sleep(1)
# Waits for 1 second in case the element is not downloaded yet EC also could have been used to determine if elements are loaded or not

anchor_elements = browser.find_elements(By.XPATH, "//div[@class='mt3']//a")
# It gets all anchor elements from divs with the class of 'mt3'

separated_teams = [anchor_elements[n:n+6] for n in range(0, len(anchor_elements), 6)]
# It separates the anchor elements into 6 sublists because every match has 6 datas, and I want to gruop the datas of the same match in the same sublist

all_matches = []

for teams in separated_teams:
    if teams[1].text in teams_I_love or teams[4].text in teams_I_love:
    # Second and fifth anchor elements consist name of the team in the website, so I check if they match with the teams I love
        first_team = teams[1]
        second_team = teams[4]
        # If it matches assign new variables
        match = f"{first_team.text} {teams[2].text} {second_team.text} {teams[5].text}"
        all_matches.append(match)
        # Then add all matches to a list

english_teams = ["Manchester United", "Manchester City", "Chelsea", "Liverpool", "Tottenham Hotspur", "Arsenal"]

for i in english_teams:
    if i in all_matches[-1]:
        all_matches.remove(all_matches[-1])

for i in all_matches:
    print(i, "\n")
    #Print all the matches

time.sleep(2)

browser.quit()

