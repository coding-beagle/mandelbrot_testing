import click


@click.group()
def cli():
    """CLI Group"""


@cli.command()  # type: ignore[attr-defined]
@click.argument("draw_res")
@click.argument("render_res")
def mandelbrot(draw_res: str, render_res: str):
    """Example script."""
    draw_resolution_x, draw_resolution_y = [int(i) for i in draw_res.split(",")]
    render_resolution_x, render_resolution_y = [int(i) for i in render_res.split(",")]
