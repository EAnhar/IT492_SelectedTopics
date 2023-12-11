# Project-4-Brevets

Reimplement the RUSA ACP control time calculator with flask
and ajax.

Anhar Aldosari 411201886@qu.edu.sa

## Grading Rubric

* **[50 Points]** For passing our test cases (not given) that
  exercise your implementation of the `acp_times.py`. We will 
  write our test cases based on the requirements described on the
  given documentation links.
* **[30 Points]** For writing at least 5 **distinguishable** test 
  cases that exercise your code (6 points each).<br>
  ## Test opeining and closing time for:
```
  60km control with brevet distance 200 (the maximum time limit for a control within the first 60km is based on 20 km/hr, plus 1 hour.)
  120km control with brevet distance 200 
  150km control with brevet distance 200 
  200km control with brevet distance 200 (Overall time limits )
  205km control with brevet distance 200 (we use a distance of 200km in the calculation, even though the route was slightly longer than that (205km). By the rules, the overall time limit for a 200km brevet is 13H30, even though by calculation, 200/15 = 13H20. The fact that the route is somewhat longer than 200km is irrelevant.)

  311km control with brevet distance 400 

  550km control with brevet distance 600 
  600km control with brevet distance 600 (Overall time limits )

  700km control with brevet distance 1000 
  890km control with brevet distance 1000 
  ```

* **[20 Points]** For a working docker container!

## Bonus Points
* **[30 Points]** For improving the front functionality to validate
  and communicate the typing of any invalid inputs. You decide what
  is invalid based on the documentation, and you decide how you will
  help the user understand what they did wrong, so they can correct
  their inputs. by anhar