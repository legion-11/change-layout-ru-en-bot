from app.letters import letters_eng, letters_rus, conflict


def translate(message: str) -> str:
    """
    Translate message to the opposite keyboard layout (eng -> rus, rus -> eng)

    :param message: Text of message
    :return: Edited text
    """

    result = ''
    lang = ''

    """finding of start language"""
    for char in message:
        if char in letters_rus and char not in letters_eng:
            lang = 'rus'
            break
        elif char in letters_eng and char not in letters_rus:
            lang = 'eng'
            break
    if lang == '':
        lang = 'eng'

    """changing layout for each letter in message"""
    for char in message:
        if char.lower() in letters_rus and char.lower() not in letters_eng:
            lang = 'rus'

        elif char.lower() in letters_eng and char.lower() not in letters_rus:
            lang = 'eng'

        letter = letters_rus.get(char.lower() if char not in conflict else char, char) if lang == 'rus' \
            else letters_eng.get(char.lower(), char)
        result += letter.upper() if char.isupper() else letter

    return result

