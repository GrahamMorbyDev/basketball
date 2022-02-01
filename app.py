# Import data from constants
import constants
import copy
user_viewing = True


def show_welcome_message():
    print("\n Here are the choices you have:")
    print("""
    --- BASKETBALL STATS TOOL ---
    A) = Show team stats
    B) = QUIT this application
    """)


def clean_data(data):
    for key, value in enumerate(data):

        # Update to experience to bool
        if value['experience'] == 'YES':
            value['experience'] = True
        else:
            value['experience'] = False

        # Update height to an INT value
        height = value['height']
        height = int(height.split()[0])
        value['height'] = height
    return data


def split_players(players, teams):
    player_teams = {}

    for i, team_name in enumerate(teams):
        full_teams = {}
        keys = range(6)

        for j in keys:
            full_teams[str(j)] = players[i * 6 + j]
        player_teams[team_name] = full_teams

    return player_teams


def dict_extract(team_name, players, key):
    sub_dict = {value[key] for (player, value) in players[team_name].items()}
    if key == 'height':
        average_height = sum(sub_dict) / len(sub_dict)
        return str(round(average_height, 1))
    else:
        return ', '.join(['{}'.format(name) for name in sub_dict])


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
    print('--------------------')


if __name__ == '__main__':
    while user_viewing:
        show_welcome_message()
        user_option = input('What do you wish to do?   ')
        list_str = ['a', 'b']
        try:
            if user_option.lower() not in list_str:
                raise ValueError(
                    'Sorry that was the wrong input')
        except ValueError as err:
            print(
                "Please select a valid option: A) Show team data or B) Quit this application")
            print("({})".format(err))
        else:
            if user_option.lower() == 'a':
                new_team_data = copy.deepcopy(constants.PLAYERS)
                players = clean_data(new_team_data)
                players = split_players(players, constants.TEAMS)

                # Display team and stats
                user_team = input(
                    'Which team would you like to view? 0 = Panthers, 1 = Bandits, 2 = Warriors   ')
                try:
                    user_team = int(user_team)
                    if user_team > 2:
                        raise ValueError(
                            'Please select the required team from the list: 0 = Panthers, 1 = Bandits, 2 = Warriors')
                except ValueError as err:
                    print(
                        "Remember you can only select from the following: 0 = Panthers, 1 = Bandits, 2 = Warriors")
                    print("({})".format(err))
                else:
                    show_team_data(user_team, players)
                    players = None
                    input('Press Enter to continue...')
            else:
                print('Thank you for using the stats program!')
                user_viewing = False
                exit()
