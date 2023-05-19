import json
player = {
"joye":[],
"darel":[],
"clare":[]
}
ratio = {
    "1":1,
    "2":6
}
score_list ={
    "joye":10,
    "darel":10,
    "clare":10
}

def placeBet():
    for o in player:
        print (o +" Place your bet")
        x = input()
        player[o].append( parseBet(x,o))
        
    json_object = json.dumps(player, indent=4)
    with open("db.json", "w") as outfile:
       outfile.write(json_object)
 

def parseBet(inp,o):
    new = inp.split(" ")
    ret = {}
    while len(new)>=2:
           ret[new[0]]=int (new[1])
           score_list[o] -= int (new[1])
           new.pop(0) 
           new.pop(0) 
    return ret 
        


def settleScore(game,winner):
    for i in player:
        for horse in player[i][game]:
            if str(winner) == horse:
                score_list[i] += player[i][game][horse]*ratio[horse] #append score to the socre list  
                print("Player: ",i, "wins",str(player[i][game][horse]*ratio[horse]))
    json_object = json.dumps(score_list, indent=4)
    with open("score.json", "w") as outfile:
       outfile.write(json_object)

# for game in range(2):
#     placeBet()
#     print("Which horse won the game?")
#     winner = input()
#     settleScore(game,winner)
# print("Game End, Winner is ",)    


placeBet()
print("Winner ?")
v =input()
settleScore(0,v)