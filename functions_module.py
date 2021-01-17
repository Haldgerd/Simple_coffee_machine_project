"""
File containing all functions needed for "coffee machine" project.
"""
import os

from pyfiglet import figlet_format
from termcolor2 import c

from data_module import MENU, resources


def output_ascii_title():
    """
    Return customized ASCII text(title) using pyfiglet and termcolor2 modules.
    :return: string, ASCII text.
    """
    ascii_title = figlet_format("The coffee machine", font="slant")
    colored_ascii_title = c(ascii_title, color="magenta")
    return colored_ascii_title

