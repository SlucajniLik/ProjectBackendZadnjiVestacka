
import copy


###############################################

###########################################################################################Heuristics


def calculateMills(board,player):
           
           count=0
           for x in range(3):
             for y in [0, 2]:
              mill = 0
              for z in range(3):
                if board['pieces'][x][y][z]==player:
                 mill += board['pieces'][x][y][z]
              if mill==3*player:
                  count+=1
           



           
           for x in range(3):
             for y in [0, 2]:
              mill = 0
              for z in range(3):
                if board['pieces'][x][z][y]==player:
                 mill += board['pieces'][x][z][y]
              if mill==3*player:
                  count+=1
          
           mill = 0
           for x in range(3):
          
                if board['pieces'][x][0][1]==player:
                 mill += board['pieces'][x][0][1]
           if mill==3*player:
                  count+=1

           mill = 0
           for x in range(3):
          
                if board['pieces'][x][1][2]==player:
                 mill += board['pieces'][x][1][2]
           if mill==3*player:
                  count+=1

           mill = 0
           for x in range(3):
          
                if board['pieces'][x][2][1]==player:
                 mill += board['pieces'][x][2][1]
           if mill==3*player:
                  count+=1

           mill = 0
           for x in range(3):
          
                if board['pieces'][x][1][0]==player:
                 mill += board['pieces'][x][1][0]
           if mill==3*player:
                  count+=1



           return count




def countMills(board,move,player):
     
     x=move[0]
     y=move[1]
     z=move[2]
     num=[0,1,2]
     count=0

     if abs(sum(board['pieces'][x][y][i] for i in num))==3 and all(board['pieces'][x][y][i] ==player for i in num):
         count+=1
     
     if abs(sum(board['pieces'][x][i][z] for i in num))==3 and all(board['pieces'][x][i][z] ==player for i in num):
         count+=1
     
     if y==1 and z==0:
        if abs(sum(board['pieces'][i][y][z] for i in num))==3 and all(board['pieces'][i][y][z] ==player for i in num):
             count+=1

     if y==1 and z==2:
        if abs(sum(board['pieces'][i][y][z] for i in num))==3 and all(board['pieces'][i][y][z] ==player for i in num):
             count+=1  

     if y==0 and z==1:
        if abs(sum(board['pieces'][i][y][z] for i in num))==3 and all(board['pieces'][i][y][z] ==player for i in num):
             count+=1

     if y==2 and z==1:
        if abs(sum(board['pieces'][i][y][z] for i in num))==3 and all(board['pieces'][i][y][z] ==player for i in num):
             count+=1      


     if count==2:
       return True


     return False 



def calculateDoubleMills(board,player):
           
           count=0
           for x in range(3):
             for y in [0, 2]:
              mill = 0
              for z in range(3):
               #if y!=1 or z!=1:
                if board['pieces'][x][y][z]==player:
                 if countMills(board,(x,y,z),player)==True:
                      count+=1
              


               


           return count



