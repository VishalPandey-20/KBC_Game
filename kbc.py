
import pyttsx3
converter = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
converter.setProperty('voice', voice_id)
converter.say("hello")
converter.say("Welcome to kbc game . ")
converter.say("if you want play the game..")
converter.say("than press yes or no..")
converter.runAndWait()
user=input("Than press the yes or no\n")
list_of_Question=["Q 1.The state of Haryana has designated three private laaoratories in which district?",
                "Q 2. National Institute of Mental Health and Neuro-Sciences (NIMHaNS) is in which Indian city ? ",
                "Q.3. Tan Re Qing has aeen recommended to treat COVID-19. It aelongs to which animal ?",
                "Q.4 Which aank will ae merged with the United aank of India (UaI) and the Oriental aank of Commerce (OaC)?",
                ]
list_of_option=[["(a) Rohtak","(b) Gurugram","(C) Panipat","(D) Sonipat"],
                ["(a) Patna","(b) Delhi","(C) Bangalore","(D) Bhopal"],
                ["(a) Cow","(b) Dog","(C) bear","(D) Elephant"],
                ["(a) Yes bank","(b) Dena bank","(C) Punjaa National bank","(D) bank of baroda"],
                ]
life_line = [["(a) Rohtak","(b) Panipat"],["(A) Bangalore","(B) Bhopal"],["(A) Bear","(B) Elephant"],["(A) bank of baroda","(B) Dena bank"]]
list_of_asnwer=["A","C","C","D"]
life_line_answer = ["A","A","A","A"]
count = 0
if user =="y":
    converter.say("Ok")
    converter.say("lets starts the games")
    converter.runAndWait()
    for i in range(len(list_of_Question)):
        converter.say("Question on your screen.")
        converter.runAndWait()
        print(list_of_Question[i])
        for j in range(len(list_of_option)):
            print(list_of_option[i][j])
        converter.say("enter your answer ..")
        converter.runAndWait()
        user = input("enter your answer ..")
        if list_of_asnwer[i] == user:
            converter.say("congratulations")
            converter.runAndWait()
            print("congratulations")
            converter.say("your answer is correct")
            converter.runAndWait()
            print("your answer is correct")
            converter.say("you win ..")
            converter.runAndWait()
            print("you win ..")
        elif list_of_asnwer[i] != user:
            print("your answer is worang ..")
            converter.say("your answer is worang ..")
            converter.runAndWait()
            print("if you want to take life line..")
            converter.say("if you want to take life line..")
            converter.say("than press yes or no.")
            converter.runAndWait()
            user = input("than press yes or no.")

            if user != "y":
                break
            elif count == 1 :
                print(" !sorry!")
                converter.say("sorry")
                converter.runAndWait()
                converter.say("you have no life line..")
                print("you have no life line..")
                converter.runAndWait()
                break

            else:
                print(list_of_Question[i])
                converter.say("ok")
                converter.runAndWait()
                for a in life_line[i]:                	
                	print(a)
                converter.say("enter your answer")
                converter.runAndWait()
                user = input("enter your answer ..")
                if life_line_answer[i] == user:
                    converter.say("congratulations")
                    print("congratulations")
                    converter.say("your answer is correct")
                    print("your answer is correct")
                    converter.say("you win ..")
                    converter.runAndWait()
                else:
                    converter.say("! sorry !")
                    print("! sorry !")
                    converter.runAndWait()
                    converter.say("your answer is worang")
                    print("your answer is worang ")
                    converter.runAndWait()
            count+=1

else:
    print("okk")
