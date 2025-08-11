import click
import numpy as np
import cv2 as cv
import math
from typing import Any


@click.group()
def cli():
    """CLI Group"""


ITER_COUNT = 255


def calculate_iter(complex_x: float, complex_y: float) -> int:

    CRE = complex_x
    CIM = complex_y

    ZRE = 0.0
    ZIM = 0.0

    output = 0

    for _ in range(ITER_COUNT):
        ZRE_new = ZRE**2 - ZIM**2 + CRE
        ZIM_new = 2 * ZRE * ZIM + CIM

        ZRE, ZIM = ZRE_new, ZIM_new

        if (ZRE**2 + ZIM**2) > 4.0:
            break

        output += 1

    return output


def pixel2complex(
    pixel_x, pixel_y, render_size_x, render_size_y
) -> tuple[float, float]:
    STEP_X = 3.0 / render_size_x
    STEP_Y = 2.0 / render_size_y

    TOP_LEFT_X = -1.5
    TOP_LEFT_Y = 1.0

    out_re = STEP_X * pixel_x + TOP_LEFT_X
    out_im = TOP_LEFT_Y - STEP_Y * pixel_y

    return (out_re, out_im)


def calculate_iters(size_x, size_y) -> Any:
    out_array = np.zeros([size_y, size_x], dtype=np.uint8)
    for y in range(size_y):
        for x in range(size_x):
            c_x, c_y = pixel2complex(x, y, size_x, size_y)

            # print(f"Pixel {x},{y} becomes {c_x},{c_y}")
            out_array[y][x] = np.uint8(calculate_iter(c_x, c_y))

    return out_array


@cli.command()  # type: ignore[attr-defined]
@click.argument("draw_res")
@click.argument("render_res")
def mandelbrot(draw_res: str, render_res: str):
    """Draw the main region of the mandelbrot set at a resolution of
    draw_res_x,draw_res_y and render it at render_res_x,render_res_y
    """
    draw_resolution_x, draw_resolution_y = [int(i) for i in draw_res.split(",")]
    render_resolution_x, render_resolution_y = [int(i) for i in render_res.split(",")]

    mandelbrot_output = calculate_iters(render_resolution_x, render_resolution_y)

    click.echo(mandelbrot_output)

    # canvas = np.zeros([draw_resolution_y, draw_resolution_x, 3], dtype=np.uint8)

    # click.echo(canvas)

    cv.imshow("Canvas", mandelbrot_output)  # pylint: disable=no-member

    cv.waitKey()  # pylint: disable=no-member
