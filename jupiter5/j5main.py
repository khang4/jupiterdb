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
                print();
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

    choice=input(">");

    if not choice.isdigit():
        print("! INVALID ENTRY !\n");
        return menu(choices);

    choice=int(choice);
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

    while 1:
        currentStudent=jupiter.getStudent(selectedId);

        if not currentStudent:
            return;

        print();
        print("selected student:");
        print("name: {},{}".format(currentStudent[2],currentStudent[1]));
        print("address: {}, {}, {}, {}".format(currentStudent[4],currentStudent[3],currentStudent[6],currentStudent[5]));
        print("email: {}".format(currentStudent[7]));
        print("gender: {}".format(currentStudent[8]));
        print("birthday: {}".format(str(currentStudent[9])));

        choice=menu(["edit","phone numbers","applications","delete","return"]);

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
                print();
                print("{}, {}: phone numbers:".format(currentStudent[1],currentStudent[2]));
                numbers=jupiter.getPhones(currentStudent[0]);

                for ix,x in enumerate(numbers):
                    print("{}: {}".format(ix,x));

                phonechoice=menu(["edit","add","delete","return"]);

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
                    print("select phone number to delete (input number next to phone number in list):");
                    phoneDeleteChoice=int(input(">"));
                    jupitewr.delRow("phone_number",["phone_number","student_id"],
                        [numbers[phoneDeleteChoice],currentStudent[0]]);

                if phonechoice==3:
                    break;

        elif choice==2:
            applicationMode(currentStudent[0],currentStudent[1],currentStudent[2]);

        elif choice==3:
            jupiter.delRow("applicants","student_id",currentStudent[0]);
            print("deleting selected student...");
            return;

        elif choice==4:
            return;

def degreeMode():
    while 1:
        print();
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
                print();
                currentDegree=jupiter.getDegree(currentDegreeString);
                print("degree selected:");
                print("name: {}".format(currentDegree[0]));
                print("department: {}".format(currentDegree[1]));
                print("director: {}".format(currentDegree[2]));
                print("email: {}".format(currentDegree[3]));
                print("phone: {}".format(currentDegree[4]));

                selectedDegreeChoice=menu(["edit","requirements (questions)","rubric","delete","return"]);

                if selectedDegreeChoice==0:
                    print("select field to edit:");
                    editChoice=menu(["name","department","director","email","phone"]);
                    degreeColumns=["degree_name","department","director","email","phone_number"];
                    print("new value:");
                    newValue=input(">");
                    if jupiter.update("degree","degree_name",currentDegree[0],degreeColumns[editChoice],newValue):
                        if editChoice==0:
                            currentDegreeString=newValue;

                elif selectedDegreeChoice==1:
                    reqMode(currentDegreeString);

                elif selectedDegreeChoice==2:
                    rubricMode(currentDegreeString);

                elif selectedDegreeChoice==3:
                    jupiter.delRow("degree","degree_name",currentDegree[0]);
                    print("deleting degree {}...".format(currentDegree[0]));
                    break;

                elif selectedDegreeChoice==4:
                    break;

        #add new degree
        elif choice==1:
            newDegree=promptValues(["degree name: ","department: ","director: ","email: ",
                "phone: "]);

            newDegree.append("");

            jupiter.add("degree",[newDegree]);

        elif choice==2:
            return;

def reqMode(currentDegreeString):
    while 1:
        print();
        print("requirements of degree {}:".format(currentDegreeString));

        reqs=jupiter.getReqs(currentDegreeString);
        for ix,x in enumerate(reqs):
            print("{}: {}".format(ix,x[1]));
        print();

        resChoice=menu(["select","add","return"]);

        if resChoice==0:
            print("enter id of requirement to select:");
            selectedReqIndex=int(input(">"));

            currentRequirementText=reqs[selectedReqIndex];
            selectedReqId=currentRequirementText[0];
            currentRequirementText=currentRequirementText[1];

            while 1:
                print();
                print('''answers of "{}" of degree {}:'''.format(currentRequirementText,currentDegreeString));
                answers=jupiter.getAnswers(selectedReqId);

                maxAnswerId=-1;
                for x in answers:
                    print("{}: {}".format(x[0],x[1]));
                    maxAnswerId=max(maxAnswerId,x[0]);
                print();

                answerChoice=menu(["add answer","delete answer","delete current requirement","change current requirement question","return"]);

                if answerChoice==0:
                    print("input new answer:");
                    newAnswer=input(">");

                    if jupiter.add("answer",[maxAnswerId+1,selectedReqId,newAnswer]):
                        maxAnswerId+=1;

                elif answerChoice==1:
                    print("input answer id to remove:");
                    removeAnswer=int(input(">"));
                    jupiter.delRow("answer",["answer_id","requirement_id"],[removeAnswer,selectedReqId]);

                elif answerChoice==2:
                    jupiter.delRow("requirement",["requirement_id","degree_name"],[selectedReqId,currentDegreeString]);
                    break;

                elif answerChoice==3:
                    print("input new question:");
                    changedQuestion=input(">");
                    jupiter.update("requirement","requirement_id",selectedReqId,"question",changedQuestion);
                    currentRequirementText=changedQuestion;

                elif answerChoice==4:
                    break;

        elif resChoice==1:
            print("input question of new requirement:");
            newReq=input(">");

            if jupiter.add("requirement",[j5const.tableMaxKeys["requirement"]+1,currentDegreeString,newReq]):
                j5const.tableMaxKeys["requirement"]+=1;

        elif resChoice==2:
            break;

