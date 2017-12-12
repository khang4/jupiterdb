/* query 1 */
select distinct last_name,first_name from applicants,application where degree_name="whale studies" and applicants.student_id=application.student_id and year="2019" and semester="spring";

/* query 2 */
select count(student_id),degree_name,semester,year from application group by degree_name,semester,year;

/* query 3 */
select count(major) majorcount,major from education where year(grad_date)="2015" group by major order by majorcount desc limit 1;

/* query 4 */
select last_name,first_name,gpa from applicants,
(select student_id,gpa
from application,
(select application_id,gpa from education where gpa=(select min(gpa) from education)) as mingpa
where application.application_id=mingpa.application_id and application.decision="accepted" and year(application.decision_date)=year(curdate()) and semester="spring") as mingpa where
applicants.student_id=mingpa.student_id;

/* query 5 */
select count(application.application_id),degree_name,major from application,education where application.application_id=education.application_id group by degree_name,major;

/* query 6 */
select application_id from application where eval_date<"2000-01-01";

/* query 7 */
select count(application_id),decision,degree_name,year from application group by decision,degree_name,year;

/* query 8 */
select acceptences,referencer from
(select count(referencer) acceptences,referencer from email,application where email.application_id=application.application_id and decision="accepted" group by referencer) as acceptenceCount,
(select max(acceptences) maxacceptences from (select count(referencer) acceptences,referencer from email,application where email.application_id=application.application_id and decision="accepted" group by referencer) acceptenceCount) as maxacceptences
where acceptenceCount.acceptences=maxacceptences.maxacceptences;

/* query 9 */

/* query 10 */
select collegecountmax.collegecountmax,college from
(select count(application_id) as collegecount,college from education where year(grad_date)>year(curdate())-5 group by college) as collegecount,
(select max(collegecount.collegecount) as collegecountmax from (select count(application_id) collegecount,college from education where year(grad_date)>year(curdate())-5 group by college) as collegecount) as collegecountmax
where collegecount.collegecount=collegecountmax.collegecountmax;