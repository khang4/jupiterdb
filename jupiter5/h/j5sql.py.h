class jupiter
{
    jupiter(string database);

    /*-- general sql --*/
    void add(string table,array-array-string values);
    void update(string table,string key,string id,string col,string value);
    void delRow(string table,string key,string id);
    int getLastId(string table,string primaryKey);

    /*-- applicants --*/
    array getApplicants();
}