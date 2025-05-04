#SDGS Trivia Game

#Get the user name and introduce the game
name = str(input("What is your name?: "))
print()
print("Welcome to the SDGs Trivia Game " +name+ ",where you will get to learn more about the goals,become more aware,and gain valuable infromation to get in action for helping achieve the goals?")
print()
#List of the questions + Answers + Hints
question1 = ["Which SDG goal relates to agriculture?(     )"]
question2=["Which SDG goal relates to hospitals?(     )"]
question3=["Which SDG goal relates to having a fair life?(     )"]
question4=["Which SDG goal relates to marine pollution?(     )"]

answer1 = ["Zero Hunger(    )"]
answer2 = ["Good Health and well-being(    )"]
answer3 =["Quality Education(    )"]
answer4=["Life Below Water(    )"]
print()

#List of hints
q1=["Sustainable agriculture practices increase food resilience in climate-vulnerable regions."]
q1hint2=["Malnutrition remains a silent crisis, often rooted in poverty and unequal food distribution."]
q2=["Mental health is often› excluded from public health discussions despite rising global demand."]
q2hint2=["Preventable diseases continue to thrive in communities with weak infrastructure and low trust in institutions."]
q3=["Gender disparities in education are often intensified by cultural norms and conflict."]
q3hint2=["Education reform must go beyond access ,it must also ensure relevance, quality, and inclusion."]
q4=["Ocean ecosystems are collapsing under the weight of industrial overfishing and pollution."]
q4hint2=["Coral bleaching serves as a visible indicator of wider climate instability."]
print()
for i in range(0,4):
    answer = input(question1)
    if answer == answer1:
        print("✅well done")
    else:
        print("❌ Incorrect. Here's a hint")
        print(q1)
        if answer == answer1:
            print("✅well done")
    else:
    print("❌ Incorrect. Here's a hint")
        print(q1hint2)


for i in range(0,4):
    answer = input(question2)
    if answer == answer2:
        print("✅well done")
    else:
        print("❌ Incorrect. Here's a hint")
        print(q2)
        if answer == answer2:
            print("✅well done")
    else:
    print("❌ Incorrect. Here's a hint")
        print(q2hint2)


for i in range(0,4):
    answer = input(question3)
    if answer == answer3:
        print("✅well done")
    else:
        print("❌ Incorrect. Here's a hint")
        print(q3)
        if answer == answer3:
            print("✅well done")
    else:
    print("❌ Incorrect. Here's a hint")
        print(q3hint2)

for i in range(0,4):
    answer = input(question4)
    if answer == answer4:
        print("✅well done")
    else:
        print("❌ Incorrect. Here's a hint")
        print(q4)
        if answer == answer4:
            print("✅well done")
    else:
    print("❌ Incorrect. Here's a hint")
        print(q4hint2)






