import os
dirs = ["01- Number of Unique Subjects Taught by Each Teacher", "03- Product Sales Analysis III", "05- Find Followers Count" , "07- Customers Who Bought All Products"]

temp = """
# [Problem name](https://problem-link-on-leetcode.com)

### Problem Requirements:

Problem requirements go here.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1-10</summary>
      <p>hint body goes here</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>


Explanation goes here.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
    SQL code goes here
```

</details>
"""
basedir = "Sorting and Grouping"
for dir in dirs:
    os.mkdir(os.path.join(basedir, dir))
    with open(os.path.join(basedir, dir, "README.md"), "w") as f:
        f.write(temp)
