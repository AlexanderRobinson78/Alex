#Hi my name is Alex Robinson
#Welcome to my Integration Project
#My project is 2 quizes based on the history of video games(yes I know I am a big geek)
#Ranging from Nintendo to Micosoft
#There will be 2 quizes, from 2 ranging difficulties: beginner to expert
#Beginner has 5 questions and expert has 8 questions
#To continue onto the next quiz you need to pass the last one

#Currently I am done with the first test but I am planning to do 2 more

#I have imported the math module because I believe I will need it later, but it is not used yet
import math

#This is the beginning code that explains what the program is and explains the basic parameters of the code
print("Hello! Welcome to my quiz program!")
print("The quiz program is based on the history of video games and it will test your knowledge.")
print("Ranging from Nintendo to Sony, you have to be a BIG nerd to know all of this")
print("There are two quizes, ranging from: beginnner to expert.")
print("You must pass the previous exam to go to the next one, to pass you have to get all of them correct.""\n")


#This while loop is the input to get to the first test, it will loop if the input is incorrect and if it is correct it will move on to the next line of code
x=True
while x==True:
                Start1=str(input("Type 'start' to begin the first quiz!: ""\n"))
                if Start1=='start':
                                print("Begin!""\n")
                                x=False
                                beginnerTest=True
                else:
                                print("ERROR, you did not input 'start', try again.")

#This is all the code for the first test, it contains 5 questions and 4 answers for each, and if you get it wrong or right it will count it in a variable
#It will ask you for an input from a to d, input what you think is correct, after each input it will say if it is correct or incorrect,
#then it will go onto the next question
if beginnerTest==True:
                Test1='start'
                while Test1=='start':
                                totalCorrectT1=0
                                totalIncorrectT1=0
                                print("Question 1: Who is the main character in the series Legend of Zelda?")
                                print("(A) Mario")
                                print("(B) Zelda")
                                print("(C) Ganon")
                                print("(D) Link")
#Each question has very similar code, that is pretty much copy and paste
#Each question code has totalCorrect and totalIncorrect variables, if either one is met it will add one value to it
                                T1Q1=str(input("Choose an answer: ""\n"))
                                if T1Q1=='d' or T1Q1=='D':
                                                totalCorrectT1+=1
                                                print("Correct!""\n")
                                else:
                                                totalIncorrectT1+=1
                                                print("Incorrect!""\n")

                                print("Question 2: What is the name of sony's first console?")
                                print("(A) NES")
                                print("(B) Playstation 1")
                                print("(C) Gamecube")
                                print("(D) Atari 2600")

                                T1Q2=str(input("Choose an answer: ""\n"))
                                if T1Q2=='b' or T1Q2=='B':
                                                totalCorrectT1+=1
                                                print("Correct!""\n")
                                else:
                                                totalIncorrectT1+=1
                                                print("Incorrect!""\n")

                                print("Question 3: What is Xbox's most popular series?")
                                print("(A) Mario Bros")
                                print("(B) Halo")
                                print("(C) Uncharted")
                                print("(D) Tetris")

                                T1Q3=str(input("Choose an answer: ""\n"))
                                if T1Q3=='b' or T1Q3=='B':
                                                totalCorrectT1+=1
                                                print("Correct!""\n")
                                else:
                                                totalIncorrectT1+=1
                                                print("Incorrect!""\n")

                                print("Question 4: What is the name of Mario's brother?")
                                print("(A) Luigi")
                                print("(B) Nathan")
                                print("(C) Billy")
                                print("(D) Donkey Kong")

                                T1Q4=str(input("Choose an answer: ""\n"))
                                if T1Q4=='a' or T1Q4=='A':
                                                totalCorrectT1+=1
                                                print("Correct!""\n")
                                else:
                                                totalIncorrectT1+=1
                                                print("Incorrect!""\n")

                                print("Question 5: What is the best selling console of all time?")
                                print("(A) Wii")
                                print("(B) Xbox 360")
                                print("(C) Playstation 2")
                                print("(D) Nintendo DS")

                                T1Q5=str(input("Choose an answer: ""\n"))
                                if T1Q5=='c' or T1Q5=='C':
                                                totalCorrectT1+=1
                                                print("Correct!""\n")
                                else:
                                                totalIncorrectT1+=1
                                                print("Incorrect!""\n")

                                print("Good you are done with the test!""\n")
#Here it shows your score for this test using print statements
                                print("Here are your results:")
                                print("The total number of questions right are:", totalCorrectT1)
                                print("The total number of questions wrong are:", totalIncorrectT1)
                                print("\n")
#Using all of the variables in the question code, it will then check to see if you passed the test
#If you did pass the test then it will allow you to go to the next quiz
                                if totalCorrectT1==5 and totalIncorrectT1==0:
                                                print("Awesome, you have passed the first test, on to the second one!""\n")
                                                Test1='passed'
                                elif totalCorrectT1<5 or totalIncorrectT1>0:
                                                print("Oh no you did not pass the test, better luck next time!")
                                                print("Lets try it again!""\n")
                                                Test1='start'
































