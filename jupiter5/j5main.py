from j5sql import _jupiter;

jupiter=_jupiter("jupiter");

def main():
    # jupiter.add("bob",[["a",2,5,"asdasda","somewhere.com","bob tyhe weasle"]]);
    # jupiter.add("applicants",[[0,"big","john2","top mtn","snow lane",21312,"go","uloseboi@somewhere.com","g"]]);

    # jupiter.update("applicants","student_id",2,"first_name","big boi john");

    # jupiter.add("phone_number",[["9991231523",0],["1234567878",0],["5568951286",3],["123",1]]);

    jupiter.add("applicants",[[jupiter.getLastId("applicants","student_id")+1,"super",
        "johnboi","city place","nowhere ln","2021","aa","someerer@anopnpna/cp","a","1990-1-2"]]);

    print(promptDate(1));

#multiple chioce menu, give array of chioces
def menu(choices):
    for i,x in enumerate(choices):
        print("{}: {}".format(i,x));

    choice=int(input(">"));

    if choice<0 or choice>=len(choices):
        return menu(choices);

    return choice;

#prompt user for things in a date, returns a date string
#enterable into a sql query
#include time=1 to also prompt for time and return datetime string
#DOES NO ERROR CHECKING! if they entered something bad the sql will
#crash
def promptDate(time):
    datestr="";

    print("year:");
    datestr+=input(">");
    datestr+="-";

    print("month:");
    datestr+=input(">");
    datestr+="-"

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


if __name__=="__main__":
    main();