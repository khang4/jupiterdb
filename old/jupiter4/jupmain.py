from jupiter import _jupiter;
import jupconsts;

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
        print("\n0: add applicant\n1: show applicants\n2: modify...\n3: exit");
        choice=int(input(">"));

        if choice==0:
            jupiter.addStudent(multiPrompt(jupconsts.studentCols));

        elif choice==1:
            jupiter.listStudents();

        elif choice==2:
            modifyMenu();

        elif choice==3:
            quit();

def modifyMenu():
    i=0;
    for x in jupconsts.tableNames:
        print("{}: {}".format(i,x));
        i+=1;

    print("{}: return".format(i+1));

    choice=int(input(">"));

    if choice==0:
        jupiter.modifyEntry("applicants","student_id",jupconsts.studentCols,jupconsts.a_studentCols);

    elif choice==1:
        return;

if __name__=="__main__":
    main();