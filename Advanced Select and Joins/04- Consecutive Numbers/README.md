# [Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>Note that the <code>ID</code> is an autoincrement column</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>Use Self Joins</p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>How do you check if three numbers are consecutive? </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

This is a medium problem but it is very simple :).

First we need to understand that the <code>ID</code> column is an autoincrement column. This means that the <code>ID</code> column will always be in ascending order. This means that if we have three consecutive numbers then the difference between the first and the last number will be 2.

Now we need to find all the numbers that appear at least three times consecutively. This can be done by using a self join. We can join the table with itself (three times) and check if the difference between the <code>ID</code> column of the first and the second table is 1 and the difference between the <code>ID</code> column of the second and the third table is 1. If this is true then it means that the three numbers are consecutive.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select distinct i1.num as ConsecutiveNums from
logs i1,logs i2,logs i3
where i1.id = i2.id-1 and i2.id = i3.id-1 and i1.num=i2.num and i2.num=i3.num;
```

</details>
