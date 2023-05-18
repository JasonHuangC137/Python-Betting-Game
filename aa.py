import json
player = {
"joye":[
    {"1":10,"2":20}#bet for gmae 1 
],
"darel":[{"1":10}]
}


def placeBet():
    for o in player:
        print (o +" Place your bet")
        x = input()
        player[o].append( parseBet(x))
    json_object = json.dumps(player, indent=4)
    with open("db.json", "w") as outfile:
       outfile.write(json_object)
 

def parseBet(inp):
    new = inp.split(" ")
    ret = {}
    while len(new)>=2:
           ret[new[0]]=int (new[1])
           new.pop(0) 
           new.pop(0) 
    return ret 
        


def settleScore(game,winner):
    for i in player:
        for horse in player[i][game]:
            if winner == horse:
                #do the score 


for game in range(2):
    placeBet()
    print("Which horse won the game?")
    winner = input()
    settleScore(game,winner)
print("Game End, Winner is ",)    