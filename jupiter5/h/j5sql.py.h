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

    /*-- applicants --*/
    array getApplicants();
    array getDegrees();
    array getStudent(int id);
    array getPhones(int id);
    array getDegree(string name);
    array getReqs(string name);
    array getAnswers(int reqId);
    array getApplications(int student);
    array getApplicationDetail(int appid);
}

/*-- utility --*/
string genPrimaryWhere(string key,string id);
string genPrimaryWhere(string-array key,string-array id);