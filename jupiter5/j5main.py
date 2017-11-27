from j5sql import _jupiter;
import j5const;

jupiter=_jupiter("jupiter");

def main():
    while 1:
        print();
        choice=menu(["select...","add...","list...","quit"]);
        print();

        if choice==0:
            print("select mode:");
            selectChoice=menu(["applicant","degree","return"]);

            if selectChoice==0:
                print("selecting student...");
                studentMode();

            elif selectChoice==1:
                print("selecting degree...");

        elif choice==1:
            print("add mode:");
            addChoice=menu(["applicant","degree","return"]);

            if addChoice==0:
                print("adding student...");
                studentvalues=promptValues(["first name:","last name:",["label","address:"],
                    "city:","street:","zip:","state:",["endlabel"],"email:",
                    "gender:",["date","birthday:",]]);

                studentvalues.insert(0,j5const.tableMaxKeys["applicants"]+1);

                if jupiter.add("applicants",[studentvalues]):
                    j5const.tableMaxKeys["applicants"]+=1;

            elif addChoice==1:
                print("adding degree...");
                degreevalues=promptValues(["degree name:","department:","director:","email:","phone:"]);

                jupiter.add("degree",[degreevalues]);

        elif choice==2:
            print("list mode:");
            listchoice=menu(["applicants","degrees","return"]);

            if listchoice==0:
                displayApplicants();

            elif listchoice==1:
                displayDegrees();

        elif choice==3:
            quit();

#multiple chioce menu, give array of chioces and return
#the picked answer. multiple choice means the answer must be
#an int!
def menu(choices):
    for i,x in enumerate(choices):
        print("{}: {}".format(i,x));

    choice=int(input(">"));

    if choice<0 or choice>=len(choices):
        print("! INVALID ENTRY !\n");
        return menu(choices);

    return choice;

#prompts for all values in inputted array of values prompts,
#returns all user's answers in array. no error checking.
#in the prompts array, use an array prompt instead of a string
#for special options
def promptValues(prompts):
    res=[];
    indent="";
    for x in prompts:
        if not isinstance(x,list):
            print(indent+x);
            res.append(input(indent+">"));
            print();

        else:
            if x[0]=="date":
                print(x[1]);
                res.append(promptDate());

            elif x[0]=="label":
                print(x[1]);
                indent="    ";

            elif x[0]=="endlabel":
                indent="";

    return res;

#prompt user for things in a date, returns a date string
#enterable into a sql query
#include time=1 to also prompt for time and return datetime string
#DOES NO ERROR CHECKING! if they entered something bad the sql will
#crash
def promptDate(time=0):
    datestr="";

    print("year:");
    datestr+=input(">");
    datestr+="-";

    print("month:");
    datestr+=input(">");
    datestr+="-";

    print("day:");
    datestr+=input(">");

    if time:
        datestr+=" ";

        print("hour:");
        datestr+=input(">");
        datestr+=":"

        print("minute:");
        datestr+=input(">");
        datestr+=":"

        print("seconds:");
        datestr+=input(">");

    return datestr;

def displayApplicants():
    print("applicants list:");
    applicants=jupiter.getApplicants();

    for x in applicants:
        print('''{}: {}, {}'''.format(x[0],x[2],x[1]));

def displayDegrees():
    print("degrees list:");
    degrees=jupiter.getDegrees();

    for x in degrees:
        print(x[0]);

def studentMode():
    print("enter student id or letter to quit:");
    selectedId=input(">");

    if not selectedId.isdigit():
        return;

    currentStudent=jupiter.getStudent(selectedId);

    if not currentStudent:
        return;

    while 1:
        print("\nselected student: {}, {}".format(currentStudent[1],currentStudent[2]));
        choice=menu(["view information","edit information","view/edit phone numbers","view/edit applications","return"]);

        if choice==0:
            # print(currentStudent);
            print("name: {},{}".format(currentStudent[2],currentStudent[1]));
            print("address: {}, {}, {}, {}".format(currentStudent[4],currentStudent[3],currentStudent[6],currentStudent[5]));
            print("email: {}".format(currentStudent[7]));
            print("gender: {}".format(currentStudent[8]));
            print("birthday: {}".format(str(currentStudent[9])));

        elif choice==1:
            pass;

        elif choice==2:
            pass;

        elif choice==3:
            pass;

        elif choice==4:
            return;


if __name__=="__main__":
    main();