# [Number of Unique Subjects Taught by Each Teacher](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Calculate the number of <strong> unique </strong> subjects each teacher teaches in the university.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>What do we normally think about when here the word <strong> each ?</strong>  </p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>Think about Grouping</p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>You can use <code>COUNT(DISTINCT column_name)</code> to count the unique values in the column</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

This question is a simple grouping question.

First When we see the word <strong> each </strong> we think about grouping. We will group by the <code>teacher_id</code>.

Then we need to count the number of unique subjects each teacher teaches. We can use the <code>COUNT(DISTINCT subject_id)</code> to count the number of unique values of <code>subject_id</code> in the column.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select teacher_id,count(distinct subject_id) as cnt from Teacher
group by teacher_id;
```

</details>
