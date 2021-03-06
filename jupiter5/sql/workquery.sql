select * from requirement;
select * from appAnswer;
drop table criteria;

select * from criteria_score;
select * from criteria;
select * from application;
select * from evaluation_score;
select * from education;

select * from application,applicants where application.student_id=applicants.student_id;
/*query 1*/
select distinct last_name,first_name from applicants,application where degree_name="whale studies" and applicants.student_id=application.student_id and year="2019" and semester="spring";

/*query 2*/
select count(student_id),degree_name,semester,year from application group by degree_name,semester,year;

/*query 3*/
select count(major) majorcount,major from education where year(grad_date)="2015" group by major order by majorcount desc limit 1;

select major,grad_date from education;
select count(major) as majorcount,major from education group by major order by majorcount desc limit 1;

select count(major) majorcount,major from education where year(grad_date)="2015" group by major order by majorcount desc limit 1;

select min(gpa) from education;
select application_id,gpa from education where gpa=(select min(gpa) from education);

/*query 4:*/
select last_name,first_name,gpa from applicants,
(select student_id,gpa
from application,
(select application_id,gpa from education where gpa=(select min(gpa) from education)) as mingpa
where application.application_id=mingpa.application_id and application.decision="accepted" and year(application.decision_date)=year(curdate()) and month(application.decision_date)>=1 and month(application.decision_date)<=6) as mingpa where
applicants.student_id=mingpa.student_id;

select gpa,decision_date from education,application
where education.application_id=application.application_id;

select min(gpa) mingpa from education,application
where education.application_id=application.application_id
and decision="accepted" and year(decision_date)=year(curdate())
and month(decision_date)<=6;

select mingpa,last_name,first_name from
(select last_name,first_name,gpa,decision_date from education,application,applicants
where education.application_id=application.application_id
and application.student_id=applicants.student_id
and decision="accepted" and year(decision_date)=year(curdate())
and month(decision_date)<=6) as periodgpas,
(select min(gpa) mingpa from education,application
where education.application_id=application.application_id
and decision="accepted" and year(decision_date)=year(curdate())
and month(decision_date)<=6) as mingpa
where periodgpas.gpa=mingpa.mingpa;

select * from application;

/*query 5*/
select count(application.application_id),degree_name,major from application,education where application.application_id=education.application_id group by degree_name,major;

/*query 6*/
select application_id from application where eval_date<"2000-01-01";

select * from application;

/*query 7*/
select count(application_id),decision,degree_name,year from application group by decision,degree_name,year;

/*query 8*/
select acceptences,referencer from
(select count(referencer) acceptences,referencer from email,application where email.application_id=application.application_id and decision="accepted" group by referencer) as acceptenceCount,
(select max(acceptences) maxacceptences from (select count(referencer) acceptences,referencer from email,application where email.application_id=application.application_id and decision="accepted" group by referencer) acceptenceCount) as maxacceptences
where acceptenceCount.acceptences=maxacceptences.maxacceptences;

(select count(referencer) acceptences,referencer from email,application where email.application_id=application.application_id and decision="accepted" group by referencer);


(select max(acceptences) from (select count(referencer) acceptences,referencer from email,application where email.application_id=application.application_id and decision="accepted" group by referencer) acceptenceCount);




/*9*/
select max(verbal),max(quant),max(analytic),
min(verbal),min(quant),min(analytic),
stddev(verbal),stddev(quant),stddev(analytic),
degree_name,year from gre,application where
gre.application_id=application.application_id
group by year,degree_name;


select * from education;
select count(application_id) collegecount,college from education where year(grad_date)>year(curdate())-5 group by college;

/*10*/
select collegecountmax.collegecountmax,college from
(select count(application_id) as collegecount,college from education where year(grad_date)>year(curdate())-5 group by college) as collegecount,
(select max(collegecount.collegecount) as collegecountmax from (select count(application_id) collegecount,college from education where year(grad_date)>year(curdate())-5 group by college) as collegecount) as collegecountmax
where collegecount.collegecount=collegecountmax.collegecountmax;

select count(application_id) as collegecount,college from education where year(grad_date)>year(curdate())-5 group by college;










