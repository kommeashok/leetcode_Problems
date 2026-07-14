# Write your MySQL query statement below
select
name as NAME,sum(amount) as BALANCE
from 
users as u
left join 
transactions as t
on u.account=t.account
GROUP BY
name
having 
sum(amount)>10000;
