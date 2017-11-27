class jupiter
{
    jupiter(string database);

    connection connection;
    cursor cursor;

    /*-- general sql --*/
    //add,update,delrow return 1 on success, 0 on fail
    int add(string table,array-array-string values);
    int update(string table,string key,string id,string col,string value);
    int delRow(string table,string key,string id);

    int getLastId(string table,string primaryKey);

    /*-- applicants --*/
    array getApplicants();
    array getDegrees();
    array getStudent(int id);
    array getPhones(int id);
}