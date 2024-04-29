def open_file(file_path: str) -> tuple[str, str]:
    """
    Open and download the file in YAML or JSON format.

    This function takes a file path as arguments,
    opens the file in YAML or JSON format, creates a file object,
    and converts the data to a string.
    The loaded data is returned as a tuple, text data
    and a string with the name of the extension.

    :param file_path: Path to the file to open and load.
    :type file_path: str
    :return: Loaded data and format.
    :rtype: tuple
    """
    with open(file_path, 'r') as file:
        text = file.read()
    if file_path.endswith('.json'):
        data_format = 'json'
    elif file_path.endswith('yaml') or file_path.endswith('yml'):
        data_format = 'yaml'

    return text, data_format
