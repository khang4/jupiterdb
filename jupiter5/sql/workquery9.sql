select max(verbal),max(quant),max(analytic),
min(verbal),min(quant),min(analytic),
stddev(verbal),stddev(quant),stddev(analytic),
degree_name,year from gre,application where 
gre.application_id=application.application_id
group by year,degree_name;
 
select min(verbal),min(quant),min(analytic),degree_name,year from gre,application
 where gre.application_id=application.application_id
 group by year,degree_name;
 
select stddev(verbal),stddev(quant),stddev(analytic),year from gre,application
 where gre.application_id=application.application_id
 group by year;

select verbal,quant,analytic,year,degree_name from gre,application
 where gre.application_id=application.application_id
 order by year;
