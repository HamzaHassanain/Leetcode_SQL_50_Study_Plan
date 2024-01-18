# [Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find managers with at least five direct reports.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 
<br>

<details>
      <summary>Hint#1</summary>
      <p>Self join Employee's table with itself using Inner Join</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>Use GROUP BY clause </p>
</details>
</details>

<br>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

<br>

We want to find the managers with at least five direct reports. So we must join the Employee table with itself on the employee1.id equals the employee2.managerId

To find the managers with at least five direct reports, we must count the number of direct reports for each manager. We can do this by grouping the result by the managerId and then counting the number of direct reports for each manager. We can then use the HAVING clause to filter out the managers with less than five direct reports.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 
<br>

```sql
SELECT e1.name AS name
FROM Employee e1 INNER JOIN Employee e2 ON e1.id = e2.managerId
GROUP BY  e2.managerId
HAVING COUNT(e2.managerId) >= 5;
```

</details>
