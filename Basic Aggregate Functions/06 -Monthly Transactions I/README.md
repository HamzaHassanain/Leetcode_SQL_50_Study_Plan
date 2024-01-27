# [Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>How can you do some things when you find given conditions?</p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>Try it using <code>CASE</code> statement</p>
</details>
<details>
      <summary>Hint#3</summary>
        <p>
            SQL has an aggregation function called <code>COUNT(expression)</code> which count all the rows that satisfy a specified condition
        </p>
</details>
<details>
      <summary>Hint#4</summary>
       <p>
            SQL has an aggregation function called <code>SUM(expression)</code> which calculate the sum of values in a set
        </p>
</details>
<details>
      <summary>Hint#5</summary>
       <p>
            The <code>DATE_FORMAT(date , format)</code> function formats a date as specified.
        </p>
</details>
<details>
      <summary>Hint#6</summary>
        <p>Use <code>GROUP BY</code> clause to group a set of rows into a set of summary rows</p>
</details>
</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

<ul> 
    <li>To count the total number of transactions we can use <code>COUNT()</code> function </li>
    <li>
        To count the total number of approved transactions we can use <code>COUNT()</code> function with the help of <code>CASE</code> statement as follows
        <br>
        WHEN state = approved THEN add <code>1</code> ELSE add <code>0</code>
    </li>
    <li>To sum the total amount we can use <code>SUM()</code> function </li>
    <li>
        To sum the total approved amount we can use <code>SUM()</code> function with the help of <code>CASE</code> statement as follows
        <br>
         WHEN state = approved THEN add <code>amount</code> ELSE add <code>0</code>
    </li>
    <li> 
        All these functions should grouped by the combination of month and country with the <code>GROUP BY</code> clause.
    </li>
</ul>

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month, 
    country, 
    COUNT(state) AS trans_count, 
    SUM(
        CASE WHEN state = 'approved' THEN 1 ELSE 0 END
    ) AS approved_count, 
    SUM(amount) AS trans_total_amount, 
    SUM(
        CASE WHEN state = 'approved' THEN amount ELSE 0 END
    ) AS approved_total_amount 
FROM 
    Transactions 
GROUP BY 
    month, 
    country

    -- we can count the number of approved transactions in another way.
    
    -- COUNT(
    --    CASE WHEN state = 'approved' THEN 1 ELSE NULL END
    -- ) AS approved_count

    -- COUNT function will ignore NULL.
```

</details>