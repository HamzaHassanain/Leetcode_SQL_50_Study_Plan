import os
dirs = ["02- Primary Department for Each Employee", "04- Consecutive Numbers", "06- Last Person to Fit in the Bus"]

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
basedir = "Advanced Select and Joins"
for dir in dirs:
    os.mkdir(os.path.join(basedir, dir))
    with open(os.path.join(basedir, dir, "README.md"), "w") as f:
        f.write(temp)