def checkBlockedPiece(board,move,player):
     x=move[0]
     y=move[1]
     z=move[2]

     if y==0 and z==0:
       if board['pieces'][x][y][z]==player:
           if board['pieces'][x][y][z+1]==player*-1 and board['pieces'][x][y+1][z]==player*-1:
               return True
           
     if y==0 and z==2:
       if board['pieces'][x][y][z]==player:
           if board['pieces'][x][y][z-1]==player*-1 and board['pieces'][x][y+1][z]==player*-1:
               return True
           



     if y==2 and z==0:
       if board['pieces'][x][y][z]==player:
           if board['pieces'][x][y][z+1]==player*-1 and board['pieces'][x][y-1][z]==player*-1:
               return True
           
     if y==2 and z==2:
       if board['pieces'][x][y][z]==player:
           if board['pieces'][x][y][z-1]==player*-1 and board['pieces'][x][y-1][z]==player*-1:
               return True
           

     if x==0:
         if y==0 and z==1:
          if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y][z-1]==player*-1 and board['pieces'][x][y][z+1]==player*-1 and board['pieces'][x+1][y][z]==player*-1 :
               return True
            
         if y==2 and z==1:
           if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y][z-1]==player*-1 and board['pieces'][x][y][z+1]==player*-1 and board['pieces'][x+1][y][z]==player*-1 :
               return True
          


         if y==1 and z==2:
           if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y-1][z]==player*-1 and board['pieces'][x][y+1][z]==player*-1 and board['pieces'][x+1][y][z]==player*-1 :
               return True
            
         if y==1 and z==0:
           if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y-1][z]==player*-1 and board['pieces'][x][y+1][z]==player*-1 and board['pieces'][x+1][y][z]==player*-1 :
               return True



         
            



     if x==2:
         if y==0 and z==1:
          if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y][z-1]==player*-1 and board['pieces'][x][y][z+1]==player*-1 and board['pieces'][x-1][y][z]==player*-1 :
               return True
            
         if y==2 and z==1:
           if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y][z-1]==player*-1 and board['pieces'][x][y][z+1]==player*-1 and board['pieces'][x-1][y][z]==player*-1 :
               return True
          


         if y==1 and z==2:
           if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y-1][z]==player*-1 and board['pieces'][x][y+1][z]==player*-1 and board['pieces'][x-1][y][z]==player*-1 :
               return True
            
         if y==1 and z==0:
           if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y-1][z]==player*-1 and board['pieces'][x][y+1][z]==player*-1 and board['pieces'][x-1][y][z]==player*-1 :
               return True



         
            



     if x==1:
         if y==0 and z==1:
          if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y][z-1]==player*-1 and board['pieces'][x][y][z+1]==player*-1 and board['pieces'][x-1][y][z]==player*-1 and board['pieces'][x+1][y][z]==player*-1 :
               return True
            
         if y==2 and z==1:
           if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y][z-1]==player*-1 and board['pieces'][x][y][z+1]==player*-1 and board['pieces'][x-1][y][z]==player*-1 and board['pieces'][x+1][y][z]==player*-1:
               return True
          


         if y==1 and z==2:
           if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y-1][z]==player*-1 and board['pieces'][x][y+1][z]==player*-1 and board['pieces'][x-1][y][z]==player*-1 and board['pieces'][x+1][y][z]==player*-1 :
               return True
            
         if y==1 and z==0:
           if board['pieces'][x][y][z]==player:
            if board['pieces'][x][y-1][z]==player*-1 and board['pieces'][x][y+1][z]==player*-1 and board['pieces'][x-1][y][z]==player*-1 and board['pieces'][x+1][y][z]==player*-1:
               return True



         
         

def NumberBlockedPiece(board,player):
    


           count=0
           for x in range(3):
             for y in range(3):
              for z in range(3):
               if y!=1 or z!=1:
                if board['pieces'][x][y][z]==player:
                 if checkBlockedPiece(board,(x,y,z),player)==True:
                      count+=1
              


               


           return count 

def checkPossibleMills(board,move,player):
     
     x=move[0]
     y=move[1]
     z=move[2]
     num=[0,1,2]
     count=0

     if abs(sum(board['pieces'][x][y][i] for i in num))==2 and sum(board['pieces'][x][y][i] ==player for i in num)==2:
         return True
     
     if abs(sum(board['pieces'][x][i][z] for i in num))==2 and sum(board['pieces'][x][i][z] ==player for i in num)==2:
         return True
     
     if y==1 and z==0:
        if abs(sum(board['pieces'][i][y][z] for i in num))==2 and sum(board['pieces'][i][y][z] ==player for i in num)==2:
             return True

     if y==1 and z==2:
        if abs(sum(board['pieces'][i][y][z] for i in num))==2 and sum(board['pieces'][i][y][z] ==player for i in num)==2:
             return True  

     if y==0 and z==1:
        if abs(sum(board['pieces'][i][y][z] for i in num))==2 and sum(board['pieces'][i][y][z] ==player for i in num)==2:
             return True

     if y==2 and z==1:
        if abs(sum(board['pieces'][i][y][z] for i in num))==2 and sum(board['pieces'][i][y][z] ==player for i in num)==2:
             return True      


    
       


     return False 


