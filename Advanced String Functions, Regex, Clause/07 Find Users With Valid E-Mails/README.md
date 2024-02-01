# [Find Users With Valid E-Mails](https://leetcode.com/problems/find-users-with-valid-e-mails/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the users who have valid emails.

Return the result table in any order.
<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>
        Try to use <code>REGEXP</code> operator to determine if a string matches a regular expression.
        <br>
        <code>expression REGEXP pattern</code>
      </p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>To define the search criteria and pattern you can use <code>Metacharacters</code></p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

First of all you have to be familiar with the following <code>Metacharacters</code>
<ol>

<li>
    The caret symbol <code>^</code> is used to check if a string starts with a certain character
</li>
<li> 
    The dollar symbol <code>$</code> is used to check if a string ends with a certain character
</li>
<li>
    The star symbol <code>*</code> matches zero or more occurrences of the pattern left to it
</li>
<li>
    Square brackets specifies a set of characters you wish to match
</li>

</ol> 
With the help of <code>REGEXP</code> and <code>Metacharacters</code> the problem will be a piece of cake :)
<ul>
    <li>
        <code>^[a-zA-Z]</code> 
        <br>
        The mail must starts with any character between 
        <code>[a , b , c , ... , z]</code>or<code>[A , B , C , ... , Z]</code>
    </li>
    <li>
        <code>@leetcode[.]com$</code> 
        <br>
        The mail must ends with <code>@leetcode.com</code>
        <br>
        We used <code>[.]</code> instead of <code>.</code> because <code>.</code> is a MetaCharacter
    </li>
    <li>
    <code>[-._a-zA-Z0-9]</code>
    <br>
    Between the start and the end the mail must contain zero or more occurrences of any character specified in the following line
    <br>
    <code>.</code> or <code>-</code> or <code>_</code> or <code>[a, b, c, ... , z]</code> or <code>[A, B, C, ... , Z]</code>
    </li>
</ul>
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT *
FROM  Users
WHERE mail REGEXP '^[a-zA-Z][-._a-zA-Z0-9]*@leetcode[.]com$'
```

</details>