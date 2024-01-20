# [Customer Who Visited but Did Not Make Any](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-Transactionss/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the IDs of the users who visited without making any Transactions and the number of times they made these types of visits.

Return the result table sorted in any order.
<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>Use <code>OUTER JOIN </code></p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>SQL has an aggregation function called <code>COUNT(expression)</code> which count all the rows that satisfy a specified condition</p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>You can use <code>IS NULL</code> to check if the value is null</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

Let's rephrase the problem statement to make our life easier.
<br>
For every <code>customer</code> <code>count</code> the number of <code>visits</code> <strong>that does not exist</strong> in Transactions Table such that <code>counter > 0</code>.
<br>
<br>
First let's try to solve easier problem. we want to count the number of <code>visits</code> for every customer whether it exists in Transactions table or no.
<br>
we can do this by selecting <code>customer_id</code> and counting <code> visit_id</code>  using <code>COUNT()</code>function.
<br>
<br>
The last thing we don't want to take the <code>visits</code> that exist in Transactions table into account, so we can left join Transactions table on visit_id and that will allow us to have <code>NULL</code> information about Transactions <i>(which means that the Visits.visit_id doesn't have matching information in Transactions table or doesn't exists)</i>  then filter these record using <code>WHERE</code> clause and <code>IS NULL </code> operator.
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
  customer_id, 
  COUNT(Visits.visit_id) AS count_no_trans 
FROM 
  Visits 
  LEFT OUTER JOIN Transactions ON Transactions.visit_id = Visits.visit_id 
WHERE 
  Transactions_id IS NULL 
GROUP BY 
  customer_id
;
```

</details>