def possibleMills(board,player):
    

           count=0
           for x in range(3):
             for y in range(3):
              for z in range(3):
               if y!=1 or z!=1:
                if board['pieces'][x][y][z]==0:
                 if checkPossibleMills(board,(x,y,z),player)==True:
                      count+=1
              


               


           return count 







#print("Broj millova: ",calculateMills(start_state,1))
#print("Broj duplih millova: ",calculateDoubleMills(start_state,1))



###############################################################################################







def playMove(board,move):
     

     pieces=copy.deepcopy(board)
     if move[0]=='set':
          player=move[1]
          x=move[2]
          y=move[3]
          z=move[4]
          pieces['pieces'][x][y][z]=player
          if player==1:
               pieces['countWhite']-=1
               pieces['onBoardWhite']+=1
          elif player==-1:
               pieces['countBlack']-=1
               pieces['onBoardBlack']+=1
     if move[0]=='move':
          player=move[1]
          x=move[2]
          y=move[3]
          z=move[4]
          fromx=move[5]
          fromy=move[6]
          fromz=move[7]
          pieces['pieces'][fromx][fromy][fromz]=0
          pieces['pieces'][x][y][z]=player
    
     if move[0]=='remove':
          player=move[1]
          x=move[2]
          y=move[3]
          z=move[4]
          pieces['pieces'][x][y][z]=0
          if player==1:
               pieces['onBoardBlack']-=1
               
          elif player==-1:
               pieces['onBoardWhite']-=1       
          
               
     return pieces




#print(playMove(start_state,('set',1,0,0,0)))
#print("Originalna",start_state)


def areLegalMoves(board,player):
                index1=0
                while  index1<len(board['pieces']):

                    index2=0
                    while  index2<len(board['pieces'][index1]):

                        index3=0
                        while index3<len(board['pieces'][index1][index2]):

                            #print('index3',index3,matrix['pieces'][index1][index2][index3])
                            
                            if index2 !=1 or index3!=1:
                                if board['pieces'][index1][index2][index3]==player:
                                     neighbors = allowedMovePosition(board,index1,index2,index3,1000,1000)
                                     #print('Broj',len(neighbors))
                                     if len(neighbors)>0:
                                      return True
                                
                                          
                            index3+=1
                        #print('index2',index2,matrix['pieces'][index1][index2])    
                        index2+=1  
                    index1+=1

                return False


