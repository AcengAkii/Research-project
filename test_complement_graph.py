import function_complement_graph as cg
import numpy as np
a =  [[0.0, 1.0, 1.0, 1.0],
  [1.0, 0.0, 0.0, 1.0],
  [1.0, 0.0, 0.0, 1.0],
  [1.0, 1.0, 1.0, 0.0]]

print(np.array(a))
b = cg.complement_graphs(a)
print(np.array(b))
