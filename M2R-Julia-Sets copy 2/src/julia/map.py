"""Module containing all of the classes for mappings."""
from abc import ABC, abstractmethod
import numpy as np
from matplotlib import cm
from PIL import Image
from numba import jit
import math


@jit(nopython=True)
def complex_to_pixel(z: complex,
                     res_x: int = 600,
                     res_y: int = 600,
                     x_range: tuple = (-3, 3),
                     y_range: tuple = (-3, 3)) -> tuple:
    """
    Convert a complex number into pixel coordinates.

    Parameters
    ----------
    z : complex
        The complex number to convert.
    res_x: int
        The horizontal resolution of the image.
    res_y: int
        The vertical resolution of the image.
    x_range: (float, float)
        The range of x values to consider.
    y_range: (float, float)
        The range of y values to consider.
    """
    return (round((z.real-x_range[0])/(x_range[1]-x_range[0])*(res_x-1)),
            round((z.imag-y_range[1])/(y_range[0]-y_range[1])*(res_y-1)))


def draw_from_array(array: np.ndarray, colormap: cm = cm.cubehelix_r) -> Image:
    """
    Draw an image from an array of values between 0 and 1.

    Parameters
    ----------
    array: np.ndarray
        The array to draw the image from.
    colormap: cm
        The colormap to use for the image.
    """
    np_image = colormap(array)*255
    # f=[]
    # m = []
    # n = []
    # for i in range(600):
    #     layer_1 = np_image[i]
    #     for j in range(600):
    #         layer_2 = layer_1[j]
    #         for k in range(3):
    #             layer_3 = layer_2[k]
    #             m.append(layer_3[0:-1])
    #         f.append(m)
    #         m = []
    #     n.append(f)
    #     f = []
    
    # print(n)


    # Image.fromarray(np.uint8(np_image))
    # np_image = (colormap(array)*255)
    # return Image.fromarray(np.uint8(np_image))
    return Image.fromarray(np.uint8(np_image))
      

class Map(ABC):
    """A mapping f: C -> C."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __call__(self, z: complex) -> complex:
        """
        Return the result of the map acting on a value z.

        Parameters
        ----------
        z: complex
            The value to apply the map to.

        Returns
        -------
        f(z): complex
            The result of the mapping applied to z.
        """
        pass

    def derivative(self, z: complex) -> complex:
        """
        Return the derivative of the map at the given point.

        Parameters
        ----------
        z: complex
            The point to evaluate the derivative at.

        Returns
        -------
 s in the map.
        """
        pass

    def draw_mandelbrot(self, colormap: cm = cm.cubehelix_r, **kwargs) -> Image.Image:
        """
        Draw the Mandelbrot set for this map.

        Parameters
        ----------
        res_x: int
            The horizontal resolution of the image.
        res_y: int
            The vertical resolution of the image.
        iterations: int
            The maximum number of times to apply the map iteratively.
        x_range: (float, float)
            The range of x values to consider.
        y_range: (float, float)
            The range of y values to consider.
        z_max: float
            The maximum z value before considering the point to have escaped.
        multiprocessing: bool
            Whether to use parallelisation or not.
        colormap: cm
            The colormap to use for the imaging.

        Returns
        -------
        im: Image.Image
            The image of the Mandelbrot set as a Pillow image object.
        """
        results = self._calculate_mandelbrot(**kwargs)
        im = draw_from_array(results[::-1], colormap=colormap)
        return im

    def _calculate_julia(self, **kwargs) -> np.ndarray:
        """
        Calculate the escape time of given points as z values in the map.
        """
        pass

    def draw_julia(self, colormap: cm = cm.cubehelix_r, **kwargs) -> Image.Image:
        """
        Draw the Julia set for this map with the current parameter values.

        Parameters
        ----------
        res_x: int
            The horizontal resolution of the image.
        res_y: int
            The vertical resolution of the image.
        iterations: int
            The maximum number of times to apply the map iteratively.
        x_range: (float, float)
            The range of x values to consider.
        y_range: (float, float)
            The range of y values to consider.
        z_max: float
            The maximum z value before considering the point to have escaped.

        Returns
        -------
        im: Image.Image
            The image of the Mandelbrot set as a Pillow image object.
        """
        results = self._calculate_julia(**kwargs)
        im = draw_from_array(results[::-1], colormap=colormap)
        return im