def allowedMovePosition(board,fromIndex1,fromIndex2,fromIndex3,countPlayer,remainPlayer):
     positions=[]

     positions=[]
     if countPlayer==0 and remainPlayer==3:
                index1=0
                while  index1<len(board['pieces']):

                    index2=0
                    while  index2<len(board['pieces'][index1]):

                        index3=0
                        while index3<len(board['pieces'][index1][index2]):

                            #print('index3',index3,matrix['pieces'][index1][index2][index3])
                            
                            if index2 !=1 or index3!=1:
                                if board['pieces'][index1][index2][index3]==0:
                                     positions.append((index1,index2,index3))
                                     
                                          
                            index3+=1
                        #print('index2',index2,matrix['pieces'][index1][index2])    
                        index2+=1  
                    index1+=1
                return positions














     if fromIndex2!=1:

       if fromIndex3-1>=0 and board['pieces'][fromIndex1][fromIndex2][fromIndex3-1]==0:
            positions.append((fromIndex1,fromIndex2,fromIndex3-1))
          
       if fromIndex3+1<=2 and board['pieces'][fromIndex1][fromIndex2][fromIndex3+1]==0:
            positions.append((fromIndex1,fromIndex2,fromIndex3+1))

     if fromIndex3!=1:

       if fromIndex2-1>=0 and board['pieces'][fromIndex1][fromIndex2-1][fromIndex3]==0:
            positions.append((fromIndex1,fromIndex2-1,fromIndex3))
          
       if fromIndex2+1<=2 and board['pieces'][fromIndex1][fromIndex2+1][fromIndex3]==0:
            positions.append((fromIndex1,fromIndex2+1,fromIndex3))




     if fromIndex2==1:
        if fromIndex1==0 and board['pieces'][fromIndex1+1][fromIndex2][fromIndex3]==0:
                positions.append((fromIndex1+1,fromIndex2,fromIndex3))

     if fromIndex2==1:
        if fromIndex1==2 and board['pieces'][fromIndex1-1][fromIndex2][fromIndex3]==0:
                positions.append((fromIndex1-1,fromIndex2,fromIndex3))

     if fromIndex2==1:
        if fromIndex1==1 and board['pieces'][fromIndex1+1][fromIndex2][fromIndex3]==0:
             positions.append((fromIndex1+1,fromIndex2,fromIndex3))

     if fromIndex2==1:
        if fromIndex1==1 and board['pieces'][fromIndex1-1][fromIndex2][fromIndex3]==0:
                positions.append((fromIndex1-1,fromIndex2,fromIndex3))

     if fromIndex3==1:
        if fromIndex1==0 and board['pieces'][fromIndex1+1][fromIndex2][fromIndex3]==0:
             positions.append((fromIndex1+1,fromIndex2,fromIndex3))

     if fromIndex3==1:
        if fromIndex1==2 and board['pieces'][fromIndex1-1][fromIndex2][fromIndex3]==0:
                positions.append((fromIndex1-1,fromIndex2,fromIndex3))

     if fromIndex3==1:
        if fromIndex1==1 and board['pieces'][fromIndex1+1][fromIndex2][fromIndex3]==0:
             positions.append((fromIndex1+1,fromIndex2,fromIndex3))

     if fromIndex3==1:
        if fromIndex1==1 and board['pieces'][fromIndex1-1][fromIndex2][fromIndex3]==0:
                positions.append((fromIndex1-1,fromIndex2,fromIndex3))


     return positions            

     
     
      
    

















          
def isMills(board,move):
     
     x=move[2]
     y=move[3]
     z=move[4]
     num=[0,1,2]
          
     if abs(sum(board['pieces'][x][y][i] for i in num))==3:
         return True
     
     if abs(sum(board['pieces'][x][i][z] for i in num))==3:
         return True
     
     if y==1 and z==0:
        if abs(sum(board['pieces'][i][y][z] for i in num))==3:
             return True

     if y==1 and z==2:
        if abs(sum(board['pieces'][i][y][z] for i in num))==3:
             return True  

     if y==0 and z==1:
        if abs(sum(board['pieces'][i][y][z] for i in num))==3:
             return True

     if y==2 and z==1:
        if abs(sum(board['pieces'][i][y][z] for i in num))==3:
             return True      

     return False


#print(isMills(start_state,('set',1,0,1,2)))

def isNonMills(board,pl):
                index1=0
                while  index1<len(board['pieces']):

                    index2=0
                    while  index2<len(board['pieces'][index1]):

                        index3=0
                        while index3<len(board['pieces'][index1][index2]):

                            #print('index3',index3,matrix['pieces'][index1][index2][index3])
                            
                            if index2 !=1 or index3!=1:
                                if board['pieces'][index1][index2][index3]==pl :
                                    if isMills(board,('non',0,index1,index2,index3))==False:
                                         return False
                                          
                            index3+=1
                        #print('index2',index2,matrix['pieces'][index1][index2])    
                        index2+=1  
                    index1+=1
     
          
                return True


