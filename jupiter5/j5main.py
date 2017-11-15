from j5sql import _jupiter;

jupiter=_jupiter("jupiter");

def main():
    jupiter.add("bob",["a",2,5,"asdasda","somewhere.com","bob tyhe weasle"]);

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