class jupiter
{
    jupiter(string database);

    connection connection;
    cursor cursor;

    /*-- general sql --*/
    //add,update,delrow return 1 on success, 0 on fail
    int add(string table,array-array-string values);
    int update(string table,string|string-array key,
        string|string-array id,string col,string value);
    int delRow(string table,string|string-array key,string|string-array id);

    int getLastId(string table,string primaryKey);

    /*-- main getters --*/
    array getApplicants();
    array getDegrees();
    array getStudent(int id);
    array getPhones(int id);
    array getDegree(string name);
    array getReqs(string name);
    array getAnswers(int reqId);
    array getApplications(int student);
    array getApplicationDetail(int appid);
    array getEducations(int appid);
    array getEmails(int appid);
    object getAppAnswers(int appid);
    array getCriteria(string degreeName);
    array getScores(int critId); //get all possible scores for a criteria (NOT actual scores)
    string getEssay(int appid);
    array getAppScores(int appid);
    array getEvaluators(int appid);

    /*-- required queries --*/
    array studentsearchDegree(string degree,string semester,int year);
    array studentsPerDegree();
    array mostPopularMajor();
    array acceptedLowestGpa();
}

/*-- utility --*/
string genPrimaryWhere(string key,string id);
string genPrimaryWhere(string-array key,string-array id);