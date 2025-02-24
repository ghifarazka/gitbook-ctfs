# Mathematics

### Greatest Common Divisor

We can calculate GCD using Euclid's algorithm. This algorithm works on the principle that `gcd(a,b) == gcd(a,a%b)`, provided that `a>b`.

If `gcd(a,b)=1`, `a` and `b` are coprime.

Here is the code implementation.

```py
def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

a = 66528
b = 52920

print(gcd(a, b))
```

Flag: `1512`

### Extended GCD

EGCD is an algorithm to find `u`,`v`, such that `a*u + b*v = gcd(a,b)`. There are infinitely many `u`s and `v`s that satisfy the equation, but knowing one of the result from calculating the EGCD would be enough.

The equation above is called **Bezout's Identity**. In the case where `gcd(a,b) = 1`, it is guaranteed that there integer solution exists (if `gcd(a,b) != 1`, the solution won't always be an integer).

To implement EGCD, we extend the previous Euclidean algorithm. This extended algorithm takes note of the equation in each round, then does back substitution from the base case up until the first round. More complete explanation [here](https://web.archive.org/web/20230511143526/http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html).

```py
def egcd(a, b):
	if b == 0:
		return a, 1, 0

	gcd, x1, y1 = egcd(b, a % b)
	x = y1
	y = x1 - (a // b) * y1

	return gcd, x, y

p = 26513
q = 32321

print(egcd(p, q))

# Output: (1, 10245, -8404)
```

Flag: `-8404`

### Modular Arithmetic 1

The basic concept of modular arithmetic is similar to how you count in terms of time when looking at a clock.

```
5 - 7 = 10
2 + 3 = 5
4 + 9 = 1
```

A clock is a modulo 12. That means that the only number that can exist (even after addition, multiplication, etc) are 0-11. When you want to count beyond 11, the number would loop back to 0.

This is the notation for modulo: `a ≡ c mod b` or `a mod b = c`.

It is the same thing as this: `a = k*b + c`, which is a longer form of division `a/b = k + c`.

If `a` is divisible by `b`, then `a mod b = 0`.

Below is the solution to the challenge.

```py
x = 11 % 6
y = 8146798528947 % 17

print(min(x, y))
```

Flag: `4`

### Modular Arithmetic 2

Suppose we pick a modulus `p`, where `p` is prime. The integers modulo `p` define a field, denoted by `Fp`. A field is a type of Ring that guarantees that every non-zero element has both additive and multiplicative inverse. For example:

```
3+(10) ≡ 0 mod 13 --> 10 is additive inverse
3*(9) ≡ 1 mod 13 --> 9 is multiplicative inverse
```

Fermat's Little Theorem states that for a prime modulus `p`, and `a` is not a multiple of `p`, This statement holds:

```
a^(p-1) ≡ 1 mod p
```

For example, `7^(16) mod 17` returns `1`.

As for the challenge, we can use the theorem and confirm the result using Python's `pow()` function.

```py
print(pow(273246787654,65536,65537))
```

Flag: `1`

### Modular Inverting

The challenge involves calculating the modular multiplicative inverse of an element. That is, an element `d` that satisfy `a * d ≡ 1 mod p`.

There are 2 ways we can approach this, first using Bezout's Identity and second by extending the previously mentioned Fermat's Little Theorem.

#### 1. Using Bezout's Identity

To calculate the inverse, we'll need EGCD. Remember how Bezout's identity states that there exists `u` & `v` such that `a*u + b*v = gcd(a,b)`? Here, we can replace `gcd(a,b)` with 1 and `u` with the inverse of `a`.

```
         a*d ≡ 1 mod p
         a*d = k*p + 1
   a*d - k*p = 1
a*d + p*(-k) = 1
```

After this, we'll do `egcd(a,p)` and what comes out as the value of `d` is the multiplicative inverse of `a`.

```py
a = 3
p = 13

def egcd(a, b):
	if b == 0:
		return a, 1, 0

	gcd, x1, y1 = egcd(b, a % b)
	x = y1
	y = x1 - (a // b) * y1

	return gcd, x, y

print(egcd(a, p)[1] % p) # egcd result is -4, we mod it with p to get 9, which is congruent to -4
```

#### 2. Using Fermat's Little Theorem

We can try multiplying both sides so that we can have the inverse of `a` on the right side.

```
		 a^(p-1) ≡ 1 mod p
        a^(p-1) * a^(-1) ≡ a^(-1) mod p
		 a^(p-2) ≡ a^(-1) mod p
		  a^(-1) = a^(p-2) mod p
		       d = a^(p-2) mod p
```

Now, we can put the formula on Python.

```py
a = 3
p = 13

d = pow(a, p-2, p)
print(d)
```

Flag: `9`
