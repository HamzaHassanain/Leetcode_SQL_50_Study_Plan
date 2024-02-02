# [Count Salary Categories](https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

- <code>"Low Salary"</code>: All the salaries strictly less than <code>$20000</code>.
- <code>"Average Salary"</code>: All the salaries in the inclusive range <code>[$20000, $50000]</code>.
- <code>"High Salary"</code>: All the salaries strictly greater than <code>$50000</code>.

The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in <strong>any order</strong>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>
        MySQL <code>UNION</code> operator allows you to combine two or more result sets of queries into a single result set.
      </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

Counting the matching records for each category is an easy task.

Simply employ the <code>COUNT()</code> function and  filter the records by applying conditions through the <code>WHERE</code> clause.

To combine result sets from multiple <code>SELECT</code> statements, utilize the <code>UNION</code> operator. The choice between <code>UNION</code> and <code>UNION ALL</code> does not affect the outcome in this case, as <strong>the result set does not contain any duplicate entries</strong>.
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    'Low Salary' AS category, 
    count(*) as accounts_count
FROM 
    Accounts
WHERE income < 20000 

UNION -- #####################################

SELECT 
    'Average Salary' AS category, 
    count(*) AS accounts_count 
FROM 
    Accounts 

WHERE income BETWEEN 20000 AND 50000

UNION -- #####################################

SELECT 
    'High Salary' AS category, 
   count(*) AS accounts_count 
FROM 
    Accounts
WHERE income > 50000
-- * symbol means all
```

</details>