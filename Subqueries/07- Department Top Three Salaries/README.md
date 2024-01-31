# [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the departments.

Return the result table in any order.

<!-- <details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>
<details>
      <summary>Hint#1-10</summary>
      <p>hint body goes here</p>
</details> -->
</details>
<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

This is a hard problem, we will break it down into pieces to make it easier to understand.

Of course, we will be doing some king of a subquery, but we will be using a window function to solve this problem.

We need to find the top three salaries for each department, we can do that by using the `DENSE_RANK()` function, which will rank the salaries in descending order for each department, and we will select only the top three salaries for each department.

Now let's see how we would break down the solution:

- First we need to join the `employee` table with the `department` table, so we can get the department name for each employee.

- Then we need to select the department name, employee name, and the salary for each employee.

- Then we need to rank the salaries for each department in descending order, and select only the top three salaries for each department.

</details>
<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select department, employee, salary
from (
    select
        d.name as department,
        e.name as employee,
        e.salary as salary,
        dense_rank() over (partition by d.name order by salary desc) AS rnk
    from employee e
    join department d
    on e.departmentId = d.id
) as rnk_tbl
where rnk <= 3;
```

</details>
