# [Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by <code>sell_date</code>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>
        How can you concatenate strings from a group into a single string with various options ?
      </p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>
        The MySQL <code>GROUP_CONCAT()</code> function is an aggregate function that concatenates strings from a group into a single string with various options.
        </p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>SQL has an aggregation function called <code>COUNT(expression)</code> which count all the rows that satisfy a specified condition</p>
</details>
</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

<ul> 
    <li> 
        To count the number of different products we can use <code>COUNT()</code> function with <code>Distinct</code> clause to avoid duplication.
    </li>
    <li> 
        To concatenate the products from a group into a single string we can use <code>GROUP_CONCAT()</code> function.
<br>

```sql
GROUP_CONCAT(
DISTINCT expression
ORDER BY expression
SEPARATOR sep)
```
<br>
    the separator is <code>","</code> by default so we don't need to specify it.
    </li>
    <li>
        All these functions should grouped by <code>sell_date</code> with the <code>GROUP BY</code> clause.
    </li>
    <li> 
        Use the<code>ORDER BY</code> clause to order the result.
    </li>
</ul>

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    sell_date, 
    COUNT(DISTINCT product) AS num_sold, 
    GROUP_CONCAT(
    DISTINCT product 
    ORDER BY 
      product
    ) AS products 
FROM 
    Activities 
GROUP BY 
    sell_date 
ORDER BY 
    sell_date
```

</details>