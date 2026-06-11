import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Physics Constants
G = 1000                 # Gravitational constant scaled up for visible movement
dt = 0.01                # Time step (delta t) for each frame of calculus

# 2. Central Star Properties (Static in the center)
star_mass = 10000
star_x, star_y = 0.0, 0.0

# 3. Orbiting Planet Properties
planet_mass = 1
planet_x, planet_y = 200.0, 0.0     # Starting position (200 units out on X-axis)
planet_vx, planet_vy = 0.0, 220.0    # Tangential starting velocity (moving straight up on Y-axis)

# Lists to store the path history so we can draw a cool tail/orbit line
trail_x = []
trail_y = []


def update_physics():
    # We use 'global' so Python lets us modify the variables we created at the top
    global planet_x, planet_y, planet_vx, planet_vy

    # 1. Calculate distance (dx, dy) and total distance (r) using Pythagoras
    dx = star_x - planet_x
    dy = star_y - planet_y
    r = math.sqrt(dx**2 + dy**2)

    # Safety brake: if the planet crashes into the star, stop calculating to avoid dividing by zero
    if r < 5:
        return

    # 2. Newton's Gravitational Force: F = G * (m1 * m2) / r^2
    F = G * (star_mass * planet_mass) / (r**2)

    # 3. Force components using similar triangles (Directional vector breakdown)
    Fx = F * (dx / r)
    Fy = F * (dy / r)

    # 4. Update velocities based on acceleration (a = F / m)
    # Velocity changes by (acceleration * tiny time step)
    planet_vx += (Fx / planet_mass) * dt
    planet_vy += (Fy / planet_mass) * dt

    # 5. Update coordinates based on the new velocity
    # Position changes by (velocity * tiny time step)
    planet_x += planet_vx * dt
    planet_y += planet_vy * dt

    # 6. Save the new coordinates to our trail arrays for drawing later
    trail_x.append(planet_x)
    trail_y.append(planet_y)
    # 1. Create the plotting canvas window
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')  # Make space look dark
ax.set_xlim(-300, 300)     # Set horizontal graph boundaries
ax.set_ylim(-300, 300)     # Set vertical graph boundaries
ax.set_title("Orbital Mechanics Simulation (Newtonian Gravity)", color='white')

# 2. Draw the static central Star (a big yellow circle)
ax.plot(star_x, star_y, 'oy', markersize=15, label="Star")

# 3. Create placeholders for the moving parts (Planet dot and its tail trail)
planet_plot, = ax.plot([], [], 'ob', markersize=6, label="Planet")  # Blue dot
trail_plot, = ax.plot([], [], '-w', alpha=0.5, linewidth=1)         # White faint trail

# 4. The Animation Loop Function (The Flipbook Frame Generator)
def animate(frame):
    # Run our calculations to get the next position
    update_physics()
    
    # Update the visual graph points with the new coordinates
    planet_plot.set_data([planet_x], [planet_y])
    trail_plot.set_data(trail_x, trail_y)
    
    return planet_plot, trail_plot

# 5. Turn on the Engine
# This calls the 'animate' function every 10 milliseconds to redraw the screen
ani = animation.FuncAnimation(fig, animate, frames=200, interval=10, blit=True)

plt.legend()
plt.grid(color='gray', linestyle='--', linewidth=0.3)
plt.show()