def removePiece(board,ListBoard,player,moves,move1):
                pl=player*-1
                index1=0
                while  index1<len(board['pieces']):

                    index2=0
                    while  index2<len(board['pieces'][index1]):

                        index3=0
                        while index3<len(board['pieces'][index1][index2]):

                            #print('index3',index3,matrix['pieces'][index1][index2][index3])
                            if index2 !=1 or index3!=1:
                             if board['pieces'][index1][index2][index3]==pl:
                                     if isNonMills(board,pl)==True:
                                          move=('remove',player,index1,index2,index3)
                                          boardd=playMove(board,move)
                                          ListBoard.append(boardd)
                                          moves.append([move1,move])
                                     elif isMills(board,('remove',player,index1,index2,index3))==False:
                                       move=('remove',player,index1,index2,index3)
                                       boardd=playMove(board,move)
                                       ListBoard.append(boardd)
                                       moves.append([move1,move])

                                          
                            index3+=1
                        #print('index2',index2,matrix['pieces'][index1][index2])    
                        index2+=1  
                    index1+=1
                    
                return ListBoard,moves 






def getMoves(board,player):
   
    moves = []
    ListBoard=[]
    countPlayer=0
    if player==1:
         countPlayer=board['countWhite']
    elif player==-1:
         countPlayer=board['countBlack']
   
    if countPlayer>0:
                

                index1=0
                while  index1<len(board['pieces']):

                    index2=0
                    while  index2<len(board['pieces'][index1]):

                        index3=0
                        while index3<len(board['pieces'][index1][index2]):

                            #print('index3',index3,matrix['pieces'][index1][index2][index3])
                            
                            if index2 !=1 or index3!=1:
                                if board['pieces'][index1][index2][index3]==0:
                                     
                                     move=('set',player,index1,index2,index3)
                                     boardd=playMove(board,move)
                                     if isMills(boardd,move):
                                          ListBoard,moves=removePiece(boardd,ListBoard,player,moves,move)
                                          
                                     else:
                                         ListBoard.append(boardd)
                                         moves.append([move])

                                     #print('indEX SET',('set',player,index1,index2,index3))   
                            index3+=1
                        #print('index2',index2,matrix['pieces'][index1][index2])    
                        index2+=1  
                    index1+=1
                    
                return ListBoard, moves




  
         
              
         
    if countPlayer==0:
                countPlayer=''
                remainPlayer=''
                if player==1:
                     countPlayer=board['countWhite']
                     remainPlayer=board['onBoardWhite']
                elif player==-1:
                     countPlayer=board['countBlack']
                     remainPlayer=board['onBoardBlack']
                     

                index1=0
                while  index1<len(board['pieces']):

                    index2=0
                    while  index2<len(board['pieces'][index1]):

                        index3=0
                        while index3<len(board['pieces'][index1][index2]):

                            #print('index3',index3,matrix['pieces'][index1][index2][index3])
                            
                            if index2 !=1 or index3!=1:
                                if board['pieces'][index1][index2][index3]==player:
                                     
                                     indexPositions=0
                                     neighbors = allowedMovePosition(board,index1,index2,index3,countPlayer,remainPlayer)
                                     while indexPositions<len(neighbors):
                                          toIndex1,toIndex2,toIndex3 = neighbors[indexPositions]
                                          if board['pieces'][toIndex1][toIndex2][toIndex3]==0:
                                            move=('move',player,toIndex1,toIndex2,toIndex3,index1,index2,index3)
                                            boardd=playMove(board,move)
                                            if isMills(boardd,move):
                                             ListBoard,moves=removePiece(boardd,ListBoard,player,moves,move)
                                             
                                            else:
                                             ListBoard.append(boardd)
                                             moves.append([move])
                                          indexPositions+=1       
                            index3+=1
                        #print('index2',index2,matrix['pieces'][index1][index2])    
                        index2+=1  
                    index1+=1
                    
                return ListBoard, moves
    
    
    return ListBoard, moves


 
