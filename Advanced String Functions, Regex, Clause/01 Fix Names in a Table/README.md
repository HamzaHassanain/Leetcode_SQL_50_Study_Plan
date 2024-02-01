# [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by <code>user_id</code>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>
        Try to divide the strings into two parts and work on each one of them
      </p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>How can you divide the string into substrings</p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>
        The <code>SUBSTRING</code> function extracts a substring that starts at a specified position with a given length.
        <br>
        <code>SUBSTRING(source_string, position, length)</code>
      </p>
</details>
<details>
      <summary>Hint#4</summary>
      <p>How to convert a string into a lowercase/uppercase</p>
</details>
<details>
      <summary>Hint#5</summary>
      <p>
      The SQL <code>UPPER</code> function converts all the letters in a string into uppercase
      <br>
      <code>UPPER(string)</code>
      <br>
      The SQL <code>LOWER</code> function converts all the characters in a string into lowercase
      <br>
      <code>LOWER(string)</code>
      </p>
</details>
<details>
      <summary>Hint#6</summary>
      <p>How to concatenate two or more strings into one string</p>
</details>
<details>
      <summary>Hint#7</summary>
      <p>
      The SQL <code>CONCAT</code> function concatenates two or more strings into one string
      <code>CONCAT(string1,string2,..)</code>
      </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

<ul> 
    <li>
    First divide the <code>name</code> into two parts.The first character in the left part and the remainder of the name in the right part By using <code>SUBSTRING</code> function
    </li>
    <li>Convert the left part into <code>uppercase</code> by using <code>UPPER</code> function </li>
    <li>Convert the right part into <code>lowercase</code> by using <code>LOWER</code> function </li>
    <li>
    Concatenate the left part and the right part into one string by using <code>CONCAT</code> function
    </li>
    <li> 
        Order the result by using <code>ORDER BY</code> clause
    </li>
</ul>

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    user_id, 
    CONCAT(
    UPPER(
      SUBSTRING(name, 1, 1)
    ), 
    LOWER(
      SUBSTRING(name, 2)
    )
    ) AS name 
FROM 
    Users 
ORDER BY 
    user_id
```

</details>