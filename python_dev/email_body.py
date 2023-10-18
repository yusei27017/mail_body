import datetime

class Line:
    def __init__(self):
        time = '20231023'
        self.line_body = ""
        self.html_stack = []
        self.a_href_last_text = f"utm_source=email-Adhoc&utm_medium=email&utm_campaign={time}"

    def span(self, text=None, color=None, size=None, bold=None):
        span_text = '<span '
        span_style = []
        if color: span_style.append(f'color: {color};')
        if bold: span_style.append(f'font-weight: bold;')
        if size: span_style.append(f'size: {size}px;')
        if span_style:
            span_text += 'style="'
            while span_style:
                sty = span_style.pop(0)
                span_text += sty
            span_text += '"'
        span_text += '>'
        if text: span_text += text
        self.line_body += span_text
        self.html_stack.append("</span>")
        return

    def a_href(self, text=None, href_str=""):
        href_array = href_str.split("#")
        href = href_array[0]
        is_and = False
        for char in href:
            if char == '?': is_and = True
        mark = '&' if is_and else '?'
        link_href = href + mark + self.a_href_last_text
        if len(href_array) > 1: link_href += "#" + href_array[1]
        a_text = f'<a href="{link_href}" target="_blank">'
        if text: a_text += text
        self.line_body += a_text
        self.html_stack.append("</a>")
        return

    def append_text(self, text):
        self.line_body += text
        return

    def html_pop(self, text=None):
        pop_text = self.html_stack.pop()
        self.line_body += pop_text
        if text: self.line_body += text
        return

if __name__ == "__main__":
    print("start")
    
