def kelvin(t, scale):
    """Converts temperature into degrees Kelvin

    Args:
        t: float - rational number
        scale: string - temperature scale in which the temperature is given

    Returns:
        temperature calculated in degrees Kelvin in float type
    """
    if scale == 'f':
        t = (t + 459.67) * 5 / 9
    elif scale == 'c':
        t += 273.15
    return t


def fahrenheit(t, scale):
    """Converts temperature into degrees Fahrenheit

    Args:
        t: float - rational number
        scale: string - temperature scale in which the temperature is given

    Returns:
        temperature calculated in degrees Fahrenheit in float type
    """
    if scale == 'k':
        t = t * 1.8 - 459.67
    elif scale == 'c':
        t = t * 1.8 + 32
    return t


def celsius(t, scale):
    """Convert temperature into degrees Celsius

    Args:
        t: float - rational number
        scale: string - temperature scale in which the temperature is given

    Returns:
        temperature calculated in degrees Celsius in float type
    """
    if scale == 'k':
        t -= 273.15
    elif scale == 'f':
        t = (t - 32) / 1.8
    return t


conversions = {'k': kelvin, 'c': celsius, 'f': fahrenheit}
scale_names = {'k': 'kelvins', 'c': 'Celsius degrees', 'f': 'Fahrenheit degrees'}

scale_in = input('Select scale (K/F/C): ')
scale_in = scale_in.lower()
temperature = float(input('Enter the temperature: '))
scale_out = input('Choose which scale to convert to (K/F/C): ')
scale_out = scale_out.lower()

print(f'{round(conversions[scale_out](temperature, scale_in), 2)}'
      f' {scale_names[scale_out]}')
