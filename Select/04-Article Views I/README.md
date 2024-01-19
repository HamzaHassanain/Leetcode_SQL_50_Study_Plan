# [Article Views I](https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find all the authors that viewed at least one of their own articles.

<strong>NOTE: </strong> Print the result table sorted by id in <b>ascending order</b>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>Use <code>DISTINCT</code> to avoid duplicates. </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

<p>
    Let's divide the problem into two sub problems.
    <ul>
        <li>Retrieve all the authors using<code>SELECT</code> statement </li>
        <li>Filtering the retrieved data using <code>WHERE</code> clause and <code>OPERATORS</code>  </li>
    </ul>
    <p>
        First retrieve the authors using <code>select</code> statement then use <code>where</code> clause to filter all the authors that satisfy the following condition <code>author_id = viewer_id</code> in the corresponding row.
        <br>
        This criterion indicates that the author has viewed the current article.
    </p>
    <p>
        But what if the author's id is duplicated , here we can use 
        <code>DISTINCT</code> clause to avoid that.
    </p>
</p>

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id
;
```

</details>