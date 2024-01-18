# [Employee Bonus](https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Report the name and bonus amount of each employee with a bonus less than 1000. If there is no bonus for an employee, the bounce should be reported as 'NULL'.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>Use Joins</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p> Join on empId</p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>We should be using LEFT JOIN (Employee table be the left one) </p>
</details>

<details>
      <summary>Hint#4</summary>
      <p>You can use IS NULL to check if the value is null</p>
</details>

</details>
<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>


We are asked to select the name and bonus amount of each employee with a bonus less than 1000. If there is no bonus for an employee, the bounce should be reported as 'NULL'.

First We must use a left join to make sure that every record in the Employee table is included in the result set and if there is no matching bounce (No mathcing Bouns.empId for a specific Employee.empId) in the Bonus table, the bounce will be set to null.

Now to the where clause, we must select the records with a bonus less than 1000 or the records with a null bonus.

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
