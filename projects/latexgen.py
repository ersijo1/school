from IPython.display import Markdown, display

def md(text):
    display(Markdown(text))

def inline(a):
    return f"${str(a)}$"

def sub(a, b):
    return f"{str(a)}_{{\\text{{{str(b)}}}}}"

def sup(a, b):
    return f"{str(a)}^{{\\text{{{str(b)}}}}}"

def supsub(a, b, c):
    return f"{str(a)}^{{\\text{{{str(b)}}}}}_{{\\text{{{str(c)}}}}}"    

def frac(a, b):
    return f"\\frac{{{str(a)}}}{{{str(b)}}}"

def parens(a):
    return f"\\left({str(a)}\\right)"

r2 = sup("r",2)
x2n = supsub("x",2,"n")
y2n = supsub("y",2,"n")
eq1 = inline(f"{r2}= {x2n} + {y2n}")

s = f"""
#2. Simulation of a two-dimensional random walk
=========

A random walk is a mathematical model that describes a path consisting of a succession of random
steps. In physics, random walks are fundamental in understanding diffusion processes, Brownian motion,
and other related phenomena. In this exercise, we will use Monte Carlo to simulate a two-dimensional
random walk.
    Consider a particle starting at the origin (0, 0) and that, at each time step, it moves one unit length
in a randomly chosen direction: up, down, left or right (i.e., along positive or negative x or y axes).
* Using a random number generator, choose the direction between the four possible (up, down, left, right), and move the particle at each time step. Compute and save {eq1} at each time step n to keep track of the particle’s position.
* Perform the above simulation for 1000 time steps, repeating this process M = 1000 times to gather statistical data on the particle’s displacement. Average {inline(r2)} over all M simulations to get ⟨{inline(r2)}⟩ as a function of n.
* Plot ⟨{inline(r2)}⟩ versus n, and fit the data to a linear model ⟨{inline(r2)}⟩ = 4Dn to find D.
* The expected value of D in this case is D = 0.25. Discuss the variability of paths taken during different simulations and how increasing M improves the accuracy of ⟨{inline(r2)}⟩
   """

print(s)