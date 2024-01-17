# [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is <span style="font-weight:bold"> strictly greater than 15 </span>.

Return the result table in any order.

### SQL Solution

```sql
SELECT tweet_id from Tweets where LENGTH(content) > 15;
```

### Explanation

We need to the IDs of the tweets that are invalid. A tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

We can do this by using the <span style="color:blue;font-weight:bold"> WHERE </span> clause and the <span style="color:yellow;font-weight:bold"> LENGTH </span> function.

The <span style="color:yellow;font-weight:bold"> LENGTH </span> function will return the number of characters in the content of the tweet. The <span style="color:blue;font-weight:bold"> WHERE </span> clause will filter out all the tweets that are not invalid (Their length is strictly greater than 15).
