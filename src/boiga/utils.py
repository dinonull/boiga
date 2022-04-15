import random

_SOUP = '!#%()*+,-./:;=?@[]^_`{|}~' + \
	       'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

def gen_uid():
	return "".join(random.choices(_SOUP, k=20))

BLANK_SVG = b"""<svg version="1.1" width="2" height="2" viewBox="-1 -1 2 2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <!-- Exported by Scratch - http://scratch.mit.edu/ -->
</svg>"""
