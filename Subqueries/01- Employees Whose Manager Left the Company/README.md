# [Employees Whose Manager Left the Company](https://leetcode.com/problems/employees-whose-manager-left-the-company/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the <strong>IDs</strong> of the employees whose salary is <strong>strictly less than <code>$30000</code></strong> and whose manager <strong> left </strong> the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their <code>manager_id</code> set to the manager that left.

Return the result table ordered by <code> employee_id</code>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 
<details>
      <summary>Hint#1</summary>
      <p>How would you find what <code>ids</code> not in the Employees table ?</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>Use <span>WHERE IN<span> clause </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

this problem is simple, but the only catch is how would you filter the managers that left the company, since their information is deleted from the Employees table, but the reports still have their <code>manager_id</code> set to the manager that left.

so we need to find the <code>manager_id</code> that is not in the Employees table, and then we can use <code>WHERE IN</code> clause to filter the employees that have <code>manager_id</code> that is not in the Employees table.

</details>

<details>

<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select distinct employee_id
from Employees
where salary < 30000 and manager_id not in (select employee_id from Employees)
order by employee_id;


```

</details>
