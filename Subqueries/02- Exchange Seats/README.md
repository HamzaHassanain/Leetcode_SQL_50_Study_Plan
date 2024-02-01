# [Exchange Seats](https://leetcode.com/problems/exchange-seats/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Write a query to swap the seat <code>id</code> of every two consecutive students. If the number of students is <strong>odd</strong>, the <code>id</code> of the last student is <strong>not</strong> swapped.

Return the result table ordered by <code>id</code> in <strong>ascending order</strong>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>How to determine if a student should be swapped or not?</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>A student will be swapped if and only if he is not the last student or the number of students is even.</p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>Suppose that a student will be swapped. What is the id of the student he or will be swapped with?</p>
</details>

<details>
      <summary>Hint#4</summary>
      <p>If a student is going to be swapped, he will be swapped with the student having his id plus one or minus one depending on the parity of the student's id.</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

We will use a subquery to get the student's name after swapping. We will change the student's name if he isn't the last student or the number of students is even.

To swap the student's name, we will check the parity of the student id. If the student id is odd he will be given the name of the student having his id plus one. Otherwise, he will be given the name of the student having his id minus one.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
SELECT s.id AS id,
  IF(
    s.id < (SELECT count(*) FROM Seat)
    OR
    MOD((SELECT count(*) FROM Seat), 2) = 0
    ,
    (
        SELECT student
        FROM Seat
        WHERE id = IF(MOD(s.id, 2) = 1, s.id+1, s.id-1)
    )
    ,
    s.student
  ) as student
FROM Seat as s
ORDER BY id;
```

</details>
