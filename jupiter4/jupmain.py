from jupiter import _jupiter;

jupiter=_jupiter("jupiter");

def main():
    mainMenu();

def multiPrompt(*prompts):
    res=[];
    for x in prompts:
        val=input(x+": ");
        res.append(val);

    return res;

def mainMenu():
    while 1:
        print("\n0: add student\n1: show students\n2: exit");
        choice=int(input(">"));

        if choice==0:
            jupiter.addStudent(multiPrompt("first name","last name","city","street","zip","state","email","gender"));

        elif choice==1:
            jupiter.listStudents();

        elif choice==2:
            quit();

if __name__=="__main__":
    main();