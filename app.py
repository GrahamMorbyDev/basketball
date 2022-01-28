# Import data from contants
import constants


def show_help():
    print("\n Here are the choices you have:")
    print("""
    --- HELP MENU ---
    'QUIT' = QUIT this application
    'HELP' = Show this help
    """)


def split_players(players, teams):
    player_teams = {}

    for i, team_name in enumerate(teams):
        full_teams = {}
        keys = range(6)

        for j in keys:
            full_teams[str(j)] = players[i * 6 + j]
        player_teams[team_name] = full_teams

    return player_teams


def clean_data():
    players = constants.PLAYERS.copy()
    for key, value in enumerate(players):

        # Update to experience to bool
        if value['experience'] == 'YES':
            value['experience'] = True
        else:
            value['experience'] = False

        # Update height to an INT value
        height = value['height']
        height = int(height.split()[0])
        value['height'] = height
    return players


def dict_extract(team_name, players, key):
    sub_dict = {value[key] for (player, value) in players[team_name].items()}
    if key == 'height':
        average_height = sum(sub_dict) / len(sub_dict)
        return str(average_height)
    else:
        return (', '.join(['{}'.format(name) for name in sub_dict]))


def show_team_data(team_id, players):
    team_id = int(team_id)
    team_name = list(players.keys())[team_id]

    # team name
    print('Team: ' + team_name)
    print('--------------------')
    print('Total Players: {}'.format(len(players[team_name])))
    print('--------------------')

    # player names
    print('Players on teams: ')
    print(dict_extract(team_name, players, 'name') + '\n')

    # Guardian names
    print('Player guardians: ')
    print(dict_extract(team_name, players, 'guardians') + '\n')

    # Average Height
    print('Average height of team:')
    print(dict_extract(team_name, players, 'height'))


if __name__ == '__main__':
    print('BASKETBALL STATS TOOL')
    show_help()
    players = clean_data()
    players = split_players(players, constants.TEAMS)
    
    # Display team and stats
    user_team = input(
        'Which team would you like to view? 0 = Panthers, 1 = Bandits, 2 = Warriors   ')
    if user_team.lower() == 'quit':
        exit()
    elif user_team.lower() == 'help':
        show_help()
    else:
        show_team_data(user_team, players)
        end_user = input("Type 'enter' to contiune or 'quit' to close the program... ")
    
