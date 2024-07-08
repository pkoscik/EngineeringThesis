#!/usr/bin/env python3

import sys
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SyntaxError("Wrong number of arguments")

    tlib = sys.argv[1]
    dromajo = sys.argv[2]

    df_tlib = pd.read_csv(tlib)
    df_dromajo = pd.read_csv(dromajo)

    print(df_tlib)

    plt.show()