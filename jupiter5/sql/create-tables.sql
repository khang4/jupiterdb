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

    birthday date,

    primary key (student_id)
);

create table if not exists jupiter.degree
(
    degree_name varchar(30),
    department varchar(30),
    director varchar(30),
    email varchar(30),
    phone_number varchar(12),

    rubric_document varchar(800),

    primary key (degree_name)
);

create table if not exists jupiter.phone_number
(
    phone_number char(11) not null,
    student_id int not null,

    primary key (phone_number,student_id),

    foreign key (student_id) references jupiter.applicants (student_id) on delete cascade
);

create table if not exists jupiter.requirement
(
    requirement_id int not null,
    degree_name varchar(30) not null,
    question varchar(180),

    primary key (requirement_id),
    foreign key (degree_name) references jupiter.degree (degree_name) on delete cascade
);

create table if not exists jupiter.answer
(
    answer_id int not null,
    requirement_id int not null,
    answer varchar(280),

    primary key (answer_id,requirement_id),
    foreign key (requirement_id) references jupiter.requirement (requirement_id) on delete cascade
);

create table if not exists jupiter.criteria
(
    criteria_name varchar(30) not null,
    degree_name varchar(30) not null,
    criteria_description varchar(150),

    primary key (criteria_name,degree_name),
    foreign key (degree_name) references jupiter.degree (degree_name) on delete cascade
);

create table if not exists jupiter.application
(
    application_id int not null,
    degree_name varchar(30),
    student_id int not null,

    essay varchar(1500),

    semester char(6),
    year int,

    primary key (application_id),
    foreign key (degree_name) references jupiter.degree (degree_name) on delete cascade,
    foreign key (student_id) references jupiter.applicants (student_id) on delete cascade
);