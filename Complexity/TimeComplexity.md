# Time Complexity 
<hr>

### Important Points:
* Look for Worst Case complexity.
* Always look for complexity for large or infinite data.
* Ignore the constants.
* Ignore the less dominating terms.

Comparisons of Time Complexity:  **1 < Log N < N < N<sup>2</sup> < 2<sup>N</sup>**

![Comparing Time Complexity](https://courses.cs.washington.edu/courses/cse373/19sp/files/resources/function-growth-rates.png)

### Big O

* This is the upper bound ,i.e, the complexity cannot be greater than Big O.
* Formal definition: **f(N) <= &Omicron;(g(N))** as _N tends to infinity_.

### Big Omega

* This is the lower bound ,i.e, the complexity cannot be lesser than Big Omega.
* Formal definition: **f(N) >= &Omega;(g(N))** as _N tends to infinity_.

### Theta

* This is both upper and lower bound ,i.e, the complexity will be equal to Theta.
* Formal definition: **f(N) = &Theta;(g(N))** as _N tends to infinity_.

### Little O

* This is a loose upper bound ,i.e, the complexity is strictly lesser than Little O.
* Formal definition: **f(N) < &omicron;(g(N))** as _N tends to infinity_.

### Little Omega

* This is a loose lower bound ,i.e, the complexity is strictly greater than Little O.
* Formal definition: **f(N) > &omega;(g(N))** as _N tends to infinity_.