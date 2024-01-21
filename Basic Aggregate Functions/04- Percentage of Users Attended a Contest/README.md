# [Percentage of Users Attended a Contest](https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the percentage of the users registered in each contest rounded to <strong>two decimals</strong>.

Return the result table ordered by <code>percentage</code> in <strong>descending order</strong>. In case of a tie, order it by <code>contest_id</code> in <strong>ascending order</strong>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>SQL has an aggregation function called <code>COUNT(expression)</code> which count all the rows that satisfy a specified condition</p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>Use <code>subquery</code></p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

To find the percentage of the users registered in each contest we should count the number of user that have registered into a contest and the total number of users then divide.
<br>
<br>
<ul>
    <li>
        calculate the number of users that registered in each contest using <code>COUNT()</code> function. 
    </li>
    <li>
        calculate the total number of user using <code>COUNT()</code> function as a <code><strong>sub query</strong></code>. By using <code>*</code> <i>(means all)</i> we can count the number of records in <code>Users</code> table. .
    </li>
    <li>
        divide both number and multiply them by <code>100</code> Then use <code>ROUND(number , decimals)</code> to round the result.
    </li>
</ul>
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    contest_id, 
    ROUND(
    COUNT(user_id)/(
        SELECT 
            COUNT(user_id) 
        FROM 
            Users
        )* 100
    , 2) AS percentage 
FROM 
  Register
GROUP BY 
  contest_id 
ORDER BY 
  percentage DESC, 
  contest_id
```

</details>