def rubricMode(currentDegreeString):
    while 1:
        print();
        print("rubric for degree {}".format(currentDegreeString));
        print();

        rubChoice=menu(["edit description","edit criteria","return"]);

        if rubChoice==0:
            pass;

        elif rubChoice==1:
            pass;

        elif rubChoice==2:
            return;

def applicationMode(studentId,firstName,lastName):
    while 1:
        print();
        print("applications for {}, {}:".format(lastName,firstName));

        applications=jupiter.getApplications(studentId);

        for ix,x in enumerate(applications):
            print("{}: {},{},{}".format(ix,x[0],x[1],x[2]));

        print();
        appChoice=menu(["select","create","return"]);

        if appChoice==0:
            print("input number next to application to select it:");
            appSelect=int(input(">"));

            selectedApplicationMode(applications[appSelect][3]);

        elif appChoice==1:
            print("select degree for new application:");
            degrees=jupiter.getDegrees();
            createDegree=menu([x[0] for x in degrees]);

            semesters=["spring","fall"];
            print("select semester:");
            createSemester=menu(semesters);

            print("input year of application:");
            createYear=int(input(">"));

            if jupiter.add("application",[j5const.tableMaxKeys["application"]+1,
                degrees[createDegree][0],studentId,"",semesters[createSemester],createYear]):
                j5const.tableMaxKeys["application"]+=1;

        elif appChoice==2:
            return;

