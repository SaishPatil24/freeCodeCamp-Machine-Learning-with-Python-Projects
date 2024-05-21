# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

my_history = []
init_play = prev_play = 'S'
opponent_list = [False, False, False, False]
ideal_response = {'P' : 'R', 'R' : 'S', 'S' : 'P'}
opponent_quincy_counter = -1
play_order = [{
    "RR" : 0, 
    "RP" : 0, 
    "RS" : 0, 
    "PR" : 0, 
    "PP" : 0, 
    "PS" : 0, 
    "SR" : 0, 
    "SP" : 0, 
    "SS" : 0, 
    }]

def player(prev_opponent_play, opponent_history = []):
    global my_history, prev_play, opponent_list, ideal_response, opponent_quincy_counter, play_order
    opponent_history.append(prev_opponent_play)
    my_history.append(prev_play)