# [Employee Bonus](https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Report the name and bonus amount of each employee with a bonus less than <code>1000</code>. If there is no bonus for an employee, the bounce should be reported as <code>NULL</code>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>Use Joins</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p> Join on <code>empId</code></p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>We should be using <code>LEFT JOIN</code> (Employee table be the left one) </p>
</details>

<details>
      <summary>Hint#4</summary>
      <p>You can use <code>IS NULL</code> to check if the value is null</p>
</details>

</details>
<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

We are asked to select the name and bonus amount of each employee with a bonus less than <code>1000</code>. If there is no bonus for an employee, the bounce should be reported as <code>NULL</code>.

First We must use a left join to make sure that every record in the Employee table is included in the result set and if there is no matching bounce (No mathcing <code>Bouns.empId</code> for a specific <code>Employee.empId</code>) in the Bonus table, the bounce will be set to <code>NULL</code>.

Now to the where clause, we must select the records with a bonus less than <code>1000</code> or the records with a <code>NULL</code> bonus.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
SELECT Employee.name, Bonus.bonus  FROM Employee
LEFT JOIN Bonus
ON Employee.empId = Bonus.empId
WHERE Bonus.bonus < 1000 OR Bonus.bonus IS NULL;
```

</details>
