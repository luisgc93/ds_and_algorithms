"""
You're given a string of available characters and a string representing a document
that you need to generate. Write a function that determines if you can generate the
document using the available characters.

If you can generate the document, return True, otherwise False

Example input: characters = 'abcabc', document = 'aabbccc'
Example output: False

Notes: the document may contain any characters, including special characters
"""


def can_generate_document(characters: str, document: str) -> bool:
    characters_map = {}
    for character in characters:
        if character in characters_map:
            characters_map[character] += 1
        else:
            characters_map[character] = 1

    document_char_map = {}
    for character in document:
        if character in document_char_map:
            document_char_map[character] += 1
        else:
            document_char_map[character] = 1

    for key, val in document_char_map.items():
        if key not in characters_map or characters_map[key] < val:
            return False
    return True
