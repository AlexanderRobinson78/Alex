#Hi my name is Alex Robinson
#Welcome to my Video Game Quiz
#It is super simple but I think I have made it full proof
#Even if it might loop forever if you couldn't figure it out
#The 2 quizzes range from beginner to expert
#Both based on the knowledge of video games and video game companies
#From Sony to Nintendo
#I hope you enjoy it!

#This comment function for the beginning of the program
#When called (it is only called once) it will print out introduction sentences
def beginning_comments():
                print("Hello! Welcome to my quiz program!")
                print("The quiz program is based on the history of video games.")
                print("Ranging from Nintendo to Sony, it will test your knowledge on video games!")
                print("There are two quizes, ranging from: beginnner to expert.")
                print("You must pass the previous exam to go to the next one,")
                print("to pass you have to get all of them correct.""\n")
#This answer function when called will list out all the answers for the questions
#Using a for loop it will take the answers from one of the lists
#They are numbered and will tell you will test they are from
#This is only called at the very end and is only called once
def answer_list():
                t1_list=["Link", "Playstation One", "Halo", "Luigi", "Playstation Two"]
                print("Test 1 list of answers:","\n")
                for i in t1_list:
                                print(t1_list.index(i) +1, ")" ,sep='', end=' ')
                                print(" ",i)
                t2_list=["Super Mushroom","Solid Snake", "Buster Sword", "2003", "Minecraft"]
                print("\n")
                print("Test 2 list of answers:","\n")
                for n in t2_list:
                                print(t2_list.index(n) +1, ")" ,sep='', end=' ')
                                print(" ",n)
                print("\n")

#Here is the main funtion code, this where everything is called and produced
def main():
#This is the comments function being called
                beginning_comments()
                x=True
#This while loop asks you if you want to start the first test
#By typing start you will begin
#But anything other than that will result in you repeating until you get it right
                while x==True:
                                start_1=str(input("Type 'start' or 'Start' to begin the first quiz!: ""\n"))
                                if start_1=='start' or start_1=='Start':
                                                print("Begin!""\n")
                                                x=False
                                                beginner_test=True
                                else:
                                                print("ERROR, you did not input 'start', try again.""\n")

#This is all the code for the first test,
#it contains 5 questions and 4 answers for each,
#and if you get it wrong or right it will count it in a variable

#It will ask you for an input from a to d, input what you think is correct,
#after each input it will say if it is correct or incorrect,
#then it will go onto the next question
                if beginner_test==True:
                                print("Make sure to type the letter of the answer not the actual answer.")
                                print("An example would be A or d""\n")
                                test_1='start'
#This while loop contains the entire first test, all the questions, answers, and ending comments
#The while loop will continue to loop until you have passed the test
                                while test_1=='start':
                                                total_correct_t1=0
                                                total_incorrect_t1=0

                                                print("Question 1: Who is the main character in the series Legend of Zelda?")
                                                print("(A) Mario")
                                                print("(B) Zelda")
                                                print("(C) Ganon")
                                                print("(D) Link")
#Each question has very similar code, that is pretty much copy and paste

#Each question has 4 answers: A, B, C, or D
#Only one is right and you input it by chosing the letter of the one you think is correct
#5 questions per quiz
#Each question code has totalCorrect and totalIncorrect variables,
#if either one is met it will add one value to it
                                                T1Q1=str(input("Choose an answer: ""\n"))
                                                if T1Q1=='d' or T1Q1=='D':
                                                                total_correct_t1+=1
                                                                print("Correct!""\n")
                                                else:
                                                                total_incorrect_t1+=1
                                                                print("Incorrect!""\n")

                                                print("Question 2: What is the name of sony's first console?")
                                                print("(A) NES")
                                                print("(B) Playstation One")
                                                print("(C) Gamecube")
                                                print("(D) Atari 2600")

                                                T1Q2=str(input("Choose an answer: ""\n"))
                                                if T1Q2=='b' or T1Q2=='B':
                                                                total_correct_t1+=1
                                                                print("Correct!""\n")
                                                else:
                                                                total_incorrect_t1+=1
                                                                print("Incorrect!""\n")

                                                print("Question 3: What is Xbox's most popular series?")
                                                print("(A) Mario Bros")
                                                print("(B) Halo")
                                                print("(C) Uncharted")
                                                print("(D) Tetris")

                                                T1Q3=str(input("Choose an answer: ""\n"))
                                                if T1Q3=='b' or T1Q3=='B':
                                                                total_correct_t1+=1
                                                                print("Correct!""\n")
                                                else:
                                                                total_incorrect_t1+=1
                                                                print("Incorrect!""\n")

                                                print("Question 4: What is the name of Mario's brother?")
                                                print("(A) Luigi")
                                                print("(B) Nathan")
                                                print("(C) Billy")
                                                print("(D) Donkey Kong")

                                                T1Q4=str(input("Choose an answer: ""\n"))
                                                if T1Q4=='a' or T1Q4=='A':
                                                                total_correct_t1+=1
                                                                print("Correct!""\n")
                                                else:
                                                                total_incorrect_t1+=1
                                                                print("Incorrect!""\n")

                                                print("Question 5: What is the best selling console of all time?")
                                                print("(A) Wii")
                                                print("(B) Xbox 360")
                                                print("(C) Playstation Two")
                                                print("(D) Nintendo DS")

                                                T1Q5=str(input("Choose an answer: ""\n"))
                                                if T1Q5=='c' or T1Q5=='C':
                                                                total_correct_t1+=1
                                                                print("Correct!""\n")
                                                else:
                                                                total_incorrect_t1+=1
                                                                print("Incorrect!""\n")

                                                print("Good you are done with the test!""\n")
