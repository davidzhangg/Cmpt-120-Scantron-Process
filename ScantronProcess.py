##CMPT 120 Scantron Processing Project


def read_string_list_from_file(the_file):
    '''
    GENERIC READING OF TEXT FILE
    USE AS TEMPLATE, INCORPORATE IN YOUR FILE
    GENERATES A LIST OF STRINGS, ONE STRING PER ELEMENT
    AUTHOR: Diana Cukierman

    Assumptions:
    1) the_file is in the same directory (folder) as this program 
    2) the_file contains one student per "line"  
    3) lines are separated by "\n", that is, after each "line" (student)
       in the file  there is a return ("\n") . Also there is (one single)
       return ("\n") after the last line  in the_file
    4) This function returns a list of strings
    '''
    
    fileRef = open(the_file,"r")      # opening file to be read
    localList=[]                      # new list being constructed
    for line in fileRef:
        string = line[0:len(line)-1]  # -1: eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)      # appends a new element
                                      # of type string to the list
        
    fileRef.close()

        #........
    print ("\n JUST TO TRACE, the local list of strings is:\n")
    for element in localList:
        print (element)  # element is a string for one student
    #........
        
    return localList


def write_result_to_file(lres,the_file):
    '''
    Creates a text output file from a list of strings
    AUTHOR: Diana Cukierman
    
    Assumptions:
    1) lres is a list of strings, where each string
       will be one line in the output file
    2) the_file will contain the name fo the output file.
       for this porgram it shoudl be a name with .csv extension
    3) it is assumed that each string in lres already includes
       the character "\n" at the end
    4) the resulting file will be in the same directory (folder) as this program 
    5) the resulting file will  contain one student data per line 
    '''
    
    fileRef = open(the_file,"w") # opening file to be written
    for line in lres:
        fileRef.write(line)
                                    
    fileRef.close()
    return


def total_pts():                            
    total = 0
    for i in range(len(key_list())):
        total = total + key_list()[i]
    return total

def high_score(list):                       
    maximum = 0
    for i in range(len(list)):
        if (maximum < list[i]):
            maximum = list[i]
    return maximum

def only_ans():                                 ##make a list of the students answers
    locallist = []
    for i in range(len(stud_ans)):
        st = ""
        for k in range(len(stud_ans[i])):
            if (stud_ans[i][k].isdigit()):
                st = st + stud_ans[i][k]
        locallist.append(st)
    return locallist

def stud_names():
    locallist = []
    for i in range(len(stud_ans)):
        st = ""
        for k in range(len(stud_ans[i])):
            if (stud_ans[i][k].isalpha()):
                st = st + stud_ans[i][k]
        locallist.append(st)
    return locallist

def answer_key():
    st = ""
    for i in range(len(key[0])):
        if(int(key[0][i]) == 1):
            st += "A" + " "
        if(int(key[0][i]) == 2):
            st += "B" + " "
        if(int(key[0][i]) == 3):
            st += "C" + " "
        if(int(key[0][i]) == 4):
            st += "D" + " "
        if(int(key[0][i]) == 5):
            st += "E" + " "
    return st

def hard_questions(list):                   ##determines the number of questions
    locallist = []
    minimum = list[0]
    for i in range(len(list)):
        if (minimum > list[i]):
            minimum = list[i]
    for i in range(len(list)):
        if (list[i] == minimum):
            locallist.append(i+1)
    return locallist

def process_ans():                          ##calculates each students total points based of answer key
    locallist = []
    for i in range(len(stud_ans)):
        total = 0
        for k in range(len(list_of_only_ans[i])):
            if (list_of_only_ans[i][k] == key[0][k]):
                total = total + key_list()[k]
        locallist.append(total)
    return locallist

def list_of_percents():                     ##calculates the percentage each student got based on total mark
    locallist = []
    for i in range(len(list_scores)):
        percent = round((list_scores[i]/total_pts())*100,1)
        locallist.append(percent)
    return locallist

def average(list):
    total = 0
    for i in range(len(list)):
          total = total + list[i]
    avg = total / len(list)
    return avg

def output(alist1,alist2):              ##saves selected names and info into csv file
    locallist = []
    for i in range(len(alist1)):
        st = "'" + alist1[i] + "'" + "," + str(alist2[i]) + "," + str((alist2[i]/total_pts())*100) + "\n"
        locallist.append(st)
    return locallist

def calc_distr_pts(alist):              ##calculates the range of distribution points
    locallist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(distr_range)):
        for k in range(len(alist)):
            if (alist[k] <= distr_range[i] and alist[k] > (distr_range[i]-10)):
                locallist[i] = locallist[i] + 1
    return locallist

def correct_ans(list):                  ##displays amount of times the each answer was answered correctly
    locallist = []
    for i in range(len(key[0])):
        count = 0
        for k in range(len(list)):
            if (list[k][i] == key[0][i]):
                count += 1
        locallist.append(count)
    return locallist

def hard_questions(list):               ##calculates the most questions answered incorrectly
    locallist = []
    minimum = list[0]
    for i in range(len(list)):
        if (minimum > list[i]):
            minimum = list[i]
    for i in range(len(list)):
        if (list[i] == minimum):
            locallist.append(i+1)
    return locallist

