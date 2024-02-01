# [Primary Department for Each Employee](https://leetcode.com/problems/primary-department-for-each-employee/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is <span>'N'</span>.

Report all the employees with their <strong>primary department.</strong> For employees who belong to one department, report their only department.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>How would you filter employees belonging to many department? </p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>If an employee beglongs to more than one then it will be very easy to find him and his primary department as it will be marked with <code>primary_flag='Y'</code>
    </p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>How would you filter employees belonging to only one department?</p>
</details>

<details>
      <summary>Hint#4</summary>
      <p>Use subqueries :) </p>
</details>

<details>
      <summary>Hint#5</summary>
      <p>Use <code>WHERE IN</code> Clause </p>
</details>

<details>
      <summary>Hint#6</summary>
      <p>Joining the results will require as only a simple <code>OR</code> operator </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

The first step is to find all the employees who belong to more than one department. This can be done by checking if the <code>priamry_flag</code> is <code>'Y'</code> or not. If it is <code>'Y'</code> then it means that the employee belongs to more than one department and this is the primary department.

Then we have to find the rest of the employees who belong to only one department. This can be done by using a subquery. We can group the employees by their <code>employee_id</code> and then count the number of distinct departments they belong to. If the count is 1 then it means that the employee belongs to only one department.

Now we have to join the results of the two queries. This can be done by using a simple <code>OR</code> operator.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select e.employee_id ,e.department_id from employee e
where e.primary_flag='Y' or e.employee_id in
(select employee_id from employee group by employee_id having count(distinct department_id)=1);
```

</details>
