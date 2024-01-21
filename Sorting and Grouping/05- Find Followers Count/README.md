# [Find Followers Count](https://leetcode.com/problems/find-followers-count/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

For each user, return the number of <strong>followers</strong>.

Return the result table ordered by <code>user_id</code> in ascending order.

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
      <p>Use SQL <code>COUNT()</code> function to count the number of  followers</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

This is a simple grouping question.

First When we see the word <strong> each </strong> we think about grouping. We will group by the user_id.

Then we need to count the number of followers for each user. We can use the <code>COUNT()</code> function to count the number of followers for each user.

Finally, we need to order the result by <code>user_id</code> in ascending order using the <code>ORDER BY</code> clause and <code>ASC</code> keyword.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
SELECT user_id, COUNT(follower_id) AS followers_count
FROM followers
GROUP BY user_id
ORDER BY user_id ASC;
```

</details>
