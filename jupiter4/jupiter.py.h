class jupiter
{
    //takes size 8 array of student values
    void addStudent(array student);
    //show all student objects
    void listStudents();

  private:
    connection connection;
    cursor cursor;

    int cStudentId; //current student id

    void loadIdCounters(); //initialise id counters
}