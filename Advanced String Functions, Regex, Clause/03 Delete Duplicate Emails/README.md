# [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Delete all duplicate emails, keeping only one unique email with the smallest <code>id</code>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>Think in an easier problem. How can you select the valid records</p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>Try to use <code>SELF JOIN</code></p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>But we want to delete ?! , just a minor change :)</p>
</details>
<details>
      <summary>Hint#4</summary>
      <p>A SQL <code>DELETE</code> statement can include JOIN operations</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

The key ideas are
<br>

- A SQL <code>DELETE</code> statement can include JOIN operations.

- It can contain zero, one, or multiple <code>JOIN</code> operations.

- The DELETE removes records that satisfy the <code>JOIN</code> and <code>WHERE</code> condition.
- You must specify which table you want to delete from.

In this problem we will use <code>SELF JOIN</code> to JOIN <code>Person as a</code> with <code>itself as b</code>and specify table <code>a</code> in <code>delete</code> statement to delete the record from it.


We will Join the Person and itself ON the following condition
<br>
<code>a.email = b.email</code>
<br>
and specify the records the should be <code>deleted</code> by the following condition
<br>
<code>a.id > b.id</code>
<br>
Which means that if a record in table <code>a</code> find a record in table <code>b</code> that have the same email then <code>DELETE</code> the record of table <code>a</code> if this record has a bigger <code>ID</code> than the record of table <code>b</code>



</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
DELETE a 
FROM 
  Person a 
  JOIN Person b ON a.email = b.email
WHERE a.id > b.id

--INNER JOIN Person b ON a.id > b.id AND a.email = b.email
--You can combine them in join condition
```

</details>