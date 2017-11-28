from j5sql import _jupiter;
import j5const;

jupiter=_jupiter("jupiter");

def main():
    while 1:
        print();
        choice=menu(["student mode","degree mode","quit"]);
        print();

        #student mode selected
        if choice==0:
            while 1:
                print("students:");
                displayApplicants();
                print();

                studentChoice=menu(["select student","add","return"]);

                if studentChoice==0:
                    studentMode();

                elif studentChoice==1:
                    studentvalues=promptValues(["first name:","last name:",["label","address:"],
                        "city:","street:","zip:","state:",["endlabel"],"email:",
                        "gender:",["date","birthday:",]]);

                    studentvalues.insert(0,j5const.tableMaxKeys["applicants"]+1);

                    if jupiter.add("applicants",[studentvalues]):
                        j5const.tableMaxKeys["applicants"]+=1;

                elif studentChoice==2:
                    break;

        #degree mode selected
        elif choice==1:
            degreeMode();

        elif choice==2:
            quit();

#multiple chioce menu, give array of chioces and return
#the picked answer. multiple choice means the answer must be
#an int!
def menu(choices):
    for i,x in enumerate(choices):
        print("{}: {}".format(i+1,x));

    choice=int(input(">"));

    if choice<1 or choice>=len(choices)+1:
        print("! INVALID ENTRY !\n");
        return menu(choices);

    return choice-1;

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
        print("selected student:");
        print("name: {},{}".format(currentStudent[2],currentStudent[1]));
        print("address: {}, {}, {}, {}".format(currentStudent[4],currentStudent[3],currentStudent[6],currentStudent[5]));
        print("email: {}".format(currentStudent[7]));
        print("gender: {}".format(currentStudent[8]));
        print("birthday: {}".format(str(currentStudent[9])));

        choice=menu(["edit","phone numbers","applications","return"]);

        if choice==0:
            print("select field to edit:");
            editChoice=menu(["first name","last name","addresss: city","address: street","address: zip","address: state"
                ,"email","gender","birthday"]);

            studentColumns=["first_name","last_name","address_city","address_street",
                "address_zip","address_state","email","gender","birthday"];

            print("new value:");

            newValue="";
            if editChoice!=8:
                newValue=input(">");
            else:
                newValue=promptDate();

            jupiter.update("applicants","student_id",currentStudent[0],studentColumns[editChoice],newValue);

        elif choice==1:
            while 1:
                print("{}, {}: phone numbers:".format(currentStudent[1],currentStudent[2]));
                numbers=jupiter.getPhones(currentStudent[0]);

                for ix,x in enumerate(numbers):
                    print("{}: {}".format(ix,x));

                phonechoice=menu(["edit...","add...","return"]);

                if phonechoice==0:
                    print("select phone number to edit (input number next to phone number in list):");
                    phoneEditChoice=int(input(">"));
                    print("new phone number:");
                    newPhone=input(">");
                    jupiter.update("phone_number",["phone_number","student_id"],
                        [numbers[phoneEditChoice],currentStudent[0]],"phone_number",newPhone);

                if phonechoice==1:
                    print("adding phone number:");
                    newNumber=input(">");
                    jupiter.add("phone_number",[[newNumber,currentStudent[0]]]);

                if phonechoice==2:
                    break;

        elif choice==2:
            pass;

        elif choice==3:
            return;

def degreeMode():
    while 1:
        print("degrees:");

        degrees=jupiter.getDegrees();
        for ix,x in enumerate(degrees):
            degrees[ix]=x[0];
            print("{}: {}".format(ix,x[0]));
        print();

        choice=menu(["select","add","return"]);

        #select degree
        if choice==0:
            print("enter the number left of the degree to select it");
            currentDegreeString=degrees[int(input(">"))];

            while 1:
                currentDegree=jupiter.getDegree(currentDegreeString);
                print("degree selected:");
                print("name: {}".format(currentDegree[0]));
                print("department: {}".format(currentDegree[1]));
                print("director: {}".format(currentDegree[2]));
                print("email: {}".format(currentDegree[3]));
                print("phone: {}".format(currentDegree[4]));

                selectedDegreeChoice=menu(["edit","requirements","rubric","delete","return"]);

                if selectedDegreeChoice==0:
                    print("select field to edit:");
                    editChoice=menu(["name","department","director","email","phone"]);
                    degreeColumns=["degree_name","department","director","email","phone_number"];
                    print("new value:");
                    newValue=input(">");
                    jupiter.update("degree","degree_name",currentDegree[0],degreeColumns[editChoice],newValue);

                elif selectedDegreeChoice==1:
                    pass;

                elif selectedDegreeChoice==2:
                    pass;

                elif selectedDegreeChoice==3:
                    pass;

                elif selectedDegreeChoice==4:
                    break;


        #add new degree
        elif choice==1:
            newDegree=promptValues(["degree name: ","department: ","director: ","email: ",
                "phone: "]);

            jupiter.add("degree",[newDegree]);

        elif choice==2:
            return;

if __name__=="__main__":
    main();