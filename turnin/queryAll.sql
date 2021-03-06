/* query 1 */
/* sample input for this query:
    degree: whale studies
    year: 2019
    semester: spring*/
select distinct last_name,first_name from applicants,
application where degree_name="whale studies" and
applicants.student_id=application.student_id and
year="2019" and semester="spring";

/* query 2 */
select count(student_id),degree_name,semester,year
from application group by degree_name,semester,year;

/* query 3
   sample input for this query:
   year: 2015*/
select count(major) majorcount,major from education where
year(grad_date)="2015" group by major order by majorcount desc limit 1;

/* query 4
   this query requires the program to specify
   the current semester, which is determined not
   by the string "fall" or "spring", but month
   >=6 or >6. The sample semester-month-range for
   this query is >=6, so the fall semester (now).
   When using the program the program will automatically
   determine this.*/
select mingpa,last_name,first_name from
(select last_name,first_name,gpa,decision_date from education,application,applicants
where education.application_id=application.application_id
and application.student_id=applicants.student_id
and decision="accepted" and year(decision_date)=year(curdate())
and month(decision_date)>=6) as periodgpas,
(select min(gpa) mingpa from education,application
where education.application_id=application.application_id
and decision="accepted" and year(decision_date)=year(curdate())
and month(decision_date)>=6) as mingpa
where periodgpas.gpa=mingpa.mingpa;

/* query 5 */
select count(application.application_id),degree_name,major
from application,education where
application.application_id=education.application_id
group by degree_name,major;

/* query 6 */
select application_id from application where eval_date<"2000-01-01";

/* query 7 */
select count(application_id),decision,degree_name,year
from application group by decision,degree_name,year;

/* query 8 */
select acceptences,referencer from
(select count(referencer) acceptences,referencer from email,application
where email.application_id=application.application_id and decision="accepted"
group by referencer) as acceptenceCount,
(select max(acceptences) maxacceptences from (select count(referencer)
acceptences,referencer from email,application where
email.application_id=application.application_id and
decision="accepted" group by referencer) acceptenceCount) as maxacceptences
where acceptenceCount.acceptences=maxacceptences.maxacceptences;

/* query 9 */
select max(verbal),max(quant),max(analytic),
min(verbal),min(quant),min(analytic),
stddev(verbal),stddev(quant),stddev(analytic),
degree_name,year from gre,application where
gre.application_id=application.application_id
group by year,degree_name;

/* query 10 */
select collegecountmax.collegecountmax,college from
(select count(application_id) as collegecount,college from education
where year(grad_date)>year(curdate())-5 group by college) as collegecount,
(select max(collegecount.collegecount) as collegecountmax from
(select count(application_id) collegecount,college from education
where year(grad_date)>year(curdate())-5 group by college) as collegecount)
as collegecountmax where collegecount.collegecount=collegecountmax.collegecountmax;