# [User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the daily active user count for a period of <code>30</code> days ending <code>2019-07-27</code> inclusively. A user was active on someday if they made at least one activity on that day.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>SQL has an aggregation function called <code>COUNT(expression)</code> which count all the rows that satisfy a specified condition</p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>Use <code>GROUP BY</code> clause to group a set of rows into a set of summary rows</p>
</details>
<details>
      <summary>Hint#3</summary>
        <p>
            To remove duplicate rows from a result set, you can use the <code>DISTINCT</code> operator 
        </p>
</details>
</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

<ul>
    <li>
        First , we need to filter the valid activities. we can do this by using <code>WHERE</code> clause.
        <br>
        the <code>activity_date</code> should be less than or equal <code>2019-07-27</code>
        and greater than or equal <code>2019-07-27 - (29 days)</code>.
        To subtract a date interval from a date we can use <code>DATE_SUB(date , interval)</code> function.
    </li>
    <li>
        To count the number of users we can use <code>COUNT()</code> function , but the table may have duplicate rows. Here we can use <code>DISTINCT</code> operator inside <code>COUNT()</code> function as follows <code>COUNT(DISTINCT user_id)</code> to avoid duplicate rows.
    </li>
    <li>
        Finally , to group the result by <code>activity_day</code> we should use <code>GROUP BY</code> clause.
    </li>
</ul>

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users 
FROM 
    Activity 
WHERE 
    activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 day) 
    AND '2019-07-27' 
GROUP BY 
    activity_date

```

</details>