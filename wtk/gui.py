from .system import get_bool_environ

import click
import sys
import time


class WGui:
   
   @staticmethod
   def debug(data):
      if get_bool_environ('WCONFIG_DEBUG'):
         click.echo(click.style(">> {}".format(data), fg='white'))
      else:
         pass

   @staticmethod
   def message(text: str):
      click.echo(click.style("* {}\n".format(text), fg='bright_white'))

   @staticmethod
   def echo(text: str, **kwargs):
      if 'message' in kwargs.keys():
         text += kwargs.pop('message')
      click.echo(click.style(text, fg='bright_white'), **kwargs)

   @staticmethod
   def ok(text: str):
      click.echo(click.style(text, fg='green'))

   @staticmethod
   def warning(text: str):
      click.echo(click.style(text, fg='yellow'))

   @staticmethod
   def error(text: str):
      click.echo(click.style(text, fg='red'))
      
   @staticmethod
   def print(text: str, f=sys.stdout):
      print(text, file=f)

   @staticmethod
   def Hi(title: str, row_del = 0.033):
      for row in title.split("\n"):
         WGui.ok(row)
         time.sleep(row_del)