#for board,move in zip(getMoves(start_state,1)[0],getMoves(start_state,1)[1]):
    
   
    #print(board,"Moveee",move)

    
    






def gameOver(board,player):
     
    
     legalMovesPlayerOne=len(getMoves(board,1)[0])
     legalMovesPlayerTwo=len(getMoves(board,-1)[0])
    
    
     if (board['onBoardWhite']==2 and board['countWhite']==0) or legalMovesPlayerOne==0:
          
          return True
     if (board['onBoardBlack']==2 and board['countBlack']==0) or legalMovesPlayerTwo==0 :
          
          return True
     
     ####PROVERAAA

     

    
def evaluate(board,originalPlayer,type):
  evaluation=0
  legalMovesPlayerOne=len(getMoves(board,originalPlayer)[0])
  legalMovesPlayerTwo=len(getMoves(board,originalPlayer*-1)[0])




  blockedBlack=NumberBlockedPiece(board,originalPlayer)
  blockedWhite=NumberBlockedPiece(board,originalPlayer*-1)
  nuumMillDoubleBlack=calculateMills(board,originalPlayer)
  nuumMillDoubleWhite=calculateMills(board,originalPlayer*-1)
  possibleMillBlack=possibleMills(board,originalPlayer)
  possibleMillWhite=possibleMills(board,originalPlayer*-1)
  nuumMillBlack=calculateMills(board,originalPlayer)
  nuumMillWhite=calculateMills(board,originalPlayer*-1)
  if originalPlayer==-1:
            firstBoard=board['onBoardBlack']
            secondBoard=board['onBoardWhite']
            firstCount=board['onBoardWhite']
            secondCount=board['onBoardBlack']
            currentBoard=board['onBoardBlack']
           
  elif originalPlayer==1:
            firstBoard=board['onBoardWhite']
            secondBoard=board['onBoardBlack']
            firstCount=board['onBoardBlack']
            secondCount=board['onBoardWhite']
            currentBoard=board['onBoardWhite']

  if type=='easy':
    
    if board['countWhite']==0 and board['countBlack']==0:
        
       

        if firstCount==2 or legalMovesPlayerTwo==0:
            evaluation=9999999
        elif secondCount==2  or legalMovesPlayerOne==0:    
            evaluation=-9999999
        else:
             evaluation=240*(firstBoard-secondBoard)
       
    else:
        evaluation=140*(firstBoard-secondBoard)
       




  if type=='medium':
    
    if board['countWhite']==0 and board['countBlack']==0:
        
       
        if firstCount==2  or legalMovesPlayerTwo==0:      
            evaluation=9999999
        elif secondCount==2 or legalMovesPlayerOne==0:
            evaluation=-9999999
        else:
             if currentBoard<=3:
                 evaluation+=100*(firstBoard-secondBoard)
                
             elif currentBoard>3:
                evaluation=140*(possibleMillBlack-possibleMillWhite)
                evaluation+=100*(firstBoard-secondBoard)
                 
                 
                 
    else: 
     evaluation=100*(possibleMillBlack-possibleMillWhite)
     evaluation+=140*(firstBoard-secondBoard)
     
     




  if type=='hard':
    
    
    if board['countWhite']==0 and board['countBlack']==0:
       
        if firstCount==2  or legalMovesPlayerTwo==0:   
            evaluation=9999999
        elif secondCount==2 or legalMovesPlayerOne==0:
            evaluation=-9999999
        else:
            
             if currentBoard<=3:
                evaluation=150*(possibleMillBlack-possibleMillWhite)
                evaluation+=30*(firstBoard-secondBoard)
             elif currentBoard>3:
               evaluation=100*(possibleMillBlack-possibleMillWhite)
               evaluation+=150*(nuumMillBlack-nuumMillWhite)
               evaluation+=140*(firstBoard-secondBoard)
               evaluation+=60*(nuumMillDoubleBlack-nuumMillDoubleWhite)
               evaluation+=20*(blockedWhite-blockedBlack)
                 
                 
                 
    else: 
     evaluation=100*(possibleMillBlack-possibleMillWhite)
     evaluation+=150*(nuumMillBlack-nuumMillWhite)
     evaluation+=140*(firstBoard-secondBoard)
     evaluation+=60*(nuumMillDoubleBlack-nuumMillDoubleWhite)
     evaluation+=20*(blockedWhite-blockedBlack)
     
           
  return evaluation


