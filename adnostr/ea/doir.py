def cprint(text, color='white', attrs=[], **kwargs):
    """Print text with specified color and attributes.

    Args:
        text (str): Text to print.
        color (str): Color of the text.
        attrs (list): List of attributes to apply to the text.
        **kwargs: Additional keyword arguments to pass to the print function.
    """
    if color not in COLORS:
        raise ValueError(f'Invalid color: {color}')

    attrs = ' '.join(attrs)
    print(f'\033[{COLORS[color]};{attrs}m{text}\033[0m', **kwargs)


cprint(f'\n>>> swap {to_symbol} | {error}', 'red')
