from jupiter import _jupiter;

jupiter=_jupiter("jupiter");

def main():
    mainMenu();

def multiPrompt(prompts):
    res=[];
    for x in prompts:
        val=input(x+": ");
        res.append(val);

    return res;

def mainMenu():
    while 1:
        print("\n0: add student\n1: show students\n2: modify student\n3: exit");
        choice=int(input(">"));

        if choice==0:
            jupiter.addStudent(multiPrompt(jupiter.studentCols));

        elif choice==1:
            jupiter.listStudents();

        elif choice==2:
            jupiter.modifyEntry("applicants","student_id",jupiter.studentCols,jupiter.a_studentCols);

        elif choice==3:
            quit();

if __name__=="__main__":
    main();