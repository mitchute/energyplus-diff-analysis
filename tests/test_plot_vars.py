import os
import tempfile
import unittest
from pathlib import Path

import pandas as pd

from src.plot_vars import plot, GenericError


class TestPlotVars(unittest.TestCase):

    def test_plot_all_cols(self):
        temp_dir = Path(tempfile.mkdtemp())
        if not temp_dir.exists():
            os.mkdir(temp_dir)
        base_path = temp_dir / "base.csv"
        mod_path = temp_dir / "mod.csv"
        df_base = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        df_mod = pd.DataFrame({"A": [1.5, 2.5, 3.5], "B": [4.5, 5.5, 6.5]})
        df_base.index.name = "Date/Time"
        df_mod.index.name = "Date/Time"
        df_base.to_csv(base_path)
        df_mod.to_csv(mod_path)
        plot(str(base_path), str(mod_path), plot_dir=str(temp_dir))

    def test_plot_single_cols(self):
        temp_dir = Path(tempfile.mkdtemp())
        if not temp_dir.exists():
            os.mkdir(temp_dir)
        base_path = temp_dir / "base.csv"
        mod_path = temp_dir / "mod.csv"
        df_base = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        df_mod = pd.DataFrame({"A": [1.5, 2.5, 3.5], "B": [4.5, 5.5, 6.5]})
        df_base.index.name = "Date/Time"
        df_mod.index.name = "Date/Time"
        df_base.to_csv(base_path)
        df_mod.to_csv(mod_path)
        plot(str(base_path), str(mod_path), cols="A", plot_dir=str(temp_dir))

    def test_plot_cols_list(self):
        temp_dir = Path(tempfile.mkdtemp())
        if not temp_dir.exists():
            os.mkdir(temp_dir)
        base_path = temp_dir / "base.csv"
        mod_path = temp_dir / "mod.csv"
        df_base = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [0, 1, 2]})
        df_mod = pd.DataFrame({"A": [1.5, 2.5, 3.5], "B": [4.5, 5.5, 6.5], "C": [0, 1, 2]})
        df_base.index.name = "Date/Time"
        df_mod.index.name = "Date/Time"
        df_base.to_csv(base_path)
        df_mod.to_csv(mod_path)
        plot(str(base_path), str(mod_path), cols=["A", "B"], plot_dir=str(temp_dir))

    def test_mismatched_rows(self):
        temp_dir = Path(tempfile.mkdtemp())
        if not temp_dir.exists():
            os.mkdir(temp_dir)
        base_path = temp_dir / "base.csv"
        mod_path = temp_dir / "mod.csv"
        df_base = pd.DataFrame({"A": [1, 2, 3]})
        df_mod = pd.DataFrame({"A": [1.5, 2.5]})
        df_base.index.name = "Date/Time"
        df_mod.index.name = "Date/Time"
        df_base.to_csv(base_path)
        df_mod.to_csv(mod_path)
        with self.assertRaises(GenericError):
            plot(str(base_path), str(mod_path), plot_dir=str(temp_dir))

    def test_mismatched_cols(self):
        temp_dir = Path(tempfile.mkdtemp())
        if not temp_dir.exists():
            os.mkdir(temp_dir)
        base_path = temp_dir / "base.csv"
        mod_path = temp_dir / "mod.csv"
        df_base = pd.DataFrame({"A": [1, 2, 3], "C": [1, 1, 1]})
        df_mod = pd.DataFrame({"A": [1.5, 2.5, 3.5], "D": [1, 1, 1]})
        df_base.index.name = "Date/Time"
        df_mod.index.name = "Date/Time"
        df_base.to_csv(base_path)
        df_mod.to_csv(mod_path)
        plot(str(base_path), str(mod_path), plot_dir=str(temp_dir))

    def test_mismatched_cols_with_list_input(self):
        temp_dir = Path(tempfile.mkdtemp())
        if not temp_dir.exists():
            os.mkdir(temp_dir)
        base_path = temp_dir / "base.csv"
        mod_path = temp_dir / "mod.csv"
        df_base = pd.DataFrame({"A": [1, 2, 3], "C": [1, 1, 1]})
        df_mod = pd.DataFrame({"A": [1.5, 2.5, 3.5], "D": [1, 1, 1]})
        df_base.index.name = "Date/Time"
        df_mod.index.name = "Date/Time"
        df_base.to_csv(base_path)
        df_mod.to_csv(mod_path)
        plot(str(base_path), str(mod_path), cols=["A", "E"], plot_dir=str(temp_dir))

    def test_plot_low_high_rows(self):
        temp_dir = Path(tempfile.mkdtemp())
        if not temp_dir.exists():
            os.mkdir(temp_dir)
        base_path = temp_dir / "base.csv"
        mod_path = temp_dir / "mod.csv"
        df_base = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        df_mod = pd.DataFrame({"A": [1.5, 2.5, 3.5], "B": [4.5, 5.5, 6.5]})
        df_base.index.name = "Date/Time"
        df_mod.index.name = "Date/Time"
        df_base.to_csv(base_path)
        df_mod.to_csv(mod_path)
        plot(str(base_path), str(mod_path), low_row_num=1, high_row_num=2, plot_dir=str(temp_dir))