"""  
def evaluate(board,originalPlayer,type):
  evaluation=0
  legalMovesPlayerOne=len(getMoves(board,originalPlayer)[0])
  legalMovesPlayerTwo=len(getMoves(board,originalPlayer*-1)[0])

  if originalPlayer==-1:
            firstBoard=board['onBoardBlack']
            secondBoard=board['onBoardWhite']
            firstCount=board['onBoardWhite']
            secondCount=board['onBoardBlack']
            currentBoard=board['onBoardBlack']
           
  elif originalPlayer==1:
            firstBoard=board['onBoardWhite']
            secondBoard=board['onBoardBlack']
            firstCount=board['onBoardBlack']
            secondCount=board['onBoardWhite']
            currentBoard=board['onBoardWhite']

  if type=='easy':
    
    if board['countWhite']==0 and board['countBlack']==0:
        
       

        if firstCount==2 or legalMovesPlayerTwo==0:
            evaluation=9999999
        elif secondCount==2  or legalMovesPlayerOne==0:    
            evaluation=-9999999
        else:
             evaluation=200*(firstBoard-secondBoard)
       
    else:
        evaluation=100*(firstBoard-secondBoard)
       




  if type=='medium':
    possibleMillBlack=possibleMills(board,originalPlayer)
    possibleMillWhite=possibleMills(board,originalPlayer*-1)
    nuumMillBlack=calculateMills(board,originalPlayer)
    nuumMillWhite=calculateMills(board,originalPlayer*-1)
    if board['countWhite']==0 and board['countBlack']==0:
        
       
        if firstCount==2  or legalMovesPlayerTwo==0:      
            evaluation=9999999
        elif secondCount==2 or legalMovesPlayerOne==0:
            evaluation=-9999999
        else:
             if currentBoard<=3:
                evaluation=100*(possibleMillBlack-possibleMillWhite)
                evaluation+=200*(nuumMillBlack-nuumMillWhite)
             elif currentBoard>3:
               evaluation=100*(possibleMillBlack-possibleMillWhite)
               evaluation+=200*(nuumMillBlack-nuumMillWhite)
               evaluation+=50*(firstBoard-secondBoard)
                 
                 
                 
    else: 
     evaluation=100*(possibleMillBlack-possibleMillWhite)
     evaluation+=150*(nuumMillBlack-nuumMillWhite)
     evaluation+=200*(firstBoard-secondBoard)




  if type=='hard':
    blockedBlack=NumberBlockedPiece(board,originalPlayer)
    blockedWhite=NumberBlockedPiece(board,originalPlayer*-1)
    nuumMillDoubleBlack=calculateMills(board,originalPlayer)
    nuumMillDoubleWhite=calculateMills(board,originalPlayer*-1)
    possibleMillBlack=possibleMills(board,originalPlayer)
    possibleMillWhite=possibleMills(board,originalPlayer*-1)
    nuumMillBlack=calculateMills(board,originalPlayer)
    nuumMillWhite=calculateMills(board,originalPlayer*-1)
    
    if board['countWhite']==0 and board['countBlack']==0:
       
        if firstCount==2  or legalMovesPlayerTwo==0:   
            evaluation=9999999
        elif secondCount==2 or legalMovesPlayerOne==0:
            evaluation=-9999999
        else:
            
             if currentBoard<=3:
                evaluation=150*(possibleMillBlack-possibleMillWhite)
                evaluation+=200*(nuumMillBlack-nuumMillWhite)
                evaluation+=30*(firstBoard-secondBoard)
             elif currentBoard>3:
               evaluation=100*(possibleMillBlack-possibleMillWhite)
               evaluation+=180*(nuumMillBlack-nuumMillWhite)
               evaluation+=50*(firstBoard-secondBoard)
               evaluation+=250*(nuumMillDoubleBlack-nuumMillDoubleWhite)
               evaluation+=20*(blockedWhite-blockedBlack)
                 
                 
                 
    else: 
     evaluation=100*(possibleMillBlack-possibleMillWhite)
     evaluation+=150*(nuumMillBlack-nuumMillWhite)
     evaluation+=200*(firstBoard-secondBoard)
     evaluation+=180*(nuumMillDoubleBlack-nuumMillDoubleWhite)
     evaluation+=30*(blockedWhite-blockedBlack)
     
           
  return evaluation
"""
 









    







