# [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the second highest salary from the <code>Employee</code> table. If there is no second highest salary, return <code>null (return None in Pandas)</code>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>hint body goes here</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

Explanation goes here.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql

select
(select distinct Salary
from Employee order by salary desc
limit 1 offset 1)
as SecondHighestSalary;


```

</details>
