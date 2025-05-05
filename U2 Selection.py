#SDGS Trivia Game

#Get the user name and introduce the game
name = str(input("What is your name?: "))
print()
print("Welcome to the SDGs Trivia Game " +name+ ",where you will get to learn more about the goals,become more aware,and gain valuable infromation to get in action for helping achieve the goals?")
print()
#List of the questions + Answers + Hints
questions = ["Which SDG goal relates to agriculture?(     )","Which SDG goal relates to hospitals?(     )", "Which SDG goal relates to having a fair life?(     )","Which SDG goal relates to marine pollution?(     )"]
answers = ["zero hunger","good health and well-being","quality education","life below water"]

#List of hints
hints1=["Sustainable agriculture practices increase food resilience in climate-vulnerable regions.","Mental health is often excluded from public health discussions despite rising global demand.","Gender disparities in education are often intensified by cultural norms and conflict.","Ocean ecosystems are collapsing under the weight of industrial overfishing and pollution."]
hints2=["Malnutrition remains a silent crisis, often rooted in poverty and unequal food distribution.","Preventable diseases continue to thrive in communities with weak infrastructure and low trust in institutions.","Education reform must go beyond access ,it must also ensure relevance, quality, and inclusion.","Coral bleaching serves as a visible indicator of wider climate instability."]

#Counter for each questions in the list instead of printing seprate variables
counter = 0
while counter < 4:
    for i in range(0,4):
        answer = input(questions[counter])
        if answer.lower() == answers[counter]:
            print("✅well done")
            break
        else:
            print("❌ Incorrect. Here's a hint")
            print(hints1[counter])
            answer = input(questions[counter])
            if answer.lower() == answers[counter]:
                print("✅well done")
                break
            else:
                print("❌ Incorrect. Here's a hint")
                print(hints2[counter])
                answer = input(questions[counter])
    counter = counter + 1

print("Well done for Completeing this game. Dont forget to always pratice!")

