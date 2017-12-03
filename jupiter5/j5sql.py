import mysql.connector;

class _jupiter:
    #construct by giving name of database to connect to
    def __init__(self,database):
        self.connection=mysql.connector.connect(user="root",password="",host="127.0.0.1",database=database);
        self.cursor=self.connection.cursor();

    #GENERAL sql add function
    #give it table name to add to and array of arrays of values, it will add each
    #array in values as a seperate row
    def add(self,table,values):
        if not isinstance(values[0],list):
            values=[values];

        valuestring="";
        for iy,y in enumerate(values):
            valuestring+="(";

            for ix,x in enumerate(y):
                valuestring+='''"{}"'''.format(x);

                if not ix==len(y)-1:
                    valuestring+=",";

            valuestring+=")";

            if not iy==len(values)-1:
                valuestring+=",";

        try:
            self.cursor.execute('''insert into {} values {}'''.format(table,valuestring));
            self.connection.commit();

        except mysql.connector.Error as err:
            print(err);
            return 0;

        return 1;

    #GENERAL sql update function
    #give it table name, primary key to match with id, col to change and new value to put in
    #key and id can both be arrays OF THE SAME SIZE to allow it to updadte tables
    #with multi-primary key (like phone numbers)
    def update(self,table,key,id,col,value):
        whereString=genPrimaryWhere(key,id);

        try:
            self.cursor.execute('''update {} set {}="{}" where {}'''.format(
                table,col,value,whereString
            ));
            self.connection.commit();

        except mysql.connector.Error as err:
            print(err);
            return 0;

        return 1;

    #general sql delete a row. give it table name, primary key, and the
    #value of the primary key of the row to delete
    def delRow(self,table,key,id):
        whereString=genPrimaryWhere(key,id);
        try:
            self.cursor.execute('''delete from {} where {}'''.format(table,whereString));
            self.connection.commit();

        except mysql.connector.Error as err:
            print(err);
            return 0;

        return 1;

    #return the highest id value of the given table and correct
    #primary key for that table, only applicable FOR TABLES that
    #HAVE INTEGER IDS FOR PRIMARY KEY!!!!!
    def getLastId(self,table,primaryKey):
        try:
            self.cursor.execute("select max({}) from {}".format(primaryKey,table));

            for x in self.cursor:
                if not x[0]:
                    return 0;

                return x[0];

        except mysql.connector.Error as err:
            print(err);
            return -1;

    #returns list of all applicants with last name, first name and student id
    def getApplicants(self):
        try:
            self.cursor.execute("select student_id,last_name,first_name from applicants");
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return [];

    #get names of degree programs
    def getDegrees(self):
        try:
            self.cursor.execute("select degree_name from degree");
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return [];

    def getStudent(self,id):
        try:
            self.cursor.execute('''select * from applicants where student_id="{}"'''.format(id));
            return self.cursor.fetchone();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getPhones(self,id):
        try:
            self.cursor.execute('''select phone_number from phone_number where student_id="{}"'''.format(id));
            res=[];
            for x in self.cursor:
                res.append(x[0]);
            return res;

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getDegree(self,name):
        try:
            self.cursor.execute('''select degree_name,department,director,email,phone_number from degree where degree_name="{}"'''.format(name));
            return self.cursor.fetchone();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getReqs(self,name):
        try:
            self.cursor.execute('''select requirement_id,question from requirement where degree_name="{}"'''.format(name));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #give requirement id, get array of answers
    def getAnswers(self,reqId):
        try:
            self.cursor.execute('''select answer_id,answer from answer where requirement_id="{}"'''.format(reqId));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

#assemble key names from array key to strings from ids with ANDS
#useful for matching primary keys
def genPrimaryWhere(key,id):
    whereString="";
    if isinstance(key,list):
        for ix,x in enumerate(key):
            whereString+='''{}="{}"'''.format(x,id[ix]);

            if not ix==len(key)-1:
                whereString+=" and ";

    else:
        whereString='''{}="{}"'''.format(key,id);

    return whereString;