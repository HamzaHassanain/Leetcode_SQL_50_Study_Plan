# [Restaurant Growth](https://leetcode.com/problems/restaurant-growth/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Compute the <code>moving average</code> of how much the customer paid in a seven days window (i.e., current day + 6 days before). <code>average_amount</code> should be rounded to two decimal places.

Return the result table ordered by <code>visited_on</code> in ascending order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>
        What if you have a table that has a day and it's total amount paid by customers How can you solve the problem then ?!
      </p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>
        Try to use <code>With clause</code> to define this temporary table and use it in your query.
      </p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>
        Use <code>SELF JOIN</code> to match every day with other days in it's week
      </p>
</details>
<details>
      <summary>Hint#4</summary>
      <p>
        To calculate the difference between two dates, you use the <code>DATEDIFF()</code>function.
        <br>
        <code>DATEDIFF ( datepart , startdate , enddate )</code>
      </p>
</details>
<details>
      <summary>Hint#5</summary>
      <p>
        How can you skip some record ?
      </p>
</details>
<details>
      <summary>Hint#6</summary>
      <p>
        The <code>OFFSET</code> offset clause skips the offset rows before beginning
        <br>
        <code>LIMIT row_count OFFSET offset</code>
      </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

Imagine that we have another table that contains <code>day</code> and the <code>total amount</code> paid by customers who visited the restaurant in this day <b> How can we solve the problem now</b>.

<ul>
    <li>
        We will JOIN the <code>NewTable as a</code> with <code>itself as b </code> On the following condition
        <br>
        a.day should be greater than or equal b.day <code>AND</code> the number of days between them should be less than or equal <code>6 days </code>
        <br>
        We can do this easily with the help of <code>DATEDIFF</code> function.
    </li>
    <li>
        To calculate the <code>total amount</code> paid from all customers we can use <code>SUM()</code> function. 
    </li>
    <li>
        To calculate the the <code>average amount</code> we just need to divide the <code>total amount paid</code>  by </code>7</code> and then use <code>ROUND()</code> function to round the result.
    </li>
    <li>
        The first six days will not have six days before them so wee need to use OFFSET to skip them
        <br>
        Use big number as possible in LIMIT clause
    </li>
</ul>

But the problem is how can we git this table :)

With help of <code>With clause</code> we can do this easily.

The <code>WITH clause</code>, also known as a Common Table Expression (CTE), is used to define a temporary result set that can be referred to within the context of a SELECT, INSERT, UPDATE, or DELETE statement. It helps to simplify complex queries by breaking them into more manageable and readable parts.

The basic syntax of a WITH clause is as follows:
```sql
WITH cte_name (column1, column2, ...) AS (
    -- Query that defines the CTE
    SELECT column1, column2, ...
    FROM some_table
    WHERE some_condition
)
-- The main query that references the CTE
SELECT *
FROM cte_name;

```
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
WITH temp AS 
(
    SELECT visited_on
    ,SUM(amount) AS tot
    FROM Customer
    GROUP BY visited_on
    ORDER BY visited_on
)
SELECT a.visited_on , SUM(b.tot) AS amount , ROUND(SUM(b.tot)/7 , 2) AS average_amount
FROM temp a
INNER JOIN temp b ON DATEDIFF(a.visited_on , b.visited_on) BETWEEN 0 AND 6
GROUP BY a.visited_on
ORDER BY a.visited_on
limit 100000000 OFFSET 6
-- Queries that have an associated WITH clause can also be written using nested
-- sub-queries but doing so add more complexity to read/debug the SQL query.
```

</details>