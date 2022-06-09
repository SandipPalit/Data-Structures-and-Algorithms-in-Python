# Solving Recursive Algorithms
<hr>

### Important Points:
* At a particular time, there can be only 1 function call in the stack, from each level of the recursive tree.
* Maximum elements present in the stack at any time = Height of the tree. So, **Space complexity of recursive algorithms is Height of the recursive tree**.

### Types of Recursions:
* ###Divide and Conquer Recursions

Example: Merge Sort

Recurrence Relation: f(N) = 2*f(N/2) + (N-1)

<b> Form: T(x) = a<sub>1</sub>*T( b<sub>1</sub>*x + &epsilon;(x) ) + a<sub>2</sub>*T( b<sub>2</sub>*x + &epsilon;(x) ) + ..... + a<sub>k</sub>*T( b<sub>k</sub>*x + &epsilon;(x) ) + g(x) </b>

**Akra Bazzi Method:**

![Akra Bazzi Formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/a35d0d6ec3f950deee27e776fd22a13d4f8d4fe2)

Find the value of **p** such that,

![Finding the value of p](https://wikimedia.org/api/rest_v1/media/math/render/svg/dd007478cb63496611a0c916c285377f2fa72fa2)

Note: **If p < power of g(x),  then ans = g(x)**

Let's solve the recurrence relation of Merge Sort using Akra Bazzi,
 
a<sub>1</sub> = 2 , b<sub>1</sub> = 1/2 , g(x) = n-1

Finding the value of **p**,

2 * (i/2)<sup>p</sup> = 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ==> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; p = 1

Putting the value of **p** in the formula,

T(x) = &Theta;( x<sup>1</sup> + x<sup>1</sup> <sub>1</sub>&Integral;<sup>x</sup> (u-1)/(u<sup>2</sup>) * du )

T(x) = &Theta;( x + x [ </sup> <sub>1</sub>&Integral;<sup>x</sup> (du / u)  - </sup> <sub>1</sub>&Integral;<sup>x</sup> (du / u<sup>2</sup>) ] )

T(X) = &Theta;( x + x [ <sub>1</sub>[<sup>x</sup> log(u) - (1/u) ] )

T(x) = &Theta;( x + x[ log(x) + (1/x) -1 ] )

T(x) = &Theta;( x + x * log(x) + 1 - x  )

T(x) = &Theta;( x * log(x) + 1 )

* ###Linear Recursions

Example: Fibonacci Number

Recurrence Relation: f(N) = f(N-1) + f(N-2)

<b> Form: f(x) = a<sub>1</sub>*f(x-1) + a<sub>2</sub>*f(x-2) + a<sub>n</sub>*f(x-n) </b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; where <b>n</b> is the order of recurrence.

**Solution:**

Let's solve the recurrence relation of Fibonacci number

**Step 1:** Put f(n) = &alpha;<sup>n</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; where **&alpha;** is a constant.

f(n) = f(n-1) + f(n-2)

Putting f(n) = &alpha;<sup>n</sup> ,

&alpha;<sup>n</sup> = &alpha;<sup>n-1</sup> + &alpha;<sup>n-2</sup>

&alpha;<sup>n</sup> - &alpha;<sup>n-1</sup> - &alpha;<sup>n-2</sup> = 0

Dividing both sides by &alpha;<sup>n-2</sup>,

&alpha;<sup>2</sup> - &alpha; - 1 = 0

The Roots are: &alpha;<sub>1</sub> =  (1+√5)/2 , &alpha;<sub>2</sub> =   (1-√5)/2

**Step 2:** Solution is f(n) = c<sub>1</sub> * &alpha;<sub>1</sub><sup>n</sup> + c<sub>2</sub> * &alpha;<sub>2</sub><sup>n</sup> + ..... + c<sub>k</sub> * &alpha;<sub>k</sub><sup>n</sup> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; where **k** is number of roots.

f(n) = c<sub>1</sub> * ((1+√5)/2)<sup>n</sup> + c<sub>2</sub> * ((1-√5)/2)<sup>n</sup>

**Fact:** No. of roots = No. of answers we already know

Here we know two answers. f(0) = 0 and f(1) = 1

f(0) = 0 = c<sub>1</sub> + c<sub>2</sub>

f(1) = 1 = c<sub>1</sub> * (1+√5)/2 + c<sub>2</sub> * (1-√5)/2

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 = c<sub>1</sub> * (1+√5)/2 - c<sub>1</sub> * (1-√5)/2

Solving this, we found c<sub>1</sub> = 1/√5 and c<sub>2</sub> = -1/√5

Putting the values of c<sub>1</sub> and c<sub>2</sub> in f(n) = c1 * ((1+√5)/2)<sup>n</sup> + c2 * ((1-√5)/2)<sup>n</sup>

f(n) = (1/√5) * ((1+√5)/2)<sup>n</sup> - (1/√5) * ((1-√5)/2)<sup>n</sup>

f(n) = (1/√5) [ ((1+√5)/2)<sup>n</sup> - ((1-√5)/2)<sup>n</sup> ] &nbsp;&nbsp;&nbsp;&nbsp;,&nbsp;&nbsp;&nbsp;&nbsp; this is the **formula for n-th Fibonacci number**