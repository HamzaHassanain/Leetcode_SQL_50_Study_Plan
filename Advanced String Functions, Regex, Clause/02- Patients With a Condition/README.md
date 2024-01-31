# [Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the <code>patient_id, patient_name, and conditions</code> of the patients who have Type I Diabetes. Type I Diabetes always starts with <code>DIAB1</code> prefix.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 
<details>
      <summary>Hint#1</summary>
      <p>We can use the  <code>LIKE</code> To check for strings matching  </p>
</details>

<details>
      <summary>Hint#2</summary>
      <p> Do not forget to check for the condition that  <code>DIAB1</code> is not the first word</p>
</details>

</details>
<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

This is a very straightforward problem.

We will just use the `LIKE` operator to check for the condition, and we will use the `%` wildcard to match any string that starts with `DIAB1` or has `DIAB1` in the middle.

</details>
<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
SELECT * FROM Patients WHERE conditions LIKE '% DIAB1%' OR  conditions LIKE 'DIAB1%';
```

</details>
