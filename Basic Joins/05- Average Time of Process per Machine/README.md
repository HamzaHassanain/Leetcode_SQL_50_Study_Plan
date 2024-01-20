# [Average Time of Process per Machine](https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p> Can you multiply timestamp with <code>-1</code> when activity is start </p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>Try it using <code> CASE</code> statement.</p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>SQL has a <code>ROUND(number, decimals)</code> function which rounds a number to a specified number of decimal places. </p>
</details>
<details>
      <summary>Hint#4</summary>
      <p>SQL has an aggregation function called <code>COUNT(expression)</code> which count all the rows that satisfy a specified condition</p>
</details>
<details>
      <summary>Hint#5</summary>
      <p>SQL has an aggregation function called <code>SUM(expression)</code> which calculate the sum of values in a set</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

Let's rephrase the problem statement to make our life easier.
<br>
For every <code>machine</code> evaluate the following 

$$
round( \frac{(timestamp_{end}) - sum(timestamp_{start})}{count(process)} , 3)
$$

<br>
The easiest way is to solve this problem is to use aggregation functions.
<br>
<br>
First we need to calculate the time of all process , we need to sum
<code>end_time - start_time</code> , with the help of <code>CASE</code> statement we can negate start_time then add the result to the time using <code> SUM()</code> function.
<br>
<br>
Second we want to <code>COUNT</code> the number of process , we can use <code>COUNT()</code>  function but we should divide it with <code>2</code> because every process has start_time and end_time so it will be calculated twice.
<br>
<br>
Finally, divide the<code>time</code> with the <code> number of process</code> then <code>ROUND</code> the result to 3 decimal places using <code>ROUND(number , decimals)</code> function.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
  machine_id, 
  ROUND(
    SUM(
      CASE WHEN activity_type = 'start' THEN timestamp *-1 ELSE timestamp END
    )/(
      COUNT(process_id)/ 2
    ), 
    3
  ) AS processing_time 
FROM 
  Activity 
GROUP BY 
  ac.machine_id
```

</details>