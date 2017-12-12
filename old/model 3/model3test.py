import mysql.connector;

class jupiter:
    def __init__(self,database):
        self.connection=mysql.connector.connect(user="root",password="",host="127.0.0.1",database=database);
        self.cursor=self.connection.cursor();

    def addApplicant(self,id,first,last,address,email,bday,gender):
        self.cursor.execute("insert into applicant (student_id,first_name,last_name) values ({},'{}','{}')".format(id,first,last));
        self.connection.commit();

    def viewApplicants(self):
        self.cursor.execute("select * from applicant");
        for x in self.cursor:
            print(x);

def main():
    jupdb=jupiter("juptier");

    # jupdb.addApplicant(0,"bob","bill","1000 somewhere street","asd@a.com","2010-10-02","m");
    jupdb.viewApplicants();

if __name__=="__main__":
    main();