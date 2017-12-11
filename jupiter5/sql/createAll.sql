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
    question varchar(200),

    primary key (requirement_id),
    foreign key (degree_name) references jupiter.degree (degree_name) on delete cascade
);

create table if not exists jupiter.answer
(
    answer_id int not null,
    requirement_id int not null,
    answer varchar(300),

    primary key (answer_id,requirement_id),
    foreign key (requirement_id) references jupiter.requirement (requirement_id) on delete cascade
);

create table if not exists jupiter.criteria
(
    criteria_id int not null,
    degree_name varchar(30) not null,

    criteria_text varchar(400),

    primary key (criteria_id),
    foreign key (degree_name) references jupiter.degree (degree_name) on delete cascade
);

create table if not exists jupiter.criteria_score
(
    score_id int not null,
    criteria_id int not null,

    score_text varchar(80),
    score_condition varchar(300),

    primary key (score_id,criteria_id),
    foreign key (criteria_id) references jupiter.criteria (criteria_id) on delete cascade
);

create table if not exists jupiter.application
(
    application_id int not null,
    degree_name varchar(30),
    student_id int not null,

    essay varchar(2000),

    semester char(6),
    year int,

    decision char(10),
    eval_date date,
    decision_date date,

    primary key (application_id),
    foreign key (degree_name) references jupiter.degree (degree_name) on delete cascade,
    foreign key (student_id) references jupiter.applicants (student_id) on delete cascade
);

create table if not exists jupiter.appAnswer
(
    application_id int not null,
    requirement_id int not null,

    answer varchar(800),

    primary key (application_id,requirement_id),
    foreign key (application_id) references jupiter.application (application_id) on delete cascade,
    foreign key (requirement_id) references jupiter.requirement (requirement_id) on delete cascade

);

create table if not exists jupiter.education
(
    education_id int not null,
    application_id int not null,

    college varchar(20),
    major varchar(20),
    degree char(2),
    grad_date date,
    gpa float,

    check (gpa >=0 and gpa<=4),

    primary key (education_id,application_id),
    foreign key (application_id) references jupiter.application (application_id) on delete cascade
);

create table if not exists jupiter.email
(
    email_id int not null,
    application_id int not null,

    referencer varchar(20),
    body varchar(2000),

    primary key (email_id,application_id),
    foreign key (application_id) references jupiter.application (application_id) on delete cascade
);

create table if not exists jupiter.gre
(
    gre_id int not null,
    application_id int not null,

    verbal int,
    quant int,
    analytic float,

    taken date,

    primary key (gre_id,application_id),
    foreign key (application_id) references jupiter.application (application_id) on delete cascade
);

create table if not exists jupiter.evaluation_score
(
    score_id int not null,
    criteria_id int not null,
    application_id int not null,

    primary key (criteria_id,application_id),
    foreign key (score_id) references jupiter.criteria_score (score_id) on delete cascade,
    foreign key (criteria_id) references jupiter.criteria (criteria_id) on delete cascade,
    foreign key (application_id) references jupiter.application (application_id) on delete cascade
);

create table if not exists jupiter.evaluator
(
    evaluator_id int not null,
    application_id int not null,

    name varchar(30),

    primary key (evaluator_id,application_id),
    foreign key (application_id) references jupiter.application (application_id) on delete cascade
);