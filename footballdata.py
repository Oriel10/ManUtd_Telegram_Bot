import requests
import json
import Constants as constants

# man_utd_url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/33/next/1"

querystring = {"timezone":"Europe/London"}

class Date:
    def __init__(self, day, month, year) -> None:
        self.m_day = day
        self.m_month = month
        self.m_year = year
    
    def getDateStr(self):
        return str(self.m_day) +"."+ str(self.m_month) +"."+ str(self.m_year)

class Hour:
    def __init__(self, hour, minute) -> None:
        self.m_hour = hour
        self.m_minute = minute
    
    def getHourStr(self):
        return str(self.m_hour) +":"+ str(self.m_minute)

class Fixture:
    def __init__(self, home_team, away_team, league_name, game_date, game_hour, home_team_goals = 0, away_team_goals = 0) -> None:
        self.m_home_team = home_team
        self.m_away_team = away_team
        self.m_league_name = league_name
        self.m_game_date = game_date
        self.m_game_hour = game_hour
        self.m_home_team_goals = str(home_team_goals)
        self.m_away_team_goals = str(away_team_goals)

    
    def GetFixtures(self):
        game_name = self.m_home_team + " " + self.m_home_team_goals +  " - " + self.m_away_team_goals + " " + self.m_away_team + "\n"
        game_league = self.m_league_name + "\n"
        game_time = "Date: " + self.m_game_hour.getHourStr() + " - " + self.m_game_date.getDateStr()
        return game_name + game_league + game_time

# {
#     "api":{"results":1,
#             "fixtures":[{
#                 "fixture_id":867954,
#                 "league_id":4335,
#                 "league":{
#                     "name":"Premier League",
#                     "country":"England",
#                     "logo":"https:\/\/media.api-sports.io\/football\/leagues\/39.png",
#                     "flag":"https:\/\/media.api-sports.io\/flags\/gb.svg"
#                 },
#                 "event_date":"2022-08-07T14:00:00+01:00",
#                 "event_timestamp":1659877200,
#                 "firstHalfStart":null,
#                 "secondHalfStart":null,
#                 "round":"Regular Season - 1",
#                 "status":"Not Started",
#                 "statusShort":"NS",
#                 "elapsed":0,
#                 "venue":"Old Trafford",
#                 "referee":"P. Tierney",
#                 "homeTeam":{
#                     "team_id":33,
#                     "team_name":"Manchester United",
#                     "logo":"https:\/\/media.api-sports.io\/football\/teams\/33.png"
#                 },
#                 "awayTeam":{
#                     "team_id":51,
#                     "team_name":"Brighton",
#                     "logo":"https:\/\/media.api-sports.io\/football\/teams\/51.png"
#                     },
#                 "goalsHomeTeam":null,
#                 "goalsAwayTeam":null,
#                 "score":{
#                     "halftime":null,
#                     "fulltime":null,
#                     "extratime":null,
#                     "penalty":null
#                 }
#             }]
#         }
# }


def checkInt(my_str):
    if my_str[0] in ('-', '+'):
        return my_str[1:].isdigit()
    return my_str.isdigit()

def getNextFixturesList(num_requested_fixtures : str):
    assert(type(num_requested_fixtures) == str)
    if(not checkInt(num_requested_fixtures)):
        return None

    man_utd_url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/33/next/" + num_requested_fixtures
    response = requests.request("GET", man_utd_url, headers=constants.football_headers, params=querystring)
    response_text = response.text.replace("null", "None") #fit to python format
    fixtures_dict = eval(str(response_text))
    # print(fixtures_dict["api"]["fixtures"])
    # for fixture in fixtures_dict["api"]["fixtures"]:

    # json_string = '''{"api":{"results":1,"fixtures":[{"fixture_id":867954,"league_id":4335,"league":{"name":"Premier League","country":"England","logo":"https:\/\/media.api-sports.io\/football\/leagues\/39.png","flag":"https:\/\/media.api-sports.io\/flags\/gb.svg"},"event_date":"2022-08-07T14:00:00+01:00","event_timestamp":1659877200,"firstHalfStart":null,"secondHalfStart":null,"round":"Regular Season - 1","status":"Not Started","statusShort":"NS","elapsed":0,"venue":"Old Trafford","referee":"P. Tierney","homeTeam":{"team_id":33,"team_name":"Manchester United","logo":"https:\/\/media.api-sports.io\/football\/teams\/33.png"},"awayTeam":{"team_id":51,"team_name":"Brighton","logo":"https:\/\/media.api-sports.io\/football\/teams\/51.png"},"goalsHomeTeam":null,"goalsAwayTeam":null,"score":{"halftime":null,"fulltime":null,"extratime":null,"penalty":null}}]}}'''
    # json_string = json_string.replace("null", "None")
    # fixtures_dict = eval(str(json_string))
    # print(len(fixtures_dict["api"]))
    if(fixtures_dict["api"]["results"] == 0):
        return "No Games Found"
    fixtures_list = []
    for f in fixtures_dict["api"]["fixtures"]:
        home_team = f["homeTeam"]["team_name"]
        away_team = f["awayTeam"]["team_name"]
        league_name = f["league"]["name"]
        #"event_date":"2022-08-07T14:00:00+01:00",
        event_date = f["event_date"]
        game_date = Date(event_date[8:10], event_date[5:7], event_date[0:4])
        game_hour = Hour(event_date[11:13], event_date[14:16]) 
        fixtures_list.append(Fixture(home_team, away_team, league_name, game_date, game_hour))
    # fixtures_str = []]
    # for f in fixtures_list:
    #     fixtures_str += f.GetFixtures()
    return fixtures_list

def getPrevFixturesList(num_requested_fixtures : str):
    assert(type(num_requested_fixtures) == str)
    if(not checkInt(num_requested_fixtures)):
        return None

    man_utd_url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/33/last/" + num_requested_fixtures
    response = requests.request("GET", man_utd_url, headers=constants.football_headers, params=querystring)
    response_text = response.text.replace("null", "None") #fit to python format
    fixtures_dict = eval(str(response_text))
    if(fixtures_dict["api"]["results"] == 0):
        return "No Games Found"
    fixtures_list = []
    for f in fixtures_dict["api"]["fixtures"]:
        home_team = f["homeTeam"]["team_name"]
        home_team_goals = f["goalsHomeTeam"]
        away_team = f["awayTeam"]["team_name"]
        away_team_goals = f["goalsAwayTeam"]
        league_name = f["league"]["name"]
        #"event_date":"2022-08-07T14:00:00+01:00",
        event_date = f["event_date"]
        game_date = Date(event_date[8:10], event_date[5:7], event_date[0:4])
        game_hour = Hour(event_date[11:13], event_date[14:16]) 
        fixtures_list.append(Fixture(home_team, away_team, league_name, game_date, game_hour, home_team_goals, away_team_goals))
    return fixtures_list
    


        
        

# getPrevFixturesList("2")

