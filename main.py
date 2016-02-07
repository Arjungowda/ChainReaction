import copy
import  math
class board_game:
     def __init__(self, matrix = [], matrix_val = [] , matrix_moves = [], player = 'X',depth = 2):
         self.matrix = matrix
         self.matrix_val = matrix_val
         self.matrix_moves = matrix_moves
         self.player = player
         self.depth = depth

#Sneak step:-
def adj(mat, row, col, player): #Getting for player = X
    p = mat[row][col]
    #print p
    if mat[row][col] == 'O' or mat[row][col] == 'X':
        return 0
    elif row == 0 and col == 0:                                         #(0,0)
        if (mat[row+1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    elif row == 4 and col == 0:                                         #(4,0)
        if (mat[row-1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    elif row == 4 and col == 4:                                         #(4,4)
        if (mat[row-1][col] != player and mat[row][col-1] != player):
            return game.matrix_val[row][col]
    elif row == 0 and col == 4:                                         #(0,4)
        if (mat[row][col-1] != player and mat[row+1][col] != player):
            return game.matrix_val[row][col]
    elif 0 < row < 4 and col == 0:                                      # Left Column
        if (mat[row-1][col] != player and mat[row+1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    elif 0 < col < 4 and row == 0:                                      # Top Row
        if (mat[row][col-1] != player and mat[row+1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    elif 0 < col < 4 and row == 4:                                      # Bottom Row
        if (mat[row][col-1] != player and mat[row-1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    elif col == 4 and 0 < row < 4:                                      # Right Column
        if (mat[row][col-1] != player and mat[row+1][col] != player and mat[row-1][col] != player):
            return game.matrix_val[row][col]
    else:                                                               # Middle Elements
        if (mat[row][col-1] != player and mat[row-1][col] != player and mat[row+1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    return 0

#Raid step:-
def raidMove(game, row, col, player):
    maxRaidSum = 0
    #maxRaidSum = game.matrix_val[row][col]
    # max_sum_cur = 0 left_idx = None right_idx = None
    if game.matrix_moves[row][col] == '*':
        if row == 0 and col == 0:                                         #(0,0)
            if game.matrix_moves[row+1][col] == player:
                if game.matrix_moves[row][col+1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col+1]
            elif game.matrix_moves[row][col+1] == player:
                if game.matrix_moves[row+1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row+1][col]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif row == 4 and col == 0:                                         #(4,0)
            if game.matrix_moves[row-1][col] == player:
                if game.matrix_moves[row][col+1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col+1]
            elif game.matrix_moves[row][col+1] == player:
                if game.matrix_moves[row-1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row-1][col]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif row == 4 and col == 4:                                         #(4,4)
            if game.matrix_moves[row-1][col] == player:
                if game.matrix_moves[row][col-1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col-1]
            elif game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row-1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row-1][col]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif row == 0 and col == 4:                                         #(0,4)
            if game.matrix_moves[row+1][col] == player:
                if game.matrix_moves[row][col-1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col-1]
            elif game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row+1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row+1][col]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif 0 < row < 4 and col == 0:                                      # Left Column
            if game.matrix_moves[row-1][col] == player or game.matrix_moves[row+1][col] == player or game.matrix_moves[row][col+1] == player:
                if game.matrix_moves[row-1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row-1][col]
                if game.matrix_moves[row+1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row+1][col]
                if game.matrix_moves[row][col+1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col+1]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif 0 < col < 4 and row == 0:                                      # Top Row
            if game.matrix_moves[row][col-1] == player or game.matrix_moves[row][col+1] == player or game.matrix_moves[row+1][col] == player:
                if game.matrix_moves[row][col-1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col-1]
                if game.matrix_moves[row][col+1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col+1]
                if game.matrix_moves[row+1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row+1][col]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif 0 < col < 4 and row == 4:                                      # Bottom Row
            if game.matrix_moves[row][col+1] == player or game.matrix_moves[row-1][col] == player or game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row][col+1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row+1][col]
                if game.matrix_moves[row-1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row-1][col]
                if game.matrix_moves[row][col-1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col-1]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif col == 4 and 0 < row < 4:                                      # Right Column
            if game.matrix_moves[row+1][col] == player or game.matrix_moves[row-1][col] == player or game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row+1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row+1][col]
                if game.matrix_moves[row-1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row-1][col]
                if game.matrix_moves[row][col-1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col-1]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        else:                                                               # Middle Elements
            if (game.matrix_moves[row][col-1] == player or game.matrix_moves[row-1][col] == player or game.matrix_moves[row+1][col] == player or game.matrix_moves[row][col+1] == player):
                if game.matrix_moves[row][col-1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col-1]
                if game.matrix_moves[row-1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row-1][col]
                if game.matrix_moves[row+1][col] == getOpp(player):
                    maxRaidSum += game.matrix_val[row+1][col]
                if game.matrix_moves[row][col+1] == getOpp(player):
                    maxRaidSum += game.matrix_val[row][col+1]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
    return 0

def getPlayerSum(game):
    playersum = 0
    oppPlayerSum = 0
    for value in range(len(game.matrix_moves)):
        for v in range(len(game.matrix_moves[value])):
            if game.matrix_moves[value][v] == game.player: #player
                playersum += game.matrix_val[value][v]
            b = getOpp(game.player)
            if game.matrix_moves[value][v] == b: #Opp_player
                oppPlayerSum += game.matrix_val[value][v]
    return playersum, oppPlayerSum

def print_output(game,left_idx,right_idx, flag):
    m = game.matrix_moves
    text_file = open("output.txt","w")
    if flag == 0:
        for i in range(5):
            for j in range(5):
                if i+1 == left_idx and j == right_idx and m[i][j] == "O":
                    text_file.write(game.player)
                elif i == left_idx and j+1 == right_idx and m[i][j] == "O":
                    text_file.write(game.player)
                elif i == left_idx and j-1 == right_idx and m[i][j] == "O":
                    text_file.write(game.player)
                elif i-1 == left_idx and j == right_idx and m[i][j] == "O":
                    text_file.write(game.player)
                elif i == left_idx and j == right_idx:
                    text_file.write(game.player)
                else:
                    text_file.write(m[i][j])
            text_file.write("\n")
    else:
        game.matrix_moves[left_idx][right_idx] = game.player
        for i in range(0,5):
            for j in range(0,5):
                text_file.write(game.matrix_moves[i][j])
            text_file.write("\n")

def GreedyBestFirst(game):
    raidSum = 0
    left_idx = None
    right_idx = None
    for row in range(len(game.matrix_val)):
        for col in range(len(game.matrix_val)):
            #if maxSum < game.matrix_val[row][col]:
            #temp = game.matrix_val[row][col]
            sneak_Sum = adj(game.matrix_moves, row, col, game.player)
            rsum= raidMove(game, row, col,game.player)
            #print rsum
            #print sneak_Sum
            flag = 0
            if sneak_Sum < rsum:
                if raidSum < rsum:
                    raidSum = rsum
                    left_idx = row
                    right_idx = col
                    flag = 0 # Raid Move
            else:
                if raidSum < sneak_Sum:
                    raidSum = sneak_Sum
                    left_idx = row
                    right_idx = col
                    flag = 1 # Sneak Move
            #outPrint(game,left_idx,right_idx,game.player)
            playerSum, oppPlayerSum = getPlayerSum(game)
            if flag == 1 and left_idx is not None and right_idx is not None:
                e = playerSum - oppPlayerSum
            elif flag == 0 and left_idx is not None and right_idx is not None:
                te = raidSum - game.matrix_val[left_idx][right_idx]
                e = playerSum - 2*te
    print 'Raid Sum'
    print raidSum
    print 'row and column:'
    print left_idx
    print right_idx
    print game.matrix_val[left_idx][right_idx]
    print_output(game,left_idx,right_idx, flag)
    #resMatrix, playerSum, oppPlayerSum = outPrint(game,left_idx,right_idx,game.player, flag)
    print 'Player sum:'
    print playerSum
    print 'opponent player sum:'
    print oppPlayerSum

def evalfunc(game, p):
    psum, oppsum = getPlayerSum(game)
    return psum - oppsum

def gamePlayerChange(p):
    if p == 'X':
        return 'O'
    else:
        return 'X'

def getOpp(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def checkForRaid(game, row, col, player):
    oppPlayer = getOpp(player)
    if game.matrix_moves[row][col] == '*':
        game.matrix_moves[row][col] = player
        if row == 0 and col == 0:                                         #(0,0)
            if game.matrix_moves[row+1][col] == player:
                if game.matrix_moves[row][col+1] == oppPlayer:
                    game.matrix_moves[row][col+1] = player
            elif game.matrix_moves[row][col+1] == player:
                if game.matrix_moves[row+1][col] == oppPlayer:
                    game.matrix_moves[row+1][col] = player
            return game
        elif row == 4 and col == 0:                                         #(4,0)
            if game.matrix_moves[row-1][col] == player:
                if game.matrix_moves[row][col+1] == oppPlayer:
                    game.matrix_moves[row][col+1] = player
            elif game.matrix_moves[row][col+1] == player:
                if game.matrix_moves[row-1][col] == oppPlayer:
                    game.matrix_moves[row-1][col] == player
            return game
        elif row == 4 and col == 4:                                         #(4,4)
            if game.matrix_moves[row-1][col] == player:
                if game.matrix_moves[row][col-1] == oppPlayer:
                    game.matrix_moves[row][col-1] = player
            elif game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row-1][col] == oppPlayer:
                    game.matrix_moves[row-1][col] = player
            return game
        elif row == 0 and col == 4:                                         #(0,4)
            if game.matrix_moves[row+1][col] == player:
                if game.matrix_moves[row][col-1] == oppPlayer:
                    game.matrix_moves[row][col-1] = player
            elif game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row+1][col] == oppPlayer:
                    game.matrix_moves[row+1][col] = player
            return game
        elif 0 < row < 4 and col == 0:                                      # Left Column
            if game.matrix_moves[row-1][col] == player or game.matrix_moves[row+1][col] == player or game.matrix_moves[row][col+1] == player:
                if game.matrix_moves[row-1][col] == oppPlayer:
                    game.matrix_moves[row-1][col] = player
                if game.matrix_moves[row+1][col] == oppPlayer:
                    game.matrix_moves[row+1][col] = player
                if game.matrix_moves[row][col+1] == oppPlayer:
                    game.matrix_moves[row][col+1] = player
            return game
        elif 0 < col < 4 and row == 0:                                      # Top Row
            if game.matrix_moves[row][col-1] == player or game.matrix_moves[row][col+1] == player or game.matrix_moves[row+1][col] == player:
                if game.matrix_moves[row][col-1] == oppPlayer:
                    game.matrix_moves[row][col-1] = player
                if game.matrix_moves[row][col+1] == oppPlayer:
                    game.matrix_moves[row][col+1] = player
                if game.matrix_moves[row+1][col] == oppPlayer:
                    game.matrix_moves[row+1][col] = player
            return game
        elif 0 < col < 4 and row == 4:                                      # Bottom Row
            if game.matrix_moves[row][col+1] == player or game.matrix_moves[row-1][col] == player or game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row][col+1] == oppPlayer:
                    game.matrix_moves[row][col+1] = player
                if game.matrix_moves[row-1][col] == oppPlayer:
                    game.matrix_moves[row-1][col] = player
                if game.matrix_moves[row][col-1] == oppPlayer:
                    game.matrix_moves[row][col-1] == player
            return game
        elif col == 4 and 0 < row < 4:                                      # Right Column
            if game.matrix_moves[row+1][col] == player or game.matrix_moves[row-1][col] == player or game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row+1][col] == oppPlayer:
                    game.matrix_moves[row+1][col] = player
                if game.matrix_moves[row-1][col] == oppPlayer:
                    game.matrix_moves[row-1][col] = player
                if game.matrix_moves[row][col-1] == oppPlayer:
                    game.matrix_moves[row][col-1] = player
            return game
        else:                                                               # Middle Elements
            if (game.matrix_moves[row][col-1] == player or game.matrix_moves[row-1][col] == player or game.matrix_moves[row+1][col] == player or game.matrix_moves[row][col+1] == player):
                if game.matrix_moves[row][col-1] == oppPlayer:
                    game.matrix_moves[row][col-1] = player
                if game.matrix_moves[row-1][col] == oppPlayer:
                    game.matrix_moves[row-1][col] = player
                if game.matrix_moves[row+1][col] == oppPlayer:
                    game.matrix_moves[row+1][col] = player
                if game.matrix_moves[row][col+1] == oppPlayer:
                    game.matrix_moves[row][col+1] = player
            return game
    return game

def checkForSneak(game,row,col, player):

    if game.matrix_moves[row][col] == 'O' or game.matrix_moves[row][col] == 'X':
        return game
    elif row == 0 and col == 0:                                         #(0,0)
        if (game.matrix_moves[row+1][col] != player and game.matrix_moves[row][col+1] != player):
            game.matrix_moves[row][col] = player
            return game
    elif row == 4 and col == 0:                                         #(4,0)
        if (game.matrix_moves[row-1][col] != player and game.matrix_moves[row][col+1] != player):
            game.matrix_moves[row][col] = player
            return game
    elif row == 4 and col == 4:                                         #(4,4)
        if (game.matrix_moves[row-1][col] != player and game.matrix_moves[row][col-1] != player):
            game.matrix_moves[row][col] = player
            return game
    elif row == 0 and col == 4:                                         #(0,4)
        if (game.matrix_moves[row][col-1] != player and game.matrix_moves[row+1][col] != player):
            game.matrix_moves[row][col] = player
            return game
    elif 0 < row < 4 and col == 0:                                      # Left Column
        if (game.matrix_moves[row-1][col] != player and game.matrix_moves[row+1][col] != player and game.matrix_moves[row][col+1] != player):
            game.matrix_moves[row][col] = player
            return game
    elif 0 < col < 4 and row == 0:                                      # Top Row
        if (game.matrix_moves[row][col-1] != player and game.matrix_moves[row+1][col] != player and game.matrix_moves[row][col+1] != player):
            game.matrix_moves[row][col] = player
            return game
    elif 0 < col < 4 and row == 4:                                      # Bottom Row
        if (game.matrix_moves[row][col-1] != player and game.matrix_moves[row-1][col] != player and game.matrix_moves[row][col+1] != player):
            game.matrix_moves[row][col] = player
            return game
    elif col == 4 and 0 < row < 4:                                      # Right Column
        if (game.matrix_moves[row][col-1] != player and game.matrix_moves[row+1][col] != player and game.matrix_moves[row-1][col] != player):
            game.matrix_moves[row][col] = player
            return game
    else:                                                               # Middle Elements
        if (game.matrix_moves[row][col-1] != player and game.matrix_moves[row-1][col] != player and game.matrix_moves[row+1][col] != player and game.matrix_moves[row][col+1] != player):
            game.matrix_moves[row][col] = player
            return game
    return game

def getChar(i,j):
    if (i == 8 or j == 8):
        return "root"
    return chr(ord('A')+j) + str(i+1)

def maximise(game, p, l_index, r_index, depth):
    if depth == 0: #check if matrix not empty
        val = evalfunc(game,p)
        text_file1.write(getChar(l_index, r_index)+","+str(int(game.depth) - int(depth))+","+ str(val))
        text_file1.write("\n")
        return val,l_index,r_index
    high = -1234567
    infinity = "Infinity"
    text_file1.write(getChar(l_index, r_index)+","+str(int(game.depth) - int(depth))+"," + str(infinity))
    text_file1.write("\n")
    m = game.matrix_moves
    for i in range(0,len(m)):
        for j in range(0,len(m)):
            if m[i][j] == '*':
                g = copy.deepcopy(game)
                g = checkForSneak(g,i,j,p)
                g = checkForRaid(g,i,j,p)
                #p = gamePlayerChange(p)
                e,a,b = minimise(g, p , i, j, int(depth)-1)
                if e > high:
                    high = e
                    l_index1 = i
                    r_index1 = j
                if(depth == game.depth):
                    text_file1.write("root"+","+str(int(game.depth) - int(depth))+","+str(high))
                else:
                    text_file1.write(getChar(l_index,r_index)+","+str(int(game.depth) - int(depth))+","+str(high))
                text_file1.write("\n")
    return high,l_index1,r_index1

def minimise(game,p,l_index,r_index,depth):
    if depth == 0:
        val = evalfunc(game, p)
        text_file1.write(getChar(l_index,r_index)+","+str(int(game.depth) - int(depth))+","+str(val))
        text_file1.write("\n")
        return val,l_index,r_index
    low = 1234567
    infinity = "Infinity"
    text_file1.write(getChar(l_index,r_index)+","+str(int(game.depth) - int(depth))+","+str(infinity))
    text_file1.write("\n")
    m = game.matrix_moves
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == '*':
                g = copy.deepcopy(game)
                g = checkForSneak(g,i,j,gamePlayerChange(p))
                g = checkForRaid(g,i,j,gamePlayerChange(p))
                #p = gamePlayerChange(p)
                e,a,b = maximise(g,p,i,j,int(depth)-1)
                if e < low:
                    low = e
                    l_index1 = i
                    r_index1 = j
                if(depth == game.depth):
                    text_file1.write("root"+","+str(int(game.depth) - int(depth))+","+str(low))
                else:
                    text_file1.write(getChar(l_index,r_index)+","+str(int(game.depth) - int(depth))+","+str(low))
                text_file1.write("\n")
    return low,l_index1,r_index1

def minMaxAlgo(game):
    #print 'root,0,-Infinity '
    evalsum,l_index,r_index = maximise(game,game.player,8, 8, game.depth)
    print "Eval and i and j",evalsum,l_index,r_index
    return

def battleSimulation(game):
    playerOne = game.matrix[1][0]
    playerTwo = game.matrix[4][0]
    while boardEmpty(game):
        playerOneMove(game)
        if boardEmpty(game):
            playerTwoMove(game)
    return game

def boardEmpty(game):
    for row in range(len(game.matrix_val)):
        for col in range(len(game.matrix_val)):
            if game.matrix_moves[row][col] == '*':
                return 1
    return 0

def playerOneMove(game):
    playerOneGame = game.matrix[2][0]
    playerOneCutOffDepth = game.matrix[3][0]
    game.depth = playerOneCutOffDepth
    if playerOneGame == '1':
        GreedyBestFirst(game)
    elif playerOneGame == '2':
        minMaxAlgo(game)
    return

def playerTwoMove(game):
    playerTwoGame = game.matrix[5][0]
    playerTwoCutOffDepth = game.matrix[6][0]
    game.depth = playerTwoCutOffDepth
    if playerTwoGame == '1':
        GreedyBestFirst(game)
    elif playerTwoGame == '2':
        minMaxAlgo(game)
    return



def maximisealpha(game, p, l_index, r_index,alpha, beta, depth):
    aa = alpha
    bb = beta
    if alpha == -1234567:
        aa = '-Infinity'
    if alpha == 1234567:
        aa = 'infinity'
    if beta == -1234567:
        bb = '-Infinity'
    if beta == 1234567:
        bb = 'Infinity'
    if depth == 0: #check if matrix not empty
        val = evalfunc(game,p)
        text_file2.write(getChar(l_index, r_index)+","+str(int(game.depth) - int(depth))+","+ str(val)+","+ str(aa)+","+ str(bb))
        text_file2.write("\n")
        return val,l_index,r_index
    high = -1234567
    infinity = "-Infinity"
    text_file2.write(getChar(l_index, r_index)+","+str(int(game.depth) - int(depth))+"," + str(infinity)+","+ str(aa)+","+ str(bb))
    text_file2.write("\n")
    m = game.matrix_moves
    for i in range(0,len(m)):
        for j in range(0,len(m)):
            if m[i][j] == '*':
                g = copy.deepcopy(game)
                g = checkForSneak(g,i,j,p)
                g = checkForRaid(g,i,j,p)
                #p = gamePlayerChange(p)
                e,a,b = minimisealpha(g, p , i, j,alpha,beta, int(depth)-1)
                if e > high:
                    high = e
                    l_index1 = i
                    r_index1 = j
                if(high>=beta):
                    text_file2.write(getChar(l_index,r_index)+","+str(int(game.depth) - int(depth))+","+str(high)+","+ str(aa)+","+ str(bb))
                    text_file2.write("\n")
                    return high,i,j
                alpha=max(alpha,high)
                if alpha == 1234567:
                    aa = 'Infinity'
                elif alpha == -1234567:
                    aa = '-Infinity'
                else:
                    aa = alpha
                if(depth == game.depth):
                    text_file2.write("root"+","+str(int(game.depth) - int(depth))+","+str(high)+","+ str(aa)+","+ str(bb))
                else:
                    text_file2.write(getChar(l_index,r_index)+","+str(int(game.depth) - int(depth))+","+str(high)+","+ str(aa)+","+ str(bb))
                text_file2.write("\n")
    return high,l_index1,r_index1

def minimisealpha(game,p,l_index,r_index, alpha, beta, depth):
    aa = alpha
    bb = beta
    if alpha == -1234567:
        aa = '-Infinity'
    if alpha == 1234567:
        aa = 'infinity'
    if beta == -1234567:
        bb = '-Infinity'
    if beta == 1234567:
        bb = 'Infinity'
    if depth == 0:
        val = evalfunc(game, p)
        text_file2.write(getChar(l_index,r_index)+","+(game.depth - depth)+","+str(val)+","+ str(aa)+","+ str(bb))
        text_file2.write("\n")
        return val,l_index,r_index
    low = 1234567
    infinity = "Infinity"

    text_file2.write(getChar(l_index,r_index)+","+str(int(game.depth) - int(depth))+","+str(infinity)+","+ str(aa)+","+ str(bb))
    text_file2.write("\n")
    m = game.matrix_moves
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == '*':
                g = copy.deepcopy(game)
                g = checkForSneak(g,i,j,gamePlayerChange(p))
                g = checkForRaid(g,i,j,gamePlayerChange(p))
                #p = gamePlayerChange(p)
                e,a,b = maximisealpha(g,p,i,j,alpha,beta,int(depth)-1)
                if e < low:
                    low = e
                    l_index1 = i
                    r_index1 = j
                if(low<=alpha):
                    text_file2.write(getChar(l_index,r_index)+","+str(int(game.depth) - int(depth))+","+str(low)+","+ str(aa)+","+ str(bb))
                    text_file2.write("\n")
                    return low,i,j;
                beta=min(low,beta)
                if beta == 1234567:
                    bb = 'Infinity'
                elif beta == -1234567:
                    bb = '-Infinity'
                else:
                    bb = beta
                if(depth == game.depth):
                    text_file2.write("root"+","+str(int(game.depth) - int(depth))+","+str(low)+","+ str(aa)+","+ str(bb))
                else:
                    text_file2.write(getChar(l_index,r_index)+","+str(int(game.depth) - int(depth))+","+str(low)+","+ str(aa)+","+ str(bb))
                text_file2.write("\n")
    return low,l_index1,r_index1

def alphaBeta(game):
    evalsum,l_index,r_index = maximisealpha(game,game.player,8, 8,-1234567,1234567, game.depth)
    print "Eval and i and j",evalsum,l_index,r_index
    return

if __name__ == '__main__':
    game = board_game()
    text_file = open("read_it.txt", "r")
    lines = text_file.readlines()

    for line in lines:
        number_strings = line.split()
        numbers = [n for n in number_strings]
        game.matrix.append(numbers)
    print game.matrix
    game.depth = game.matrix[2][0]
    s = 0
    i = 0
    j = 0
    if game.matrix[0][0] == '4':
        for value in range(7, len(game.matrix)-5):
            game.matrix_val.append([])
            for v in range(len(game.matrix[value])):
                temp = game.matrix[value][v]
                t = int(temp)
                game.matrix_val[i].append(t)
                if s < t:
                    s = t
                j += 1
            i += 1
    else:
        for value in range(3, len(game.matrix)-5):
            game.matrix_val.append([])
            for v in range(len(game.matrix[value])):
                temp = game.matrix[value][v]
                t = int(temp)
                game.matrix_val[i].append(t)
                if s < t:
                    s = t
                j += 1
            i += 1
    j = 0
    for value in range(len(game.matrix)-5,len(game.matrix)):
        game.matrix_moves.append([])
        for v in range(len(game.matrix[value])):
            for x in range(len(game.matrix[value][v])):
                game.matrix_moves[j].append(game.matrix[value][v][x])
        j += 1
    print 'Values:'
    print game.matrix_val
    print 'Moves: '
    print game.matrix_moves
    if game.matrix[0][0] == '4':
        print 'v/s game'
        game = battleSimulation(game)
    if game.matrix[0][0] == '1':
        print 'Greedy play'
        GreedyBestFirst(game)
    elif game.matrix[0][0] == '2':
        text_file1 = open("traverse_log1.txt", "w")
        print 'MinMax play'
        minMaxAlgo(game)
    elif game.matrix[0][0] == '3':
        text_file2 = open("traverse_log2.txt", "w")
        text_file2.write("Node,Depth,Value,Alpha,Beta")
        text_file2.write("\n")
        print 'Alpha Beta'
        alphaBeta(game)
    text_file.close()
