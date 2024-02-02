# [Triangle Judgement](https://leetcode.com/problems/triangle-judgement/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Report for every three line segments whether they can form a triangle.

Return the result table in <strong>any order</strong>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>Review the <strong>Triangle Inequality Theorem</strong></p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>Use <code>CASE Statement</code></p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

[Triangle inequality](https://www.mathsisfun.com/geometry/triangle-inequality-theorem.html)
<br>
The <code>triangle inequality</code> states that for any triangle, the sum of the lengths of any two sides must be greater than the length of the remaining side.

To report the status for every three line segments we can use 
<code>CASE Statement</code>

A triangle is considered valid if the sum of any two sides is greater than the third side. <code>Conversely</code>, if the sum of any two sides is less than or equal to the remaining side, <code>it does not form a valid triangle</code>.
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT * ,
    (
    CASE 
        WHEN x+y<=z THEN 'No'
        WHEN x+z<=y THEN 'No'
        WHEN z+y<=x THEN 'No'
        ELSE 'Yes'
    END
    ) AS triangle
FROM Triangle
```

</details>