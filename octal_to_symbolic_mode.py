from ansible.module_utils.common.text.converters import to_text

class FilterModule(object):
  def filters(self):
    return {
      'oct_to_sym': self.oct_to_sym,
    }

  def oct_to_sym(self, mode, format_long = None):
    # return format_long
    if (len(mode) == 5) and (mode[0:2] == "0o"):
      mode = mode[2:]
    elif (len(mode) == 4) and (mode[0] == "0"):
      mode = mode[1:]
    if (len(mode) > 3) or (not mode.isdigit()):
      raise TypeError('Unsupported mode: expected 1 or 3-digit octal mode with 0o or 0 prefix')

    separator = "-" if format_long or (len(mode) > 1) else ""
    result = []
    for digit in map(int, str(mode)):
      for value, letter in ((4, "r"), (2, "w"), (1, "x")):
        result.append(letter if digit & value else separator)
    return to_text("".join(result))
