# [Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Show the unique ID of each user, If a user does not have a unique ID replace just show <code>null</code>.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>Use <code>OUTER JOIN</code></p>
</details>
<details>
      <summary>Hint#2</summary>
      <p><code>JOIN ON</code>  ID</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>
We want for every <code>Employee</code> to retrieve tha matching <code>unique_ids</code>.
<br> 
With the help of <code>JOINS</code> we can retrieve data from multiple tables but which one <code>INNER JOIN</code> or <code>OUTER JOIN</code>.
<br>
The answer is <code>OUTER JOIN</code> because if the <code>name</code> does not have any <code>unique_id</code>  we still need to retrieve it with <code>NULL</code> <code>unique_id</code>.
<br>
SO we will <code>JOIN</code> Employees table with EmployeeUNI table <code>ON</code> <code>id</code>.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    EmployeeUNI.unique_id,
    Employees.name
FROM
    Employees
LEFT OUTER JOIN EmployeeUNI ON EmployeeUNI.id = Employees.id
;
```

</details>