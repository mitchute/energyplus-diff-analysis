import os
import sys
from math import ceil
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

    # make sure the number of rows match for each file
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

    # get ride of the index col
    if "Date/Time" in base_cols:
        base_cols.remove("Date/Time")
    if "Date/Time" in mod_cols:
        mod_cols.remove("Date/Time")

    # make sure we're only plotting columns that exist and that we want
    if cols is None:
        # only plot the columns contained in both files
        cols = list(set(base_cols) & set(mod_cols))
    else:
        # we"re only plotting a select number of columns
        if type(cols) is str:
            # for when cols takes a single string input
            cols = [cols]
        elif type(cols) is list:
            # for when cols takes a list input
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

    # create the plots dir if it doesn't exist
    if not plot_dir_path.exists():
        os.mkdir(plot_dir_path)

    # upper limit of 30 markers for the plot
    marker_interval = max(ceil(df_base.shape[0] / 30), 1)

    # make plots
    for idx, c in enumerate(cols):
        try:
            print(f"Plotting: {c}")
            # process the column to be plotted
            x = [*range(min_idx + 1, max_idx + 1, 1)]
            base = df_base[c].iloc[min_idx:max_idx].values
            mod = df_mod[c].iloc[min_idx: max_idx].values
            diff = base - mod

            # create the figure and plot the series
            fig, ax1 = plt.subplots(1)
            ax2 = ax1.twinx()
            ln1 = ax1.plot(x, base, marker="s", markevery=marker_interval)[0]
            ln2 = ax1.plot(x, mod, marker="^", linestyle="--", markevery=marker_interval)[0]
            ln3 = ax2.plot(x, diff, marker=".", linestyle="-.", c="r", markevery=marker_interval)[0]

            # primary x/y axis grid lines
            ax1.grid()

            # make a legend that contains all series
            line_labels = ["baseline", "modified", "delta"]
            fig.legend([ln1, ln2, ln3], line_labels, loc="lower right", ncol=3)

            # add a note for when we're not adding markers to all data points
            if marker_interval > 1:
                ax2.annotate(f"Note: marker icons only shown every {marker_interval} points\n"
                             f"for clarity",
                             xy=(10, 10),
                             xycoords="figure pixels",
                             fontsize=8)

            # final housekeeping
            ax2.set_ylabel("Delta (baseline - modified)")
            plt.suptitle("\n".join(wrap(c)))
            fig_name = c.replace(" ", "_").replace("/", "-")
            fig_path = plot_dir_path / f"{fig_name}.png"
            plt.savefig(fig_path, bbox_inches="tight")
        except:
            print(f"Failed on: {c}")


if __name__ == "__main__":
    plot(sys.argv[1], sys.argv[2])
