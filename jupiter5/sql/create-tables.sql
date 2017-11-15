create table if not exists jupiter.applicants
(
    student_id int not null,

    first_name varchar(30) not null,
    last_name varchar(30) not null,

    address_city varchar(20),
    address_street varchar(20),
    address_zip char(5),
    address_state char(2),

    email varchar(60),
    gender char(2),

    primary key (student_id)
);

create table if not exists jupiter.degree
(
    degree_name varchar(30),
    department varchar(30),
    director varchar(30),
    email varchar(30),
    phone_number varchar(12),

    primary key (degree_name)
);

create table if not exists jupiter.phone_number
(
    phone_number char(11) not null,
    student_id int not null,

    primary key (phone_number,student_id),

    foreign key (student_id) references jupiter.applicants (student_id) on delete cascade
);