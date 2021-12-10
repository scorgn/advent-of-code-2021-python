from enum import Enum
from os import write
import sys
from typing import Optional


class Color(Enum):
    BLACK = '\u001b[30m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    BLUE = '\u001b[34m'
    MAGENTA = '\u001b[35m'
    CYAN = '\u001b[36m'
    WHITE = '\u001b[37m'
    RESET = '\u001b[0m'
    BOLD = '\033[1m'


default_message_colors = {
    'info': Color.CYAN,
    'error': Color.RED,
    'warn': Color.YELLOW,
    'success': Color.GREEN,
    'message': Color.WHITE,
}


class Logger():
    message_bold: bool
    message_color: Optional[Color]
    message_stderr: bool
    message_color_map: dict

    def __init__(
        self,
        bold: bool = None,
        color: Optional[Color] = None,
        stderr: bool = None,
        message_color_map = None,
    ):
        self.message_bold = bold
        self.message_color = color
        self.message_stderr = stderr
        self.message_color_map = message_color_map or default_message_colors

    @classmethod
    def create(cls, message_color_map: dict[str, Color] = None):
        return cls.__class__(message_color_map)

    def write(
        self,
        message: str,
        color: Optional[Color] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        if bold is None:
            bold = self.message_bold

        if stderr is None:
            stderr = self.message_stderr

        if color is None:
            color = self.message_color

        if bold:
            message = self._wrap_color(Color.BOLD, message)
        
        if color:
            message = self._wrap_color(color, message)

        write_function = sys.stderr.write if stderr else sys.stdout.write
        write_function("%s\n" %message)
        return self

    def color(
        self,
        color: Color,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ): 
        if not isinstance(color, Color):
            raise ValueError("Color is not a valid color choice. Must be instance of utils.output.Color.")

        if message is not None:
            return self.write(message, color, stderr, bold)
        return self._chain_method(color, stderr, bold)

    def stderr(
        self,
        message: Optional[str] = None,
        color: Optional[Color] = None,
        bold: Optional[bool] = None,
    ):
        stderr = True
        if message is not None:
            return self.write(message, color, stderr, bold)
        return self._chain_method(color, stderr, bold)
    
    def bold(
        self,
        message: Optional[str] = None,
        color: Optional[Color] = None,
        stderr: Optional[bool] = None,
    ):
        bold = True
        if message is not None:
            return self.write(message, color, stderr, bold)
        return self._chain_method(color, stderr, bold)

    def black(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        return self.color(Color.BLACK, message, stderr, bold)

    def red(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        return self.color(Color.RED, message, stderr, bold)

    def green(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        return self.color(Color.GREEN, message, stderr, bold)

    def yellow(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        return self.color(Color.YELLOW, message, stderr, bold)

    def blue(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        return self.color(Color.BLUE, message, stderr, bold)

    def magenta(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        return self.color(Color.MAGENTA, message, stderr, bold)

    def cyan(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        return self.color(Color.CYAN, message, stderr, bold)

    def white(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        return self.color(Color.WHITE, message, stderr, bold)

    def error(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        if bold is None and self.message_bold is None:
            bold = True
        if stderr is None and self.message_stderr is None:
            stderr = True
        return self.color(self.message_color_map['error'], message, stderr, bold)

    def warn(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        if bold is None and self.message_bold is None:
            bold = True
        if stderr is None and self.message_stderr is None:
            stderr = True
        return self.color(self.message_color_map['warn'], message, stderr, bold)

    def success(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        if bold is None and self.message_bold is None:
            bold = True
        return self.color(self.message_color_map['success'], message, stderr, bold)

    def info(
        self,
        message: Optional[str] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        if bold is None and self.message_bold is None:
            bold = True
        return self.color(self.message_color_map['info'], message, stderr, bold)

    def reset(self):
        return __class__(
            bold=None,
            color=None,
            stderr = None,
            message_color_map=self.message_color_map
        )

    def _wrap_color(self, color: Color, message: str) -> str:
        formatted = str(color.value) + str(message)
        if not formatted.endswith(Color.RESET.value):
            formatted = formatted + Color.RESET.value
        return formatted

    def _chain_method(
        self,
        color: Optional[Color] = None,
        stderr: Optional[bool] = None,
        bold: Optional[bool] = None,
    ):
        return __class__(
            bold=bold if bold is not None else self.message_bold,
            color=color if color is not None else self.message_color,
            stderr=stderr if stderr is not None else self.message_stderr,
            message_color_map=self.message_color_map,
        )
