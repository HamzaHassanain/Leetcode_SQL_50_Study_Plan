# [Students and Examinations](https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>Use Multiple <code>Joins</code></p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>Use <code>CROSS JOIN</code> with subjects and <code>OUTER JOIN</code> with Examinations</p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>SQL has an aggregation function called <code>COUNT(expression)</code> which count all the rows that satisfy a specified condition</p>
</details>
<details>
      <summary>Hint#4</summary>
      <p>Use <code>GROUP BY</code> clause to group a set of rows into a set of summary rows</p>
</details>
<details>
      <summary>Hint#5</summary>
      <p>Use <code>ORDER BY</code> clause to sort a set of rows in <code>ASC </code> or <code> DESC </code></p>
</details>
<details>
      <summary>Hint#6</summary>
      <p>Use <code>AND</code> operator to combine more than one condition  </p>
</details>
</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

Let's rephrase the problem statement to make our life easier.
<br>
for every record in the combination of <code>student</code> and <code>subject</code> <code>count</code> how many times it exists in Examinations table.
<br>
<br>
First, let's make the combination of <code>students</code>and<code>subjects</code>.It's done easily using <code>CROSS JOIN</code>.
<br>
<br>
Second, <code>JOIN</code> Examinations table <code>ON</code> <code>student_id</code> <strong>and</strong> <code>subject_id</code>
Then count <code>Examinations.student_id</code> or <code>Examinations.subject_name</code> using <code>COUNT()</code>function grouped by <code>student_id </code> and <code>subject_name</code>. 
<br>
<br>
Finally, Order the result Using <code>ORDER BY</code> clause in ascending order<code>(ASC)</code>.
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
  Students.student_id, 
  Students.student_name, 
  Subjects.subject_name, 
  COUNT(Examinations.student_id) AS attended_exams 
FROM 
  Students  
  CROSS JOIN Subjects  
  LEFT OUTER JOIN Examinations  ON Students.student_id = Examinations.student_id 
  AND Subjects.subject_name = Examinations.subject_name 
GROUP BY 
  Students.student_id, 
  Subjects.subject_name 
ORDER BY 
  Students.student_id, 
  Subjects.subject_name
;
-- I preferred to use CROSS JOIN because no need to specify any condition and CROSS JOIN does not have the ON or USING clause also you can use another type of JOINS

```

</details>