# not using default parameter values
# have to overload functions with java/cpp
def banner_text(text=" ", screen_width=80) -> None: 
    """Creates a banner for a message entered by user with bordered asterisks `*` 

    :param text: text to output on * , defaults to " "
    :type text: `str`
    :param screen_width: _description_, defaults to 80
    :type screen_width: int, optional
    :raises ValueError: _description_
    """
    if len(text) > screen_width - 4:
        raise ValueError(f"String \"{text}\" is larger than screen width = {screen_width}")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)


# default parameter values -> screen_width = 80, text=" "

banner_text("*", 100)
banner_text("My life's about to change for the better", 100)
banner_text("Probably in 10 years or so", 100)
banner_text(screen_width=100)  # use default text, but override default screen_width
banner_text("Please come back to this file when you are finally happy with your life", 100)
banner_text("*", 100)


# https://docs.python.org/3/library/exceptions.html#concrete-exceptions
# docstring: https://www.youtube.com/watch?v=L7Ry-Fiij-M&t=900s

