# [Confirmation Rate](https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

The confirmation rate of a user is the number of <code>'confirmed'</code> messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is <code>0</code>. Round the confirmation rate to <strong>two decimal</strong> places.

Find the confirmation rate of each user.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>How can you count the number of actions when <code>action = confirmed</code>, try it using <code>CASE</code> statement</p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>Use <code>OUTER JOIN </code></p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>SQL has an aggregation function called <code>SUM(expression)</code> which calculate the sum of values in a set</p>
</details>
<details>
      <summary>Hint#4</summary>
      <p>SQL has a <code>ROUND(number, decimals)</code> function which rounds a number to a specified number of decimal places. </p>
</details>
<details>
      <summary>Hint#5</summary>
      <p>Use <code>GROUP BY</code> clause to group a set of rows into a set of summary rows</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>
Let's rephrase the problem statement to make our life easier.
<br>
for each user divide the number of confirmed message with the total requested messages.

![equation](https://latex.codecogs.com/gif.latex?round%28%5Cfrac%7Bcount%28confirmed_messages%29%7D%7Bcount%28messages%29%7D%20%2C%202%29)
<br>
First, count the total requested messages for each user. we can use <code>COUNT()</code> function to evaluate this easily.
<br>
<br>
Second, count the confirmed messages for each user. we can use <code>CASE</code> statement with <code> SUM()</code> function to evaluate this as follows <b>:</b> if the message is confirmed add <code>1</code> to your sum otherwise add <code>0</code>.
<br>
<br>
Finally, divide confirmed messages by total requested messages then round the result to 2 decimals using <code> ROUND(number , decimals)</code> function.
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
  Signups.user_id, 
  ROUND(
    SUM(
      CASE WHEN Confirmations.action = 1 THEN 1 ELSE 0 END
    ) / COUNT(Signups.user_id), 
    2
  ) AS confirmation_rate 
FROM 
  Signups 
  LEFT OUTER JOIN Confirmations ON Signups.user_id = Confirmations.user_id 
GROUP BY 
  Signups.user_id
```

</details>