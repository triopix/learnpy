import esc_seq as e

# void function
# ! on windows - cmd does not work with ANSI!
# * "wheel" is a file containing a python package


def color_print(text: str, *effects: str) -> None:
    """Print given text: `str`, with `effect` applied by the
    specified ANSI sequence

    :param ``text``: text to print
    :param ``effects``: ANSI sequence(s) applied on ``text``. Must ``import``
       :py:mod:`esc_seq` which contain the releavant ANSI escape sequences
    :raises:
       ``TypeError`` → if invalid type entered
    """
    effect_string = "".join(effects)
    output_string = f"{effect_string}{text}{e.RESET}"
    print(output_string)


color_print("Hello Red in Bold", e.RED, e.BOLD)

print()


# ... print with all constants applied!
for name, effect in e.__dict__.items():
    # filter out constants
    if isinstance(effect, str) and not name.startswith("__"):
        print(f"Testing {name}:")
        color_print("Hello World!", effect)
        print()  # Print a newline for better readability
