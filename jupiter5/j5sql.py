import mysql.connector;
import datetime;

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

    def getApplications(self,student):
        try:
            self.cursor.execute('''select degree_name,semester,year,application_id from application where student_id="{}"'''.format(student));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getApplicationDetail(self,appid):
        try:
            self.cursor.execute('''select degree_name,semester,year from application where application_id="{}"'''.format(appid));
            return self.cursor.fetchone();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getEducations(self,appid):
        try:
            self.cursor.execute('''select education_id,college,major,degree,grad_date,gpa from education where application_id="{}"'''.format(appid));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getEmails(self,appid):
        try:
            self.cursor.execute('''select email_id,referencer,body from email where application_id="{}"'''.format(appid));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getGres(self,appid):
        try:
            self.cursor.execute('''select gre_id,verbal,quant,analytic,taken from gre where application_id="{}"'''.format(appid));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #returns DICT of answers, key is REQUIREMENT ID of the answer, to match up with REQUIREMENT ID
    def getAppAnswers(self,appid):
        try:
            self.cursor.execute('''select requirement_id,answer from appAnswer where application_id="{}"'''.format(appid));
            answers=self.cursor.fetchall();
            aObj={};
            for x in answers:
                aObj[x[0]]=x[1];

            return aObj;

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getCriteria(self,degreeName):
        try:
            self.cursor.execute('''select criteria_id,criteria_text from criteria where degree_name="{}"'''.format(degreeName));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getScores(self,critId):
        try:
            self.cursor.execute('''select score_id,score_text,score_condition from criteria_score where criteria_id="{}"'''.format(critId));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getEssay(self,appid):
        try:
            self.cursor.execute('''select essay from application where application_id="{}"'''.format(appid));
            return self.cursor.fetchone()[0];

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getEvalDetails(self,appid):
        try:
            self.cursor.execute('''select decision,eval_date,decision_date from application where application_id="{}"'''.format(appid));
            return self.cursor.fetchone();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    def getAppScores(self,appid):
        try:
            self.cursor.execute('''select evaluation_score.criteria_id,evaluation_score.score_id,score_text from evaluation_score,criteria_score where application_id="{}" and evaluation_score.score_id=criteria_score.score_id and evaluation_score.criteria_id=criteria_score.criteria_id'''.format(appid));
            scores=self.cursor.fetchall();
            res={};
            for x in scores:
                res[x[0]]=x;
            return res;

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #get all evaluators for an application
    def getEvaluators(self,appid):
        try:
            self.cursor.execute('''select evaluator_id,name from evaluator where application_id="{}"'''.format(appid));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;
    #q1
    def studentsearchDegree(self,degree,year="",semester=""):
        whereString=[];
        if degree and degree!="":
            whereString.append('''degree_name="{}"'''.format(degree));

        if year and year!="":
            whereString.append('''year="{}"'''.format(year));

        if semester and semester!="":
            whereString.append('''semester="{}"'''.format(semester));

        whereString=" and ".join(whereString);

        try:
            self.cursor.execute('''select last_name,first_name from applicants,application where applicants.student_id=application.student_id and {}'''.format(whereString));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #q2
    def studentsPerDegree(self):
        try:
            self.cursor.execute('''select count(student_id),degree_name,semester,year from application group by degree_name,semester,year''');
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #q3
    def mostPopularMajor(self,year):
        try:
            self.cursor.execute('''select count(major) majorcount,major from education where
                year(grad_date)="{}" group by major order by majorcount desc limit 1'''
                .format(year));
            return self.cursor.fetchone();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #q4
    def minGpaPeriod(self):
        monthrange=datetime.date.today().month;

        if monthrange<=6:
            monthrange='<=6';
        else:
            monthrange='>=7';

        try:
            self.cursor.execute('''select mingpa,last_name,first_name from
                (select last_name,first_name,gpa,decision_date from education,application,applicants
                where education.application_id=application.application_id
                and application.student_id=applicants.student_id
                and decision="accepted" and year(decision_date)=year(curdate())
                and month(decision_date){}) as periodgpas,
                (select min(gpa) mingpa from education,application
                where education.application_id=application.application_id
                and decision="accepted" and year(decision_date)=year(curdate())
                and month(decision_date){}) as mingpa
                where periodgpas.gpa=mingpa.mingpa;
                '''.format(monthrange,monthrange));
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #q5
    def degreeByMajor(self):
        try:
            self.cursor.execute('''select count(application.application_id),degree_name,major from application,education where application.application_id=education.application_id group by degree_name,major''');
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #q6
    def unevaluated(self):
        try:
            self.cursor.execute('''select application_id from application where eval_date<"2000-01-01"''');
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #q7
    def decisionsCounts(self):
        try:
            self.cursor.execute('''select count(application_id),decision,degree_name,year from application group by decision,degree_name,year''');
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #q8
    def acceptenceEmails(self):
        try:
            self.cursor.execute('''select acceptences,referencer from (select count(referencer) acceptences,referencer from email,application where email.application_id=application.application_id and decision="accepted" group by referencer) as acceptenceCount,(select max(acceptences) maxacceptences from (select count(referencer) acceptences,referencer from email,application where email.application_id=application.application_id and decision="accepted" group by referencer) acceptenceCount) as maxacceptences where acceptenceCount.acceptences=maxacceptences.maxacceptences''');
            return self.cursor.fetchall();

        except mysql.connector.Error as err:
            print(err);
            return 0;

    #q10
    def mostAttend(self):
        try:
            self.cursor.execute('''select collegecountmax.collegecountmax,college from (select count(application_id) as collegecount,college from education where year(grad_date)>year(curdate())-5 group by college) as collegecount,(select max(collegecount.collegecount) as collegecountmax from (select count(application_id) collegecount,college from education where year(grad_date)>year(curdate())-5 group by college) as collegecount) as collegecountmax where collegecount.collegecount=collegecountmax.collegecountmax''');
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