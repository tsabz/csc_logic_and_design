tuition = 20000


for i in range(1, 11):
    tuition += tuition*0.03
    print("The tuition will be " + str(tuition) + " in " + str(i) + " year(s)")
