# [Project Employees I](https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Report the <code>average</code> experience years of all the employees for each project, <strong> rounded to 2 digits</strong>.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>When we have more than one tables we must think about joins first</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>SQL has a function <code>AVG(column_name)</code> returns the average value of that column </p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>Here we are asked to find the average for each project, we must think about <strong>Grouping</strong>  </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

We want to find the average experience years for each project, so we must join the two tables on the <code>employee_id</code> column, then we must group the result by the <code>project_id</code> column, and finally we must find the average of the <code>experience_years</code> column.

When selecting the average of a column we must use the <code>AVG(column_name)</code> function, and to round the result to 2 digits we must use the <code>ROUND()</code> function, then we use <code>AS</code> to give the column an alias (<code>average_years</code>)

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select p.project_id, round(avg(e.experience_years),2)  as average_years
from Project p
inner join Employee e on e.employee_id = p.employee_id
group by p.project_id;
```

</details>
