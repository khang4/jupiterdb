from j5sql import _jupiter;

jupiter=_jupiter("jupiter");

def main():
    # jupiter.add("bob",[["a",2,5,"asdasda","somewhere.com","bob tyhe weasle"]]);
    # jupiter.add("applicants",[[0,"big","john2","top mtn","snow lane",21312,"go","uloseboi@somewhere.com","g"]]);

    # jupiter.update("applicants","student_id",2,"first_name","big boi john");

    # jupiter.add("phone_number",[["9991231523",0],["1234567878",0],["5568951286",3],["123",1]]);

    print(jupiter.getLastId("applicants","student_id"));

#multiple chioce menu, give array of chioces
def menu(choices):
    for i,x in enumerate(choices):
        print("{}: {}".format(i,x));

    choice=int(input(">"));

    if choice<0 or choice>=len(choices):
        return menu(choices);

    return choice;

if __name__=="__main__":
    main();