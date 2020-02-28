import sys
from textwrap import wrap

import matplotlib.pyplot as plt
import pandas as pd


def plot(base_path: str, mod_path: str):
    df_vars = pd.read_csv("plot_vars.csv")
    df_vars["VarName"] = df_vars["VarName"].str.strip()
    df_base = pd.read_csv(base_path)
    df_mod = pd.read_csv(mod_path)
    df_base.rename(columns=lambda x: x.strip(), inplace=True)
    df_mod.rename(columns=lambda x: x.strip(), inplace=True)

    for idx, row in df_vars.iterrows():
        print(row["VarName"])
        base = df_base.iloc[row["LowIndex"]: row["HighIndex"]][row["VarName"]]
        mod = df_mod.iloc[row["LowIndex"]: row["HighIndex"]][row["VarName"]]
        diff = base - mod
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        ax1.plot(base, label='New Coil')
        ax1.plot(mod, label='DXCoils', linestyle='--')
        ax1.legend()
        ax1.grid()
        ax2.plot(diff)
        ax2.set_ylabel("diff: New Coil - DXCoils")
        ax2.grid()
        plt.suptitle("\n".join(wrap(row["VarName"])))
        plt.savefig("Var_{}.png".format(idx), bbox_inches='tight')


if __name__ == "__main__":
    plot(sys.argv[1], sys.argv[2])
