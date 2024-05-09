import pandas as pd
import ast
import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')

df['attractors'] = df['attractors'].str.replace(' ', '').str.replace("'", '').apply(ast.literal_eval)
df['attractors'] = df['attractors'].apply(lambda x: [''.join(map(str, l)) for l in x]).explode()

attractor_counts = df.groupby(['size', 'connectivity', 'num_steps', 'mutation_rate'])['attractors'].apply(lambda x: len(set(x))).reset_index(name='num_attractors')

pivot_table = attractor_counts.pivot_table(index='size', columns='connectivity', values='num_attractors')
pivot_table.plot(marker='o')
plt.xlabel('Size')
plt.ylabel('Number of attractors')
plt.title('Number of attractors vs. size and connectivity')
plt.show()
