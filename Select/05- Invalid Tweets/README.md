# [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is <strong> strictly greater than <code> 15</code> </strong>.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>There is a function in SQL called <code> LENGTH</code> that returns the number of characters of a string.
  </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;font-weight:800"> Explanation </summary>

We need to find the <code> IDs</code> of the tweets that are invalid. A tweet is invalid if the number of characters used in the content of the tweet is <strong> strictly greater than <code> 15</code> </strong>.

We can do this by using the <code> WHERE</code> clause and the <code> LENGTH</code> function.

The <code> LENGTH</code> function will return the number of characters in the content of the tweet. The <code> WHERE</code> clause will filter out all the tweets that are not invalid (Their length is strictly greater than 15).

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
SELECT tweet_id from Tweets where LENGTH(content) > 15;
```

</details>
