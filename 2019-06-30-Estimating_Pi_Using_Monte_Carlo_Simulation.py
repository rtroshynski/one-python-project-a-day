# Python 3.7
# https://www.youtube.com/watch?v=k7_pSwjieiQ
# https://gist.github.com/nikhilkumarsingh/b766da0497932b9681cf7ab029cef294
import random

def run_experiment(n=10000):
	points = [(random.uniform(-1,1),random.uniform(-1,1)) for _ in rand(n)]
	points_inside_circle = [(x,y) for (x,y) in points if x**2 + y**2 <= 1]
	return 4*len(points_inside_circle) / len(points) 
	
results = []
avg_pi_values = []

for _ in range(10000):
    results.append(run_experiment())
    avg_pi = sum(results) / len(results)
    avg_pi_values.append(avg_pi)
	
avg_pi_errors = [abs(math.pi - pi) for pi in avg_pi_values]

import matplotlib.pyplot as plt

plt.plot(avg_pi_errors)
# eof
