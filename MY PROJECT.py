print ("=====================================")

print ("WELLCOME TO M.K COMPUTER QUIZ GAME !")

print ("=====================================")
while True:
   playing = input("Do you want to play? ")
   if playing . lower() == "yes":
    print("Okay! Let's Play :")
   else:
     break
   print ("==================================")
   score = 0
   print("1. What does CPU Stands For? ")
   answer=str(input('Answer =  '))
   if answer . lower() == "central processing unit":
            print ('Correct!')
            score += 1
   else:
          print ("In Correct!")
   print("2. What does GPU Stands For? ")
   answer=str(input('Answer =  '))
   if answer. lower() == "graphics processing unit":
          print ('Correct!' )
          score += 1
   else:
           print ("In Correct !")
   print("3. What does PEMDAS Stands For? ")
   answer=str(input('Answer =  '))
   if answer . lower() == "power expression multiplication divison addition subtraction":
            print ('In correct!' )
            score += 1
            print ("Correct !")
   else:
            print ("In Correct")
   print("4. What does RAM Stands For? ")
   answer=str(input('Answer =  '))
   if answer . lower() == "random access memory":
            print ('Correct!' )
            score += 1
   else:
            print ("In Correct !")
   print("5. what does HTTP stands for? ")
   answer=str(input('Answer =  '))
   if answer . lower() == "hyper text transfer protocol":
            print ('Correct!' )
            score += 1
   else:
            print ("In Correct !")
   print("6. what does URL stands for? ")
   answer=str(input('Answer =  '))
   if answer . lower() == "uniform resources locator":
            print ('Correct!' )
            score += 1
   else:
            print ("In Correct !")
   print("7. What does MAN Stands For? ")
   answer=str(input('Answer =  '))
   if answer . lower() == "metropolitan area network ":
            print ('Correct!' )
            score += 1
   else:
            print ("In Correct !")
   print("8. What does WWW Stands For? ")
   answer=str(input('Answer =  '))
   if answer . lower() == "world wide web":
            print ('Correct!' )
            score += 1
   else:
            print ("In Correct !")
   print("9. What does LCD Stands For? ")
   answer=str(input('Answer =  '))
   if answer . lower() == "liquid crystal display":
            print ('Correct!' )
            score += 1
   else:
            print ("In Correct !")
   print("10. What does OS Stands For? ")
   answer=str(input('Answer =  '))
   if answer . lower() == "operating system":
               print ('Correct!' )
               score += 1
   else:
               print ("In Correct !")
   print ("You got " + str(score) + " questions correct!")
   print ("You got " + str((score/ 10) * 100) + "%.")
   if score <=5:
               print("Sorry ! Poor Result please try again")
               repeat = input("Do you want to repeat the program? (yes/no):"). lower()
               if repeat != "yes":
                  quit()
               else:
                  print("Keep Up! The Amazing work You Are Truly Impressive")
   
 

9
