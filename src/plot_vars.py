import os
import sys
from pathlib import Path
from textwrap import wrap
from typing import Union

import matplotlib.pyplot as plt
import pandas as pd


class GenericError(Exception):
    pass


def plot(base_path: str,
         mod_path: str,
         cols: Union[str, list] = None,
         low_row_num: int = None,
         high_row_num: int = None,
         plot_dir: str = None):
    # proper path objects
    base_path = Path(base_path)
    mod_path = Path(mod_path)

    # load data
    df_base = pd.read_csv(base_path)
    df_mod = pd.read_csv(mod_path)

    # make sure the number of rows match
    if df_base.shape[0] != df_mod.shape[0]:
        msg = "Files do not have the same number of rows. Each file must contain the same number of rows.\n" \
              f"File: {base_path.name}, num rows: {df_base.shape[0]}\n" \
              f"File: {mod_path.name}, num rows: {df_mod.shape[0]}"
        raise GenericError(msg)

    # process available columns
    df_base.rename(columns=lambda x: x.strip(), inplace=True)
    df_mod.rename(columns=lambda x: x.strip(), inplace=True)
    base_cols = df_base.columns.tolist()
    mod_cols = df_mod.columns.tolist()
    if "Date/Time" in base_cols:
        base_cols.remove("Date/Time")
    if "Date/Time" in mod_cols:
        mod_cols.remove("Date/Time")

    if cols is None:
        # only plot the matching columns
        cols = list(set(base_cols) & set(mod_cols))
    else:
        # we're only plotted a select number of columns
        if type(cols) is str:
            cols = [cols]
        elif type(cols) is list:
            cols = [x.strip() for x in cols]

        # make sure both files have the requested columns
        if not all([x in base_cols for x in cols]):
            msg = f"File: {base_path.name} does not contain all requested columns"
            GenericError(msg)
        if not all([x in mod_cols for x in cols]):
            msg = f"File: {mod_path.name} does not contain all requested columns"
            GenericError(msg)

    # set low plot range based on row number
    if low_row_num is None:
        min_idx = 0
    else:
        min_idx = low_row_num - 1

    # set high plot range based on row number
    if high_row_num is None:
        max_idx = df_base.shape[0]
    else:
        max_idx = high_row_num - 1

    # setup plots folder
    parent_dir = Path(__file__).parent.parent
    if plot_dir is None:
        plot_dir_path = parent_dir / "plots"
    else:
        plot_dir_path = Path(plot_dir)

    if not plot_dir_path.exists():
        os.mkdir(plot_dir_path)

    # make plots
    for idx, c in enumerate(cols):
        try:
            base = df_base[c].iloc[min_idx:max_idx].values
            mod = df_mod[c].iloc[min_idx: max_idx].values
            diff = base - mod
            fig, (ax1, ax2) = plt.subplots(2, sharex=True)
            x = [*range(min_idx + 1, max_idx + 1, 1)]
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
            print(c)
        except:
            pass


if __name__ == "__main__":
    plot(sys.argv[1], sys.argv[2])