def key_list():                       ##displays answer list
    st = ""
    lst = []
    for i in range(len(key[1])):
        if (key[1][i] != " "):
            st += key[1][i]
        if (key[1][i] == " "):
            lst.append(float(st))
            st = ""
        if (i == len(key[1])-1):
            lst.append(float(st))
    return lst
        

stud_ans = read_string_list_from_file("IN_data_studs.txt")
key = read_string_list_from_file("IN_key+pts.txt")
list_of_only_ans = only_ans()
list_stud_names = stud_names()
list_scores = process_ans()
percentages = list_of_percents()
distr_range = [10, 20, 30, 40, 50, 60 ,70, 80, 90, 100]

print()
print()
print("~ Welcome to this CMPT 120 Scantron Processing system ~")
print(" ===================================================== ")
print()
print("The data file in this folder has",len(stud_ans),"students.")
print()
print("There are",len(key[0]),"questions.")
print()
print("The answer key is:")
print(answer_key())
print()
print("The points are:")
for i in range(len(key_list())):
    print(key_list()[i], end=" ")
print()
print("The maximum points possible are:",total_pts())

print()
print()
print("You have to choose one of two options:")
print("Type ALL (not case sensitive) to process the whole class")
print("Type SEL (not case sensitive) to process selected students",'\n',
      "(up to half of the whole class)")
print()
user_input = input("Type ALL or SEL: ")
print()

while (user_input.isdigit()==True or (user_input.lower()!="all") and (user_input.lower() != "sel")):
    print("Please retype, ALL or SEL")
    user_input = input("Type in your option: ")
    print()

if (user_input.lower() == "all"):
    
    max_points = high_score(list_scores)
    avg = average(list_scores)
    correct = correct_ans(list_of_only_ans)
    hardest_questions = hard_questions(correct)
    distr_pts = calc_distr_pts(percentages)  
    print("All students have been processed.")
    print()
    print()
    print("Here is the output that will be saved in the folder!")
    print()
    for i in range(len(stud_ans)):
        st = "'" + list_stud_names[i] + "'" + ", " + str(list_scores[i]) + ", " + str(percentages[i])
        print(st)
        print()
    output_file = output(list_stud_names,list_scores)
    write_result_to_file(output_file,"output_testcase.csv")
    print()

    print("HERE ARE THE THE STATS!")
    print("=======================")
    print()
    print("Maximum points:",max_points)
    print()
    print("Average points:",avg)
    print()
    print("Number of students processed:",len(stud_ans))
    print()
    print("Number of times each question was answered correctly:")
    print(correct)
    print()
    print("Most difficult questions:",hardest_questions)
    print()
    print("Distribution points:",distr_pts)
    print("(Considering ranges:",distr_range,")")
    print()

if (user_input.lower() == "sel"):

    sel_answer = []
    sel_stud_names = []
    sel_points = []
    sel_percentage = []

    print("You chose to process selected students")
    print("You will be asked to provide the name of the student")
    print()
    sel_input=input("Type a name or END to finish: ")
 
    while sel_input.upper()!="END":
        count = 0
        if (sel_input.upper() == "END"):
            break
        else:
            for i in range(len(list_stud_names)):
                if (sel_input.upper() == list_stud_names[i]):
                    count = count + 1
                    print("Student " + list_stud_names[i] + " got " + str(list_scores[i]) + " points ")
                    sel_answer.append(list_of_only_ans[i])
                    sel_stud_names.append(list_stud_names[i])
                    sel_points.append(list_scores[i])
                    sel_percentage.append(percentages[i])
            if (count == 0):
                print("This name is not in the data, type again")
                print()
            sel_input = input("Type a name or END to finish: ") 

    max_points = high_score(sel_points)
    avg = average(sel_points)
    correct = correct_ans(sel_answer)
    hardest_questions = hard_questions(correct)
    distr_pts = calc_distr_pts(sel_percentage)

    print("All your selected students have been processed.")
    print()
    print()
    print("Here is the output that will be saved in the folder.")
    print()
    for i in range(len(sel_stud_names)):
        st = "'" + sel_stud_names[i] + "'" + ", " + str(sel_points[i]) + ", " + str(sel_percentage[i])
        print(st)
        print()
    output_file = output(sel_stud_names,sel_points)
    write_result_to_file(output_file,"output_result.csv")
    print()
			
    print("HERE ARE THE STATS")
    print("==================")
    print()
    print("Maximum points:",max_points)
    print()
    print("Average points:",avg)
    print()
    print("Number of students processed:",len(sel_answer))
    print()
    print("Number of times each question was answered correctly:")
    print(correct)
    print()
    print("Most difficult questions:",hardest_questions)
    print()
    print("Distribution points:",distr_pts)
    print("(Considering ranges:",distr_range,")")
    print()

input_graph = input("Would you like to graph the distribution? (Y/N): " )
if (input_graph.upper() == "Y"):
    import turtle as t
    t.penup()
    t.sety(-100)
    t.pendown()
    t.forward(350)
    t.left(180)
    t.forward(700)
    t.right(180)
    t.forward(60)
    t.left(90)
    t.colormode(255)
    t.fillcolor(66, 149, 244)
    for i in range(10):
        t.begin_fill()
        t.forward(int(distr_pts[i])*30)
        t.right(90)
        t.forward(22)
        t.right(90)
        t.forward(int(distr_pts[i])*30)
        t.left(90)
        t.end_fill()
        t.forward(40)
        t.left(90)

print()

print("All stats are done! Bye!")          
        