def selectedApplicationMode(appid):
    while 1:
        currentApplication=jupiter.getApplicationDetail(appid);
        print();
        print("current selected application:");
        print("degree: {}".format(currentApplication[0]));
        print("semester: {}".format(currentApplication[1]));
        print("year: {}".format(currentApplication[2]));
        print();

        selectChoice=menu(["educations","GRE scores","essay",
            "reference emails","answers","edit details","delete this application","return"]);

        if selectChoice==0:
            while 1:
                print();
                print("educations of some application:");
                educations=jupiter.getEducations(appid);

                educationIdMax=-1;
                for ix,x in enumerate(educations):
                    print("{}: {} in {} from {} with {} GPA, {}".format(ix,x[3],x[2],x[1],x[5],x[4]));
                    educationIdMax=max(educationIdMax,x[0]);
                print();

                edChoice=menu(["add","edit","delete","return"]);

                if edChoice==0:
                    print("adding education:");
                    newEd=promptValues(["college:","major:","degree (BS,BA,MS,MA):",["date","graduation date:"],"gpa"]);

                    if jupiter.add("education",[educationIdMax+1,appid,newEd[0],newEd[1],
                        newEd[2],newEd[3],newEd[4]]):
                        educationIdMax+=1;

                elif edChoice==1:
                    print("input number next to education to edit it:");
                    editChoice=int(input(">"));
                    print("select field to edit:");
                    fieldChoice=menu(["college","major","degree type","graduation date","gpa"]);
                    educationFields=["college","major","degree","grad_data","gpa"];

                    print("input new value:");
                    if fieldChoice==3:
                        newValue=promptDate();

                    elif fieldChoice==4:
                        newValue=float(input(">"));

                    else:
                        newValue=input(">");

                    jupiter.update("education",["education_id","application_id"],
                        [educations[editChoice][0],appid],educationFields[fieldChoice],newValue);

                elif edChoice==2:
                    print("type number next to education to delete:");
                    deleteChoice=int(input(">"));

                    jupiter.delRow("education",["education_id","application_id"],[educations[deleteChoice][0],appid]);

                elif edChoice==3:
                    break;

        elif selectChoice==1:
            while 1:
                print();
                print("GRE scores for current application:");
                gres=jupiter.getGres(appid);

                greMaxId=-1;
                for ix,x in enumerate(gres):
                    print("gre test {}:\nverbal reasoning: {}\nquantitative reasoning: {}\nanalytical writing: {}\ndate taken: {}\n".format(ix,x[1],x[2],x[3],x[4]));
                    greMaxId=max(greMaxId,x[0]);

                greChoice=menu(["add","edit","delete","return"]);

                if greChoice==0:
                    print("adding new gre scores:");
                    greValues=promptValues(["verbal reasoning score:","quantitative reasoning score:",
                        "analytical writing score:",["date","date taken:"]]);

                    greValues.insert(0,appid);
                    greValues.insert(0,greMaxId+1);

                    if jupiter.add("gre",greValues):
                        greMaxId+=1;

                elif greChoice==1:
                    print("input number of test to edit:");
                    greEdit=int(input(">"));

                    print("choose field to edit:");
                    fieldChoice=menu(["verbal reasoning score","quantitative reasoning score",
                        "analytical writing score","date taken"]);
                    actualFields=["verbal","quant","analytic","taken"];

                    print("input new value:");
                    if fieldChoice==3:
                        newValue=promptDate();

                    else:
                        newValue=input(">");

                    jupiter.update("gre",["gre_id","application_id"],[gres[greEdit][0],appid],
                        actualFields[fieldChoice],newValue);

                elif greChoice==2:
                    print("gre test number to delete:");
                    deleteChoice=int(input(">"));

                    jupiter.delRow("gre",["gre_id","application_id"],[gres[deleteChoice][0],appid]);

                elif greChoice==3:
                    break;

        elif selectChoice==2:
            pass;

        elif selectChoice==3:
            while 1:
                print();
                print("reference emails of current application:");
                emails=jupiter.getEmails(appid);

                maxEmailId=-1;
                for ix,x in enumerate(emails):
                    print("email {}:\nfrom: {}\nbody: {}\n".format(ix,x[1],x[2]));
                    maxEmailId=max(maxEmailId,x[0]);

                emailChoice=menu(["add","edit","delete","return"]);

                if emailChoice==0:
                    if len(emails)>=3:
                        print("maximum 3 email references. delete one and try again");

                    else:
                        print("adding new email reference:");
                        emailValues=promptValues(["referencer name:","body:"]);
                        emailValues.insert(0,appid);
                        emailValues.insert(0,maxEmailId+1);
                        if jupiter.add("email",emailValues):
                            maxEmailId+=1;

                elif emailChoice==1:
                    print("input email number to edit:");
                    emailEditChoice=int(input(">"));

                    print("select field to edit:");
                    fieldChoice=menu(["referencer name","body"]);
                    actualFields=["referencer","body"];

                    print("enter new value:");
                    newValue=input(">");

                    jupiter.update("email",["email_id","application_id"],
                        [emails[emailEditChoice][0],appid],actualFields[fieldChoice],newValue);

                elif emailChoice==2:
                    print("select number next to email to delete:");
                    deleteEmail=int(input(">"));

                    jupiter.delRow("email",["email_id","application_id"],[emails[deleteEmail][0],appid]);

                elif emailChoice==3:
                    break;

        elif selectChoice==4:
            questions=jupiter.getReqs(currentApplication[0]);
            print(questions);

        elif selectChoice==5:
            print("select field to edit:");
            fields=["degree","semester","year"];
            editChoice=menu(fields);

            if editChoice==0:
                print("select new degree:");
                degrees=jupiter.getDegrees();
                newDeg=degrees[menu([x[0] for x in degrees])];

                jupiter.update("application","application_id",appid,"degree_name",newDeg);

            elif editChoice==1:
                print("select new semester:");
                semesters=["spring","fall"];
                newSem=semesters[menu(semesters)];

                jupiter.update("application","application_id",appid,"semester",newSem);

            elif editChoice==2:
                print("input new year:");
                newYear=int(input(">"));

                jupiter.update("application","application_id",appid,"year",newYear);

        elif selectChoice==6:
            pass;

        elif selectChoice==7:
            return;

if __name__=="__main__":
    main();