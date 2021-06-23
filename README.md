# CSV Compare
This is a very basic tool used for plotting and comparing csv data from two separate csv files.

## Usage
A version of the jupyter notebook is hosted at [mybinder.org](https://mybinder.org/v2/gh/mitchute/plot-eplusout-csv)

*How is this used?*

1. Open the binder (https://mybinder.org/v2/gh/mitchute/plot-eplusout-csv). This may take a few minutes to build and load the container images running behind the scenes. Once completed, mybinder.org will launch the jupyter dashboard in your web browser. This looks like a file explorer.
2. Launch the "Make_Plots.ipynb" jupyter notebook by clicking on it from the jupyter dashboard. This will launch a new tab in your browser with this notebook loaded and running.
3. Upload your data by clicking "upload" from the jupyter dashboard. For example, you could upload and name your baseline csv file "base.csv", and your modified version csv "mod.csv".
4. Back over on the "Make_Plots" jupyter notebook, update the names of your baseline and modified csv data files to match what you uploaded.
5. Select how you want your data plotted. See the examples section below for additional information.
6. To execute, you can select Cell >> Run All (or other available options). You can also run individual cells with the "shift+return" command."

## Examples

### Example 1 - Plotting all columns
As described, this plots all columns

```plot(baseline_path, mod_path)```

### Example 2 - Plot only one series
If you only want to plot a single column from the csv data, the column name can be passed explicitly to the ```cols``` field.

```plot(baseline_path, mod_path, cols="Col Name 1")```

### Example 3 - Plot a selected set of columns from the csv data
The ```cols``` field also accepts a list input for when you want to plot more than one column, but not all of them.

```plot(baseline_path, mod_path, cols=["Col Name 1", "Col Name 2"])```

### Example 4 - Plot one series for a specified number of rows
You may also specify the range of rows you want to plot.

```plot(baseline_path, mod_path, cols="Col Name 1", low_row_num=10, high_row_num=20)```
