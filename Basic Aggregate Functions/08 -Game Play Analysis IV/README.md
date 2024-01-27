# [Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

 Find the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>
        What if you have another column that has the <code>first_login</code>,
        The problem will be very easy, isn't it?
      </p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>
        Try use <code>WITH</code> clause. It will help you to define a temporary data set. It will make your life easier.
      </p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>
      The SQL <code>MIN(expression)</code> function returns the minimum value in a set of values
      </p>
</details>
<details>
      <summary>Hint#4</summary>
      <p>
        Try use <code>window function</code>.
      </p>
</details>

<details>
      <summary>Hint#5</summary>
      <p>SQL has an aggregation function called <code>COUNT(expression)</code> which count all the rows that satisfy a specified condition</p>
</details>
<details>
      <summary>Hint#6</summary>
      <p>
      To subtract an interval e.g., a year, a month and a day to date, you can use the <code>DATE_SUB()</code> function. 
      </p>
</details>
<details>
      <summary>Hint#7</summary>
      <p>SQL has a <code>ROUND(number, decimals)</code> function which rounds a number to a specified number of decimal places. </p>
</details>
</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

We want to count the number of players who logged in the next day of their first login day.
<br>
we should determine the first login date for each player.
Then when we find a player logged in the next day of this day we should put this player into account.

<ul>
  <li>We can determine the first login for each player with the help of aggregate window function
  <code>MIN(expression) OVER </code>
  . Aggregate window function will work the same as the normal aggregate function but it doesn't cause rows to become grouped into a single output row. 
  </li>
  <li>To be able to use our original table and the new column we can use <code> WITH</code> clause , it will help us to define the temporary data set and use them in the query.
  </li>
  <li>  
  We will filter this table according to our condition <code>(event_date and first_login are consecutive days)</code>.
  <br>
  We can use  <code>DATE_SUB()</code> function to subtract a given duration from <code>event_date</code> As follows<br> <code>DATE_SUB(event_date, INTERVAL 1 DAY) = first_login</code> 
  </li>
  <li>
  Finally, divide the player that satisfies the condition by the total number of player that we can calculate as a <code>subquery</code> then round the result using <code>ROUND()</code>function to round the result.
  </li>
</ul>

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
WITH temp AS(
  SELECT 
    *, 
    MIN(event_date) OVER (Partition BY player_id) AS first_login 
    -- over means that the function before it is a window function 
  FROM 
    Activity
)
SELECT 
  ROUND(
    (
      SELECT 
        COUNT(player_id) 
      FROM 
        temp 
      WHERE 
        DATE_SUB(event_date, INTERVAL 1 DAY) = first_login
    ) / (
      SELECT 
        COUNT(DISTINCT player_id) 
      FROM 
        Activity
    ), 
    2
  ) AS fraction


```

</details>