#Here it shows your score for this test using print statements
                                                print("Here are your results:")
                                                print("The total number of questions right are:", total_correct_t1)
                                                print("The total number of questions wrong are:", total_incorrect_t1)
                                                print("\n")
#Using all of the variables in the question code,
#it will then check to see if you passed the test
#If you did pass the test then it will allow you to go to the next quiz
                                                if total_correct_t1==5 and total_incorrect_t1==0:
                                                                print("Awesome, you have passed the first test, on to the second one!""\n")
                                                                test_1='passed'
                                                elif total_correct_t1<5 or total_incorrect_t1>0:
                                                                print("Oh no you did not pass the test, better luck next time!")
                                                                print("Lets try it again!""\n")
                                                                test_1='start'
#This while loop makes sure that you passed the last quiz
#And then allows you to go onto the next one like last time
                while test_1=='passed':
                                start_2=str(input("Type 'start' or 'Start' to begin the second quiz!: ""\n"))
                                if start_2=='start' or start_2=='Start':
                                                print("Begin!""\n")
                                                test_1=False
                                                expert_test=True
                                else:
                                                print("ERROR, you did not input 'start', try again.""\n")
#Everything here is really the same, just different variables, questions, and answers
                if expert_test==True:
                                print("Make sure to type the letter of the answer not the actual answer.")
                                print("An example would be C or b""\n")
                                test_2='start'

                                while test_2=='start':
                                                total_correct_t2=0
                                                total_incorrect_t2=0

                                                print("Question 1: What Mario power up makes you bigger in size?")
                                                print("(A) Cardboard box")
                                                print("(B) Wooden starter sword")
                                                print("(C) Super mushroom")
                                                print("(D) Fire flower")

                                                T2Q1=str(input("Choose an answer: ""\n"))
                                                if T2Q1=='c' or T2Q1=='C':
                                                                total_correct_t2+=1
                                                                print("Correct!""\n")
                                                else:
                                                                total_incorrect_t2+=1
                                                                print("Incorrect!""\n")

                                                print("Question 2: Who is the main character of the Metal Gear series?")
                                                print("(A) Solid Snake")
                                                print("(B) Kirby")
                                                print("(C) Marth")
                                                print("(D) Kratos")

                                                T2Q2=str(input("Choose an answer: ""\n"))
                                                if T2Q2=='a' or T2Q2=='A':
                                                                total_correct_t2+=1
                                                                print("Correct!""\n")
                                                else:
                                                                total_incorrect_t2+=1
                                                                print("Incorrect!""\n")

                                                print("Question 3: What is the name of Cloud's sword in Final Fantasy 7?")
                                                print("(A) Master Sword")
                                                print("(B) Rebellion")
                                                print("(C) Buster Sword")
                                                print("(D) Lightsaber")

                                                T2Q3=str(input("Choose an answer: ""\n"))
                                                if T2Q3=='c' or T2Q3=='C':
                                                                total_correct_t2+=1
                                                                print("Correct!""\n")
                                                else:
                                                                total_incorrect_t2+=1
                                                                print("Incorrect!""\n")

                                                print("Question 4: What year did the first Call of Duty come out?")
                                                print("(A) 1999")
                                                print("(B) 2002")
                                                print("(C) 2005")
                                                print("(D) 2003")

                                                T2Q4=str(input("Choose an answer: ""\n"))
                                                if T2Q4=='d' or T2Q4=='D':
                                                                total_correct_t2+=1
                                                                print("Correct!""\n")
                                                else:
                                                                total_incorrect_t2+=1
                                                                print("Incorrect!""\n")

                                                print("Question 5: What is the best selling video game of all time?")
                                                print("(A) Minecraft")
                                                print("(B) Tetris")
                                                print("(C) Pac-man")
                                                print("(D) Grand Theft Auto V")

                                                T2Q5=str(input("Choose an answer: ""\n"))
                                                if T2Q5=='a' or T2Q5=='A':
                                                                total_correct_t2+=1
                                                                print("Correct!""\n")
                                                else:
                                                                total_incorrect_t2+=1
                                                                print("Incorrect!""\n")

                                                print("Awesome you are done with the test!""\n")
                                                print("Here are your results:")
                                                print("The total number of questions right are:", total_correct_t2)
                                                print("The total number of questions wrong are:", total_incorrect_t2)
                                                print("\n")

                                                if total_correct_t2==5 and total_incorrect_t2==0:
                                                                print("Awesome, you have passed the second and final test!""\n")
                                                                test_2='passed'
                                                elif total_correct_t2<5 or total_incorrect_t2>0:
                                                                print("Oh no you did not pass the test, better luck next time!")
                                                                print("Lets try it again!""\n")
                                                                test_2='start'
#These are ending comments and parameters
                if test_2=='passed':
                                print("Awesome, how was the quizzes?")
                                print("I hopped you enjoyed it!")
                                print("While it was simple I did really enjoy making it!""\n")
                else:
                                print("Error")
#You have the choice of ending the program or looking at the answer list
                print("If you want to see the answer list type 'answer' or 'Answer'")
                print("If you are done then type 'end' and have a good day!""\n")
#It uses a while loop so it does not auto end the program
                command=True
                while command==True:
                                answer_command=str(input("Type what you would like to do: ""\n"))
                                if answer_command=='answer' or answer_command=='Answer':
                                                answer_list()
                                elif answer_command=='end' or answer_command=='End':
                                                command=False
                                                print("Thanks for playing my quiz, have a great day!""\n")
                                                print("Special thanks to https://www.wikipedia.org/ for all the information in the quizzes!")
                                else:
                                                print("Error, you have not inputed the right command/commands to continue.""\n")
                                                print("Try again""\n")
                

#This is the main, it will start, loop, and end the entire program
main()                
































