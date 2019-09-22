def ask_if_default_true(prompt):
  result = input("%s [Y/n]" % prompt)
  if result.startswith('n') or result.startswith('N'):
    return False
  return True

def ask_if_default_false(prompt):
  result = input("%s [n/N]" % prompt)
  if result.startswith('y') or result.startswith('Y'):
    return True
  return False

def ask_if_dive(path):
  return ask_if_default_true('(%s) is a directory, dive into it?' % path)

