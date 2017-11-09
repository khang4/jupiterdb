create table if not exists jupiter.applicants
(
    student_id int not null,

    first_name varchar(20) not null,
    last_name varchar(20) not null,

    address_city varchar(20),
    address_street varchar(20),
    address_zip int,
    address_state char(2),

    email varchar(20),
    gender char(1),

    primary key (student_id)
);