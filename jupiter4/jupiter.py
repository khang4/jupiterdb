import mysql.connector;

class _jupiter:
    def __init__(self,database):
        self.connection=mysql.connector.connect(user="root",password="",host="127.0.0.1",database=database);
        self.cursor=self.connection.cursor();

        self.tableNames=["applicants"];

        self.cStudentId=0;
        self.studentCols=["first name","last name","city","street","zip","state","email","gender"];
        self.a_studentCols=["first_name","last_name","address_city","address_street","address_zip","address_state","email","gender"];

        self.loadIdCounters();

    def loadIdCounters(self):
        self.cursor.execute("select max(student_id) from applicants");
        self.cStudentId=self.cursor.fetchone()[0];

    #give array of values to prompt user, returns array of answers
    def addStudent(self,student):
        self.cursor.execute("insert into applicants values ({},'{}','{}','{}','{}',{},'{}','{}','{}')".format(self.cStudentId+1,student[0],student[1],student[2],student[3],student[4],student[5],student[6],student[7]));
        self.cStudentId+=1;
        self.connection.commit();

    def listStudents(self):
        self.cursor.execute("select * from applicants");
        for x in self.cursor:
            print(x);

    #   table: name of table in database that will be modified
    #   pkey: primary key of table being modified
    #   prompts: prompts of column names to be shown to user, tells them what
    #       can be changed
    #   colActual: array of actual column names so function can make database call
    def modifyEntry(self,table,pkey,prompts,colActual):
        print("\nid to modify:");
        modid=int(input(">"));

        print("select field to modify:");
        for i,x in enumerate(prompts):
            print("{}: {}".format(i,x));
        modfield=int(input(">"));

        print("\nnew value:");
        newvalue=input(">");

        self.cursor.execute("update {} set {}='{}' where {}='{}'".format(table,colActual[modfield],newvalue,pkey,modid));
        self.connection.commit();
