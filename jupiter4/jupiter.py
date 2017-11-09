import mysql.connector;

class _jupiter:
    def __init__(self,database):
        self.connection=mysql.connector.connect(user="root",password="",host="127.0.0.1",database=database);
        self.cursor=self.connection.cursor();

        self.cStudentId=0;

        self.loadIdCounters();

    def loadIdCounters(self):
        self.cursor.execute("select max(student_id) from applicants");
        self.cStudentId=self.cursor.fetchone()[0];

    def addStudent(self,student):
        self.cursor.execute("insert into applicants values ({},'{}','{}','{}','{}',{},'{}','{}','{}')".format(self.cStudentId+1,student[0],student[1],student[2],student[3],student[4],student[5],student[6],student[7]));
        self.cStudentId+=1;
        self.connection.commit();

    def listStudents(self):
        self.cursor.execute("select * from applicants");
        for x in self.cursor:
            print(x);