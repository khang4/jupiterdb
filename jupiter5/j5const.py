from j5main import jupiter;

#[table name,table key name]
tableinfo=[
    {"name":"applicants","primary_key":"student_id"},
    {"name":"degree","primary_key":"degree_name"}
];

tableMaxKeys={
    "applicants":jupiter.getLastId("applicants","student_id")
};