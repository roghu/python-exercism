import re

HTML = str
MARKDOWN = str


re_italic = re.compile(r"(.*)_(.*)_(.*)")
re_strong = re.compile(r"(.*)__(.*)__(.*)")
re_header = re.compile(r"(#{1,6}) (.*)")
re_list_item = re.compile(r"\* (.*)")


def header(matches: re.Match[str]) -> str:
    header_level = len(matches.group(1))
    open_tag = f"<h{header_level}>"
    close_tag = f"</h{header_level}>"
    return f"{open_tag}{matches.group(2)}{close_tag}"


def strong(matches: re.Match[str]) -> HTML:
    return f"{matches.group(1)}<strong>{matches.group(2)}</strong>{matches.group(3)}"


def italic(matches: re.Match[str]) -> HTML:
    return f"{matches.group(1)}<em>{matches.group(2)}</em>{matches.group(3)}"


def inline_markdown(inline: MARKDOWN) -> HTML:
    if matches := re.match(re_strong, inline):
        inline = strong(matches)
    if matches := re.match(re_italic, inline):
        inline = italic(matches)

    return inline


def parse(markdown: MARKDOWN) -> HTML:
    lines: list[MARKDOWN] = markdown.split("\n")
    html: HTML = ""
    in_list = False
    for line in lines:
        if matches := re.match(re_header, line):
            html += header(matches)

        elif match := re.match(re_list_item, line):
            if not in_list:
                in_list = True
                html += "<ul>"
            html += f"<li>{inline_markdown(match.group(1))}</li>"

        else:
            if in_list:
                html += f"</ul><p>{inline_markdown(line)}</p>"
                in_list = False
            else:
                html += f"<p>{inline_markdown(line)}</p>"

    if in_list:
        html += "</ul>"
    return html
