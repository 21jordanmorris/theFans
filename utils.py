from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.injury_report import get_injury_report
from basketball_reference_scraper.players import get_stats
from basketball_reference_scraper.seasons import get_schedule
import pandas as pd

def getTeamMisc(year):
    atl = get_team_misc('ATL', year).to_frame().transpose()
    brk = get_team_misc('BRK', year).to_frame().transpose()
    bos = get_team_misc('BOS', year).to_frame().transpose()
    cho = get_team_misc('CHO', year).to_frame().transpose()
    chi = get_team_misc('CHI', year).to_frame().transpose()
    cle = get_team_misc('CLE', year).to_frame().transpose()
    dal = get_team_misc('DAL', year).to_frame().transpose()
    den = get_team_misc('DEN', year).to_frame().transpose()
    det = get_team_misc('DET', year).to_frame().transpose()
    gsw = get_team_misc('GSW', year).to_frame().transpose()
    hou = get_team_misc('HOU', year).to_frame().transpose()
    ind = get_team_misc('IND', year).to_frame().transpose()

    lac = get_team_misc('LAC', year).to_frame().transpose()
    lal = get_team_misc('LAL', year).to_frame().transpose()
    mem = get_team_misc('MEM', year).to_frame().transpose()
    mia = get_team_misc('MIA', year).to_frame().transpose()
    mil = get_team_misc('MIL', year).to_frame().transpose()
    mint = get_team_misc('MIN', year).to_frame().transpose()
    nop = get_team_misc('NOP', year).to_frame().transpose()
    nyk = get_team_misc('NYK', year).to_frame().transpose()
    okc = get_team_misc('OKC', year).to_frame().transpose()
    orl = get_team_misc('ORL', year).to_frame().transpose()
    phi = get_team_misc('PHI', year).to_frame().transpose()
    pho = get_team_misc('PHO', year).to_frame().transpose()

    por = get_team_misc('POR', year).to_frame().transpose()
    sac = get_team_misc('SAC', year).to_frame().transpose()
    sas = get_team_misc('SAS', year).to_frame().transpose()
    tor = get_team_misc('TOR', year).to_frame().transpose()
    uta = get_team_misc('UTA', year).to_frame().transpose()
    was = get_team_misc('WAS', year).to_frame().transpose()

    frames = [atl,brk,bos,cho,chi,cle,dal,den,det,gsw,hou,ind,lac,lal,mem,mia,mil,mint,nop,nyk,okc,orl,phi,pho,por,sac,sas,tor,uta,was]
    return pd.concat(frames)

def get_next_day(day):
    if day == "Monday":
        return "Tuesday"
    elif day == "Tuesday":
        return "Wednesday"
    elif day == "Wednesday":
        return "Thursday"
    elif day == "Thursday":
        return "Friday"
    elif day == "Friday":
        return "Saturday"
    elif day == "Saturday":
        return "Sunday"
    elif day == "Sunday":
        return "Monday"

def get_day_before(day):
    if day == "Monday":
        return "Sunday"
    elif day == "Tuesday":
        return "Monday"
    elif day == "Wednesday":
        return "Tuesday"
    elif day == "Thursday":
        return "Wednesday"
    elif day == "Friday":
        return "Thursday"
    elif day == "Saturday":
        return "Friday"
    elif day == "Sunday":
        return "Saturday"

def get_teams_last_twenty_init():
    how_many_games = [0] * 20
    teams = [
        'ATL','BRK','BOS','CHO','CHI','CLE','DAL','DEN',
        'DET','GSW','HOU','IND','LAC','LAL','MEM','MIA', 
        'MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO', 
        'POR','SAC','SAS','TOR','UTA','WAS']
    teams_last = {k:how_many_games for k in teams}
    
    return teams_last

def get_win_loss_percentage_last_twenty(team, team_dict):
    current_last_twenty = team_dict[team]
    wins = current_last_twenty.count('W')
    losses = current_last_twenty.count('L')
    if losses == 0:
        if wins > 0:
            return 1
        else:
            return 0
    else:
        return wins / (wins + losses)

def get_missing_win_shares(injury_report, team):
    team_injuries = injury_report.loc[injury_report['TEAM'] == team]
    team_injuries = team_injuries.loc[team_injuries['STATUS'] == 'Out']
    team_injuries = list(team_injuries['PLAYER'])
    win_shares = 0
    for player in team_injuries:
        try:
            player_stats = get_stats(player, stat_type='ADVANCED').tail(1)
            if not player_stats.loc[player_stats['SEASON'] == '2019-20'].empty:
                win_shares += list(player_stats['WS'])[0]
        except:
            pass
    return round(win_shares)

def get_first_no_result_date(entire_schedule):
    upcoming_games = entire_schedule[pd.isnull(entire_schedule['HOME_PTS'])].head(1)
    return list(upcoming_games['DATE'])[0]
