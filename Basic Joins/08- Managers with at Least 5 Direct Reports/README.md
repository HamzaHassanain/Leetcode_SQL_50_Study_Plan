# [Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find managers with at least <code>5</code> direct reports.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>Self join Employee's table with itself <code> using INNER JOIN</code></p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>Use <code>GROUP BY</code> clause </p>
</details>
</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

We want to find the managers with at least <code>5</code> direct reports. So we must join the Employee table with itself on the <code> employee1.id = the employee2.managerId </code> considering that the employee1 is the manager of employee2.

To find the managers with at least <code>5</code> direct reports, we must count the number of direct reports for each manager. We can do this by grouping the result by the <code>managerId</code> and then counting the number of direct reports for each manager. We can then use the <code>HAVING</code> clause and <code>COUNT</code> function to filter out the managers with at least <code>5</code> direct reports.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
SELECT e1.name AS name
FROM Employee e1 INNER JOIN Employee e2 ON e1.id = e2.managerId
GROUP BY  e2.managerId
HAVING COUNT(e2.managerId) >= 5;
```

</details>
