<<<<<<< HEAD
import pandas as pd
import time

url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,+pl_rade,+pl_orbper,+st_teff,+st_mass,+sy_dist,+discoverymethod,+disc_year+from+ps&format=csv'
df = pd.read_csv(url)
df = df.drop_duplicates(subset='pl_name')

start_time = time.perf_counter()

print(f"Loaded {len(df)} unique exoplanets")
# Filter for Earth-sized planets
earth_size = df[(df['pl_rade'] >= 0.8) & (df['pl_rade'] <= 1.2)]

print(f"Earth-sized planets: {len(earth_size)}")
print(earth_size[['pl_name', 'pl_rade']].head(10))
# Habitable zone candidates
habitable = df[
    (df['pl_rade'] >= 0.8) & 
    (df['pl_rade'] <= 1.2) & 
    (df['st_teff'] >= 4000) & 
    (df['st_teff'] <= 6000)
]

print(f"Potentially habitable planets: {len(habitable)}")
print(habitable[['pl_name', 'pl_rade', 'st_teff']].head(10))
# Planets discovered in 2020 or later
recent = df[df['disc_year'] >= 2020]

print(f"Planets discovered since 2020: {len(recent)}")
print(recent[['pl_name', 'disc_year']].head(10))
# Recent, Earth-sized, habitable candidates
goldilocks = df[
    (df['disc_year'] >= 2020) &
    (df['pl_rade'] >= 0.8) & 
    (df['pl_rade'] <= 1.2) & 
    (df['st_teff'] >= 4000) & 
    (df['st_teff'] <= 6000)
]
# Step 5: Discovery method analysis

# All planets
print("=" * 50)
print("STEP 5: DISCOVERY METHOD ANALYSIS")
print("=" * 50)

# Method rankings for all planets
all_methods = df['discoverymethod'].value_counts()
print("\nAll planets - discovery method rankings:")
print(all_methods)

top_method = all_methods.index[0]
top_count = all_methods.iloc[0]
print(f"\n🏆 Most common method (all planets): {top_method} ({top_count} planets)")

# Method rankings for habitable planets only
habitable_methods = habitable['discoverymethod'].value_counts()
print("\nHabitable planets - discovery method rankings:")
print(habitable_methods)

if len(habitable_methods) > 0:
    top_hab_method = habitable_methods.index[0]
    top_hab_count = habitable_methods.iloc[0]
    print(f"\n🏆 Most common method (habitable planets): {top_hab_method} ({top_hab_count} planets)")

# Sample of planets with their methods
print("\nSample of planets and their discovery methods:")
print(df[['pl_name', 'discoverymethod']].sample(10))

print(f"Recent Earth-sized habitable candidates: {len(goldilocks)}")
print(goldilocks[['pl_name', 'pl_rade', 'st_teff', 'disc_year']])
end_time = time.perf_counter()
duration = end_time - start_time

print(f"Total execution time: {duration:.6f} seconds")
# Reset index before printing
goldilocks = goldilocks.reset_index(drop=True)

# After filtering, add this line
goldilocks = goldilocks.reset_index(drop=True)

# Then print
print(goldilocks[['pl_name', 'pl_rade', 'st_teff', 'disc_year']])

import matplotlib.pyplot as plt

# Get the counts
method_counts = df['discoverymethod'].value_counts()

# Create bar chart
plt.figure(figsize=(10, 6))
method_counts.plot(kind='bar')
plt.title('Exoplanet Discovery Methods')
plt.xlabel('Discovery Method')
plt.ylabel('Number of Planets')
plt.xticks(rotation=45, ha='right')
=======
import pandas as pd
import time

url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,+pl_rade,+pl_orbper,+st_teff,+st_mass,+sy_dist,+discoverymethod,+disc_year+from+ps&format=csv'
df = pd.read_csv(url)
df = df.drop_duplicates(subset='pl_name')

start_time = time.perf_counter()

print(f"Loaded {len(df)} unique exoplanets")
# Filter for Earth-sized planets
earth_size = df[(df['pl_rade'] >= 0.8) & (df['pl_rade'] <= 1.2)]

print(f"Earth-sized planets: {len(earth_size)}")
print(earth_size[['pl_name', 'pl_rade']].head(10))
# Habitable zone candidates
habitable = df[
    (df['pl_rade'] >= 0.8) & 
    (df['pl_rade'] <= 1.2) & 
    (df['st_teff'] >= 4000) & 
    (df['st_teff'] <= 6000)
]

print(f"Potentially habitable planets: {len(habitable)}")
print(habitable[['pl_name', 'pl_rade', 'st_teff']].head(10))
# Planets discovered in 2020 or later
recent = df[df['disc_year'] >= 2020]

print(f"Planets discovered since 2020: {len(recent)}")
print(recent[['pl_name', 'disc_year']].head(10))
# Recent, Earth-sized, habitable candidates
goldilocks = df[
    (df['disc_year'] >= 2020) &
    (df['pl_rade'] >= 0.8) & 
    (df['pl_rade'] <= 1.2) & 
    (df['st_teff'] >= 4000) & 
    (df['st_teff'] <= 6000)
]
# Step 5: Discovery method analysis

# All planets
print("=" * 50)
print("STEP 5: DISCOVERY METHOD ANALYSIS")
print("=" * 50)

# Method rankings for all planets
all_methods = df['discoverymethod'].value_counts()
print("\nAll planets - discovery method rankings:")
print(all_methods)

top_method = all_methods.index[0]
top_count = all_methods.iloc[0]
print(f"\n🏆 Most common method (all planets): {top_method} ({top_count} planets)")

# Method rankings for habitable planets only
habitable_methods = habitable['discoverymethod'].value_counts()
print("\nHabitable planets - discovery method rankings:")
print(habitable_methods)

if len(habitable_methods) > 0:
    top_hab_method = habitable_methods.index[0]
    top_hab_count = habitable_methods.iloc[0]
    print(f"\n🏆 Most common method (habitable planets): {top_hab_method} ({top_hab_count} planets)")

# Sample of planets with their methods
print("\nSample of planets and their discovery methods:")
print(df[['pl_name', 'discoverymethod']].sample(10))

print(f"Recent Earth-sized habitable candidates: {len(goldilocks)}")
print(goldilocks[['pl_name', 'pl_rade', 'st_teff', 'disc_year']])
end_time = time.perf_counter()
duration = end_time - start_time

print(f"Total execution time: {duration:.6f} seconds")
# Reset index before printing
goldilocks = goldilocks.reset_index(drop=True)

# After filtering, add this line
goldilocks = goldilocks.reset_index(drop=True)

# Then print
print(goldilocks[['pl_name', 'pl_rade', 'st_teff', 'disc_year']])

import matplotlib.pyplot as plt

# Get the counts
method_counts = df['discoverymethod'].value_counts()

# Create bar chart
plt.figure(figsize=(10, 6))
method_counts.plot(kind='bar')
plt.title('Exoplanet Discovery Methods')
plt.xlabel('Discovery Method')
plt.ylabel('Number of Planets')
plt.xticks(rotation=45, ha='right')
>>>>>>> eb32051c6598987de923b54fea96da8e882695a7
plt.show()