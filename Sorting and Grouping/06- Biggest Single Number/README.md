# [Biggest Single Number](https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the largest <strong>single number</strong>. If there is no <strong>single number</strong>, report <code>null</code>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>SQL has an aggregation function called <code>COUNT(expression)</code> which count all the rows that satisfy a specified condition</p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>
        To specify a condition for groups, you use the <code>HAVING</code> clause.
      </p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>
        To limit the number of rows returned by a <code>select</code> statement, you use the <code>LIMIT</code> clause
      </p>
</details>
<details>
      <summary>Hint#4</summary>
      <p>
        The MySQL <code>IFNULL()</code> function lets you return an alternative value if an expression is <code>NULL</code>
      </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

<ul> 
    <li>
    First, we should find all the number that appeared only once. This can done with <code>COUNT()</code> function and <code>GROUP BY</code> clause to group the result by <code>num</code>
    </li>
    <li>
        To find the largest number , we can order the result by <code>num</code> in descending order by using <code>ORDER BY</code> clause and then use <code>LIMIT</code> clause to limit the number of rows returned
    </li>
    <li>
    But what if noting was returned at all ?!
    <br>
    Here we can use <code>IFNULL()</code> function as follows 
    <br>
    If nothing was returned return <code>NULL</code>
    <br>
    IN SQL <code>IFNULL(Our_selected_data , NULL)</code>
    </li>
</ul>

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    IFNULL(
    (
        SELECT 
            num 
        FROM 
            MyNumbers 
        GROUP BY 
            num 
        HAVING 
            COUNT(num) = 1 
        ORDER BY 
            num DESC 
        limit 
            1
    ), 
    NULL
  ) AS num
-- But why we can not use <code>where</code> clause ?

-- Because The WHERE clause applies the condition to individual rows before the rows are summarized  into groups by the GROUP BY clause. However, the HAVING clause applies the condition to the groups after the rows are grouped into groups.
```

</details>