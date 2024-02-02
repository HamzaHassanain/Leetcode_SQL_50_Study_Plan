# [The Number of Employees Which Report to Each Employee](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by <code>employee_id</code>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p><code>JOIN</code> the table with itself</p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>Consider the first table as <code>Managers</code> and the second one as <code>Employees</code></p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>Use <code>INNER JOIN</code></p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

We are required to perform a <code>self-JOIN</code> on the Employees table.

Let's designate the first instance of the table as the "Manager" and the second instance as the <code>"Employee"</code> who is being managed.

For the linkage, we'll use the condition where the <code>employee_id</code> in the first table matches the <code>reports_to</code> in the second table <code>(first_table.employee_id = second_table.reports_to)</code>.

As mentioned to retrieve information on all <code>managers</code>, we will employ an <code>INNER JOIN</code>, as managers must have at least one employee reporting to them.

Lastly, we will utilize the <code>AVG()</code> function to compute the average and then apply the <code>ROUND()</code> function to round the result.
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    a.employee_id, 
    a.name, 
    count(b.reports_to) AS reports_count, 
    ROUND(
        AVG(b.age)
    ) AS average_age 
FROM 
    Employees a 
    INNER JOIN Employees b ON a.employee_id = b.reports_to 
GROUP BY 
    a.employee_id 
ORDER BY 
    a.employee_id
-- ROUND(something , 0) by default
```

</details>