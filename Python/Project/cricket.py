import random

team = """
        SELECT YOUR TEAM

        1) GT  2) MI  3) CSK  4) RR  5) LSG
        6) KKR  7) K11P  8) DC  9) SRH  10) RCB

"""

print(team)
team_list = ['GT', 'MI', 'CSK', 'RR', 'LSG', 'KKR', 'K11P', 'DC', 'SRH', 'RCB']
toss_list = ["HEAD", "TAILS"]
decision = ["BAT", "BALL"]
run = ["1","2","3","4","6","NO BALL","WICKET","WIDE BALL"]
status = True
c_score = 0
y_score = 0
c_wickets = 0
y_wickets = 0


while status:
    your_team = input("Select your team: ").upper()
    print("..................................\n")
    print(f"Your team : {your_team}")
    if your_team not in team_list:
        print("Invalid team selection. Please choose from the available options.")
        continue

    team_list.remove(your_team)
    computer_team = random.choice(team_list)
    print(f"Computer team : {computer_team}")
    print("..................................\n")

    print("Toss Time !!!")
    toss = random.choice(toss_list)
    u_toss = input("HEAD or TAIL: ").upper()

    if u_toss not in toss_list:
        print("Invalid toss selection. Please choose HEADS or TAILS.")
        continue

    print(u_toss)
    print("..................................\n")

    if toss == u_toss:
        print("You won the toss!")
        toss_choice = input("Press 1 to bat and 2 to bowl: ")

        if toss_choice == "1":
            print("You selected to bat first!")
            print("...................................\n")
            print(your_team,"Bating Started.")
            i = 1
            while i < 7 :
                input()
                auto_ball = random.choice(run)
                print(f"{i} ball {auto_ball}")

                if auto_ball == "NO BALL":
                    y_score += 1
                    print("NO BALL")
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i-1)
                elif auto_ball == "WICKET":
                    y_wickets += 1
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i)
                    i += 1
                elif y_wickets == 2:
                    print("ALL OUT !!!")
                    break
                elif auto_ball == "WIDE BALL":
                    y_score += 1
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i-1)
                    print("WIDE BALL")
                else:
                    y_score += int(auto_ball)
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i)
                    i+=1
            print("\n==============================================")
            print(your_team,"Final Score is : ",y_score,"/",y_wickets," Overs :","1.0")
            print("==============================================")

            print(computer_team,"Bating Started.")
            i = 1
            while i < 7 :
                input()
                auto_ball = random.choice(run)
                print(f"{i} ball {auto_ball}")

                if auto_ball == "NO BALL":
                    c_score += 1
                    print("NO BALL")
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i-1)
                elif auto_ball == "WICKET":
                    c_wickets += 1
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i)
                    i += 1
                elif c_wickets == 2:
                    print("ALL OUT !!!")
                    break
                elif auto_ball == "WIDE BALL":
                    c_score += 1
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i-1)
                    c_wickets += 0
                else:
                    c_score += int(auto_ball)
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i)
                    i += 1
            print("\n================================================")
            print(computer_team,"Final Score is : ",c_score,"/",c_wickets," Overs :","1.0")
            print("================================================\n")

        elif toss_choice == "2":
            print("You selected to bowl first!")
            print("...................................\n")
            print(computer_team,"Bating Started.")
            i = 1
            while i < 7 :
                input()
                auto_ball = random.choice(run)
                print(f"{i} ball {auto_ball}")

                if auto_ball == "NO BALL":
                    c_score += 1
                    print("NO BALL")
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i-1)
                elif auto_ball == "WICKET":
                    c_wickets += 1
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i)
                    i += 1
                elif c_wickets == 2:
                    print("ALL OUT !!!")
                    break
                elif auto_ball == "WIDE BALL":
                    c_score += 1
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i-1)
                    c_wickets += 0
                else:
                    c_score += int(auto_ball)
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i)
                    i += 1
            print("\n================================================")
            print(computer_team,"Final Score is : ",c_score,"/",c_wickets," Overs :","1.0")
            print("================================================\n")

            print(your_team,"Bating Started.")
            i = 1
            while i < 7 :
                input()
                auto_ball = random.choice(run)
                print(f"{i} ball {auto_ball}")

                if auto_ball == "NO BALL":
                    y_score += 1
                    print("NO BALL")
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i-1)
                elif auto_ball == "WICKET":
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i)
                    y_wickets += 1
                    i += 1
                elif auto_ball == "WIDE BALL":
                    y_score += 1
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i-1)
                    print("WIDE BALL")
                elif y_wickets == 2:
                    print("ALL OUT !!!")
                    break
                else:
                    y_score += int(auto_ball)
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i)
                    i+=1
            print("\n==============================================")
            print(your_team,"Final Score is : ",y_score,"/",y_wickets," Overs :","1.0")
            print("==============================================")

        else:
            print("Invalid choice. Please enter 1 or 2.")

    elif toss != u_toss:
        c_decision = random.choice(decision)
        print(f"Computer won the toss and selected to {c_decision}!\n")
        if c_decision == "BAT" :
            print(computer_team,"Bating Started.")
            i = 1
            while i < 7 :
                input()
                auto_ball = random.choice(run)
                print(f"{i} ball {auto_ball}")

                if auto_ball == "NO BALL":
                    c_score += 1
                    print("NO BALL")
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i-1)
                elif auto_ball == "WICKET":
                    c_wickets += 1
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i)
                    i += 1
                elif auto_ball == "WIDE BALL":
                    c_score += 1
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i-1)
                    c_wickets += 0
                elif c_wickets == 2:
                    print("ALL OUT !!!")
                    break
                else:
                    c_score += int(auto_ball)
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i)
                    i += 1
            print("\n================================================")
            print(computer_team,"Final Score is : ",c_score,"/",c_wickets," Overs :","1.0")
            print("================================================\n")
                        
            print(your_team,"Bating Started.")
            i = 1
            while i < 7 :
                input()
                auto_ball = random.choice(run)
                print(f"{i} ball {auto_ball}")

                if auto_ball == "NO BALL":
                    y_score += 1
                    print("NO BALL")
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i-1)
                elif auto_ball == "WICKET":
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i)
                    y_wickets += 1
                    i += 1
                elif auto_ball == "WIDE BALL":
                    y_score += 1
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i-1)
                    print("WIDE BALL")
                elif y_wickets == 2:
                    print("ALL OUT !!!")
                    break
                else:
                    y_score += int(auto_ball)
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i)
                    i+=1
            print("\n==============================================")
            print(your_team,"Final Score is : ",y_score,"/",y_wickets," Overs :","1.0")
            print("==============================================")

        else:
            print(your_team,"Bating Started.")
            i = 1
            while i < 7 :
                input()
                auto_ball = random.choice(run)
                print(f"{i} ball {auto_ball}")

                if auto_ball == "NO BALL":
                    y_score += 1
                    print("NO BALL")
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i-1)
                elif auto_ball == "WICKET":
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i)
                    y_wickets += 1
                    i += 1
                elif auto_ball == "WIDE BALL":
                    y_score += 1
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i-1)
                    print("WIDE BALL")
                elif y_wickets == 2:
                    print("ALL OUT !!!")
                    break
                else:
                    y_score += int(auto_ball)
                    print(your_team,":", y_score, "/",y_wickets," Overs :","0.",i)
                    i+=1
            print("\n==============================================")
            print(your_team,"Final Score is : ",y_score,"/",y_wickets," Overs :","1.0")
            print("==============================================")

            print(computer_team,"Bating Started.")
            i = 1
            while i < 7 :
                input()
                auto_ball = random.choice(run)
                print(f"{i} ball {auto_ball}")

                if auto_ball == "NO BALL":
                    c_score += 1
                    print("NO BALL")
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i-1)
                elif auto_ball == "WICKET":
                    c_wickets += 1
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i)
                    i += 1
                elif auto_ball == "WIDE BALL":
                    c_score += 1
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i-1)
                    c_wickets += 0
                elif c_wickets == 2:
                    print("ALL OUT !!!")
                    break
                else:
                    c_score += int(auto_ball)
                    print(computer_team,":", c_score, "/",c_wickets," Overs :","0.",i)
                    i += 1
            print("\n================================================")
            print(computer_team,"Final Score is : ",c_score,"/",c_wickets," Overs :","1.0")
            print("================================================\n")

    print("---------------- Final Result ----------------\n")
    print(your_team,"Final Score is : ",y_score,"/",y_wickets," Overs :","1.0")
    print(computer_team,"Final Score is : ",c_score,"/",c_wickets," Overs :","1.0")

    if your_team > computer_team:
        print("\nYOU WON THE MATCH !!!!\n")
    else:
        print("\nCOMPUTER WON THE MATCH !!!!\n")
                    
    choice = input("Want to play again? Enter Y for Yes, N for No: ")
    if choice.lower() == "n":
        status = False
