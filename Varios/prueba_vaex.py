##https://github.com/vaexio/vaex-datasets/releases/download/v1.0/helmi-dezeeuw-2000-FeH-v2-10percent.hdf5


##https://github.com/vaexio/vaex-datasets/releases/download/v1.0/helmi-dezeeuw-2000-FeH-v2-10percent.hdf5
##  to C:\Users\danyc/.vaex\data\helmi-dezeeuw-2000-FeH-v2-10percent.hdf5
import vaex
df = vaex.example()
##df.x.values  # Since this is the last statement in a cell, it will print the DataFrame in a nice HTML format.

import numpy as np
np.sqrt(df.x**2 + df.y**2 + df.z**2)