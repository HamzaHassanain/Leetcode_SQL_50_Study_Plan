# [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is <strong> strictly greater than 15 </strong>.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 
<br>

<details>
      <summary>Hint#1</summary>
      <p>There is a function in SQL called <strong style="color:yellow;"> LENGTH </strong> that returns the number of characters of a string.
  </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;font-weight:800"> Explanation </summary> 
<br>

We need to the IDs of the tweets that are invalid. A tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

We can do this by using the <strong> WHERE </strong> clause and the <strong> LENGTH </strong> function.

The <strong style="color:yellow;"> LENGTH </strong> function will return the number of characters in the content of the tweet. The <strong> WHERE </strong> clause will filter out all the tweets that are not invalid (Their length is strictly greater than 15).

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 
<br>

```sql
SELECT tweet_id from Tweets where LENGTH(content) > 15;
```

</details>
