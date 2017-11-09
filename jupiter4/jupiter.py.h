class jupiter
{
    //modifiable applicant columns
    string-array studentCols;

    //takes size 8 array of student values
    void addStudent(array student);
    //show all student objects
    void listStudents();

    //prompt user to change single entry
    void modifyEntry(string table,string pkey,string-array prompts,string-array colArray);

  private:
    connection connection;
    cursor cursor;

    int cStudentId; //current student id

    void loadIdCounters(); //initialise id counters
}