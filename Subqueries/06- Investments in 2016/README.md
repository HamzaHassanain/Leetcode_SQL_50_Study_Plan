# [Investments in 2016](https://leetcode.com/problems/investments-in-2016/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Report the sum of all total investment values in 2016 <code>tiv_2016</code>, for all policyholders who:

- have the same tiv_2015 value as one or more other policyholders, and
- are not located in the same city as any other policyholder (i.e., the (<code>lat, lon</code>) attribute pairs must be unique).

Round <code>tiv_2016</code> to two decimal places.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>How to test for the existence of any record meeting specific criteria?</p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>The <code>EXISTS</code> operator is used to test for the existence of any record in a subquery</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

<ul>

<li>
    To check that there is no another policyholder in the same city 
    We will use <code>NOT</code> and <code>EXISTS</code> operators
    and then specify a <code>subquery</code> to test for the existence of different policyholders in the same city
</li>
<li>
    To check that there is  another policyholder in different city 
    We will use <code>EXISTS</code> operator
    and then specify a <code>subquery</code> to test for the existence of different policyholders in different cities have the same investment in <code>2015</code>
</li>
<li>
    To sum of all total investment values in <code>2016</code> we can use <code>SUM()</code> function and then use <code>ROUND()</code>
    function to round the result 
</li>
</ul>

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT ROUND(SUM(b.tiv_2016) , 2) AS tiv_2016
FROM Insurance b
WHERE NOT EXISTS(
    SELECT a.pid
    FROM Insurance a
    WHERE a.lat = b.lat AND a.lon = b.lon AND a.pid != b.pid
)
AND EXISTS(
    SELECT a.pid
    FROM Insurance a
    WHERE a.tiv_2015 = b.tiv_2015 AND a.pid != b.pid
)
-- The EXISTS operator returns true if the subquery contains any rows. 
-- Otherwise, it returns false.
```

</details>