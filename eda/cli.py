import click

from eda.plot_vars import plot


@click.command(name="energyplus-diff-analysis")
@click.argument("baseline-csv", type=click.Path(exists=True))
@click.argument("modified-csv", type=click.Path(exists=True))
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(),
    required=False,
    default=None,
    help="Output directory path to save plots."
)
def cli(baseline_csv, modified_csv, output_dir):
    click.echo(click.format_filename(baseline_csv))
    click.echo(click.format_filename(modified_csv))
    plot(base_path=baseline_csv, mod_path=modified_csv, plot_dir=output_dir, plot_only_diffs=False)
