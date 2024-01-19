# [Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

We define query <code>quality</code> as:

    The average of the ratio between query rating and its position.

We also define <code>poor_query_percentage</code> as:

    The percentage of all queries with rating less than 3.

Find each <code>query_name</code>, the <code>quality</code> and <code>poor_query_percentage</code>.

Both <code>quality</code> and <code>poor_query_percentage</code> should be rounded to <code>2</code> decimal places.

Return the result table in any order.

<!-- <details open>
<summary style="font-size:1.5rem;"> <strong>Solution#1</strong> </summary> -->

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>How SQL <code>AVG</code> function works ? <br>
        <code>AVG(column_name) = SUM(column_name) / COUNT(column_name)</code>
        </p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>SQL has something called <code>CASE</code> Expression <br>
        <code>CASE WHEN condition THEN value1 ELSE value2 END</code>
       </p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>Try combining <code>AVG</code> and <code>CASE</code> together</p>
</details>
<details>
      <summary>Hint#5</summary>
      <p> Use Grouping </p>
</details>
<details>
      <summary>Hint#4</summary>
      <p> Note that <code>query_name</code> may be <code>NULL</code> </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

This problem is a bit tricky, we need to calculate the <code>quality</code> and <code>poor_query_percentage</code> for each <code>query_name</code>.

First we must think about Grouping the data by <code>query_name</code>, then we can calculate the <code>quality</code> and <code>poor_query_percentage</code> for each group using <code>AVG</code> function.

The <code>quality</code> is the average of the ratio between query rating and its position <code>q1.rating / q1.position</code>, so we can use <code>AVG</code> as following: <code>AVG(q1.rating / q1.position)</code>

The <code>poor_query_percentage</code> is the percentage of all queries with rating less than <code>3</code>, so how do we get the avarge of this condition ? we can use <code>CASE</code> expression to check if the rating is less than <code>3</code>, then we can calculate the average of this condition, do not forget to multiply the avarage by <code>100</code> to get the percentage.

Do not forget to round the results to <code>2</code> decimal places.

Also do not forget to filter out the <code>NULL</code> values in <code>query_name</code> column.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select
    q1.query_name as query_name,
    round(avg(q1.rating / q1.position), 2) as quality,
    round(100 * avg(case when q1.rating < 3 then 1 else 0 end), 2)  as poor_query_percentage
from Queries q1
where q1.query_name is not null
group by query_name;
```

</details>

<!-- </details> -->
