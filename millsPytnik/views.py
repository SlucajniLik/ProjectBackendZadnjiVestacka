from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
## Vidi sta je ovo
import json 
from .mills import alphaBeta
from .pytnik import depth_first_search,brute_force_tsp,branch_and_bound,A_star
##Vidi sta je ovo
@csrf_exempt
  
def  search_coin(request):

    data=json.loads(request.body)
    agent=data['name']
    matrix=data['matrix']
    print(matrix)
    print(agent)

    if agent == "Aki":
        path=depth_first_search(matrix)
    elif agent == "Jocke":
        path=brute_force_tsp(matrix)
    elif agent == "Uki":
        path=branch_and_bound(matrix)
    elif agent == "Micko":
        path=A_star(matrix)



    return JsonResponse({'path': path})

   
    


@csrf_exempt
def playMills(request):
          
        

        
        board = json.loads(request.body)
        data=board['data']
        hardness = board['hardness']
        currentPlayer = board['currentPlayer']
        depth=0
        dificulty='easy'
        if hardness==1:
             dificulty='easy'
             depth=2
        elif hardness==2:
             dificulty='medium'
             depth=2
        elif hardness==3:
             dificulty='hard'
             depth=2
     
        
        score,_,move=alphaBeta(True,data,currentPlayer,0,depth,float('-inf'),float('inf'),dificulty,currentPlayer)
        print("Ovo je potez taj:    ",move)
        return JsonResponse({ 'move': move, 'score':score})


       