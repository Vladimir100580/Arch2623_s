


def generate_list_unicode(text: str) -> list[int]:
    list_unicode = set()
    for char in text:
        list_unicode.add(ord(char))
    return sorted(list_unicode, reverse=True)

text = "каждого символа введённой строки отсортированный по убыванию."

print(generate_list_unicode(text))