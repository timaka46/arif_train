import time
import random
while True:
    sumtime=0
    right=0
    wrong=0
    num_mode=input('run with  basic number of digits(xxxxx * yyy / xxxxxx +- yyyyy +- zzzz +- dd) '
               '\nor change number of digits?\n"1" - default\n"2" - different number of digits\n"3" - same as it was before\n')
    if num_mode=="1":
        ndigits={'xmult' : 4,'ymult' : 3,'xadd' : 6,'yadd' : 5, 'zadd' : 4, 'dadd': 2}
    elif num_mode=='2':
        ndigits={'xmult' : 4,'ymult' : 3,'xadd' : 6,'yadd' : 5, 'zadd' : 4, 'dadd': 2}
        ndigits['xmult'] = int(input('number of "x" in multiplying - '))
        ndigits['ymult'] = int(input('number of "y" in multiplying - '))
        ndigits['xadd'] = int(input('number of "x" in add/sub - '))
        ndigits['yadd'] = int(input('number of "y" in add/sub - '))
        ndigits['zadd'] = int(input('number of "z" in add/sub - '))
        ndigits['dadd'] = int(input('number of "d" in add/sub - '))
    elif num_mode=="3":
        try:
            print(ndigits)
            continue
        except:
            ndigits = {'xmult': 4, 'ymult': 3, 'xadd': 6, 'yadd': 5, 'zadd': 4, 'dadd': 2}
    elif num_mode =="end":
        breakx

    game_mode=input('select mode:\n"1" - both multiplication and sum\n"2" - only multiplication\n"3" - only sum\n'
                    'You can also pause the game if you will write DURING the game "s" and by "g" continue it\n')
    if game_mode == "1":
        operators = ["+", "-", "*"]
    elif game_mode=="2":
        operators = ["*"]
    elif game_mode=="3":
        operators = ["+", "-"]
    end=False
    while end !=True:
        num1 = random.randint(1, 10**random.randint(2,ndigits['xmult']))
        num2 = random.randint(1, 10**random.randint(2,ndigits['ymult']))
        start=time.time()
        operator = random.choice(operators)

        print(f"What is {num1} {operator} {num2}?")

        answer = input()
        end=time.time()
        # Check if the answer is correct
        result = None
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2

        sumtime+=round(end - start, 2)
        if answer == str(result):
            print("Correct!")
            right+=1
        elif answer == "end":
            print("sum time -",round(sumtime,2),f"\nRight answers - {right}, Wrong answers - {wrong}, Total answers - {right+wrong}\n/\n/")
            break
        elif answer =="s":
            chk='no'
            while chk != 'g':
                chk=input("GAME PAUSED\n")
            end = 0
            start=0


        else:
            print("Incorrect. The correct answer is", result)
            wrong+=1
        print("Time -", round(end - start, 2),"seconds", "\n/\n/")
