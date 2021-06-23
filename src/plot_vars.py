import os
import sys
from pathlib import Path
from textwrap import wrap
from typing import Union

import matplotlib.pyplot as plt
import pandas as pd


def plot(base_path: str,
         mod_path: str,
         cols: Union[str, list] = None,
         low_row_num: int = None,
         high_row_num: int = None):
    # load data
    df_base = pd.read_csv(base_path)
    df_mod = pd.read_csv(mod_path)
    df_base.rename(columns=lambda x: x.strip(), inplace=True)
    df_mod.rename(columns=lambda x: x.strip(), inplace=True)

    # handle column selection
    if cols is None:
        cols = df_base.columns.tolist()
        if "Date/Time" in cols:
            cols.remove("Date/Time")
    else:
        if type(cols) is str:
            cols = [cols]
        elif type(cols) is list:
            cols = [x.strip() for x in cols]

    # set low plot range based on row number
    if low_row_num is None:
        min_idx = 0
    else:
        min_idx = low_row_num - 1

    # set high plot range based on row number
    if high_row_num is None:
        max_idx = len(df_base.index)
    else:
        max_idx = high_row_num - 1

    # setup plots folder
    parent_dir = Path(__file__).parent.parent
    plot_dir_path = parent_dir / "plots"

    if not plot_dir_path.exists():
        os.mkdir(plot_dir_path)

    # make plots
    for idx, c in enumerate(cols):
        print(c)
        base = df_base[c].iloc[min_idx:max_idx].values
        mod = df_mod[c].iloc[min_idx: max_idx].values
        diff = base - mod
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
        x = range(min_idx + 1, max_idx + 1)
        ax1.plot(x, base, label='baseline')
        ax1.plot(x, mod, label='modified', linestyle='--')
        ax1.legend()
        ax1.grid()
        ax2.plot(x, diff)
        ax2.set_ylabel("Delta (baseline - modified)")
        ax2.grid()
        plt.suptitle("\n".join(wrap(c)))
        fig_name = c.replace(" ", "_").replace("/", "-")
        fig_path = plot_dir_path / f"{fig_name}.png"
        plt.savefig(fig_path, bbox_inches='tight')


if __name__ == "__main__":
    plot(sys.argv[1], sys.argv[2])
