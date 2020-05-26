import re


def extract_phone(text):
    # phone_regex = r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$'
    # phone_regex = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    phone_regex = r'(([+]?\d{1,2}[-\.\s]?)?(\d{3}[-\.]?){2}\d{4})'
    matches = []
    pos = re.findall(phone_regex, text)
    matches.extend([x[0] for x in pos])
    return matches
    while m is not None:
        matches.append(m.group(0))
        m = re.search(phone_regex, text, pos=pos)
        pos += 1

    return matches
