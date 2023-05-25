import json
player = {
"Joye":[],
"Jessie":[],
"Una":[], 
"Katrina":[],
"Wayne":[],
"Joanna":[],
"Jack":[]
}
ratio = {
    "1":2.1,
    "2":3.5,
    "3":4.8,
    "4":4.2,
    "5":15.8,
    "6":12.8,
    "7":18.7,
    "8":115
}
score_list ={
}
for p in player:
    score_list[p]=5000 #inicial number
print (score_list)

def placeBet():
    for o in player:
        print (o +" Place your bet")
        x = input()
        player[o].append( parseBet(x,o))
        
    json_object = json.dumps(player, indent=4)
    with open("db.json", "w") as outfile:
       outfile.write(json_object)
 

def parseBet(inp,o):
    new = inp.strip().split(" ")
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

for game in range(10):
    print("New Round",str(game+1))
    placeBet()
    print("Which horse won the game?")
    winner = input()
    settleScore(game,winner)
    print ("----SCORE-----")
    for i in score_list:
        print (i," : ",score_list[i])
    print ("--------------")
print("Game Ended!")    