#print('pogledaj ovde',evaluate(start_state,-1,'medium'))
#print("Broj blokiranih : ",NumberBlockedPiece(start_state,1) )
#print('Broj mogucih millsova: ',possibleMills(start_state,1))










def alphaBeta(pl,board,current,depth,maxDepth,alpha,beta,dificulty,originalPlayer):
        
           

 

         if depth==maxDepth or gameOver(board,current):
          print(dificulty,evaluate(board,originalPlayer,dificulty))
          return evaluate(board,originalPlayer,dificulty),None,None
          #return current,None,None
         next=current*-1
         bestBoard1=None
         bestMove=None
         if pl==True:
              bestScore=float('-inf')
              result1, result2 = getMoves(board,current)
              for board1,move in zip(result1, result2):
                   print(board1,"player: ",current," depth : ",depth,"Move: ",move)
                   currentScore=alphaBeta(False,board1,next,depth+1,maxDepth,alpha,beta,dificulty,originalPlayer)[0]
                   print('currentScore : ',currentScore,"  MaxBestScore  : ",bestScore )
                   if currentScore>bestScore:
                      bestScore=currentScore      
                      print("Postavljen  MaxBestScore  : ",bestScore )         
                      bestBoard1=board1
                      bestMove=move
                   #alpha = max(alpha, currentScore)
                   alpha = max(alpha, bestScore)
                    
                   if alpha>=beta:
                    print("alpha: ",alpha," beta: ",beta)
                    break
                   

              return bestScore,bestBoard1,bestMove
              
         elif pl==False:
              bestScore=float('inf')
              result1, result2 = getMoves(board,current)
              for board1,move in zip(result1,result2):
                   print(board1,"player: ",current," depth : ",depth," Move : ",move)

                   
                   currentScore=alphaBeta(True,board1,next,depth+1,maxDepth,alpha,beta,dificulty,originalPlayer)[0]
                   print('currentScore : ',currentScore,"  MinBestScore  : ",bestScore )
                   if currentScore<bestScore:
                      bestScore=currentScore   
                      print("Postavljen  MinBestScore  : ",bestScore )             
                      bestBoard1=board1
                      bestMove=move
                   beta = min(beta, bestScore)
                   #beta = min(beta, currentScore)
                   if alpha>=beta:
                      print("alpha: ",alpha," beta: ",beta)
                      break
                   
              return bestScore,bestBoard1,bestMove




#print(len(getMoves(start_state,-1)[0]))
#print("OVDE:  ",alphaBeta(True,start_statee,-1,0,3,float('-inf'),float('inf'),'hard',-1)[2])
#print(" Min : ",minimax(start_state,1,0,2,False))
    
    
#print("Evaluacija:   ",evaluate(start_statee,-1,'hard'))
print("Hostovan")