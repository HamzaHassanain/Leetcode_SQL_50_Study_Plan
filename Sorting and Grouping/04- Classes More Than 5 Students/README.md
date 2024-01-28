# [Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find all the classes that have at least five students.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>SQL has an aggregation function called <code>COUNT(expression)</code> which count all the rows that satisfy a specified condition</p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>
        To specify a condition for groups, you can use the <code>HAVING</code> clause.
      </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

We need to find the classes that have at lease <code>5</code> students.

But why we can not use <code>where</code> clause ?

Because The <code>WHERE</code> clause applies the condition to individual rows before the rows are summarized into groups by the <code>GROUP BY</code> clause. However, the <code>HAVING</code> clause applies the condition to the groups after the rows are grouped into groups.

<ul> 
    <li>
        We will use <code>HAVING</code> to filter the data 
    </li>
    <li> 
        In the condition we will count the number of students by using <code>COUNT()</code> function
    </li>
    <li>
        To apply the <code>COUNT()</code> function to every class we should  use the <code>GROUP BY</code> clause before the <code>HAVING</code> clause.
    </li>
</ul>
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    class
FROM 
    Courses
GROUP BY 
    class
HAVING 
    COUNT(student) >= 5
```

</details>