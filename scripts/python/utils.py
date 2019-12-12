import sys

def ask_if_default_true(prompt):
  print("%s [Y/n]" % prompt, file=sys.stderr)
  result = input()
  if result.startswith('n') or result.startswith('N'):
    return False
  return True

def ask_if_default_false(prompt):
  print("%s [y/N]" % prompt, file=sys.stderr)
  result = input()
  if result.startswith('y') or result.startswith('Y'):
    return True
  return False

def ask_if_dive(path):
  return ask_if_default_true('(%s) is a directory, dive into it?' % path)

