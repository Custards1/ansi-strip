import re

def remove_xterm_csi(mangled_text:str,replace_with="",filter="@ABCDHJKLMPTcfgh1mnrx"):
    """
    remove standard xterm sequences that follow the ESC[c; pattern
    """
    return re.sub(r'\x1b\[[0-9;]*['+filter+r']',replace_with,mangled_text)

def remove_xterm_csiq(mangled_text:str,replace_with="",filter="h1rsl"):
    """
    remove standard xterm sequences that follow the ESC[?c; pattern
    """
    return re.sub(r'\x1b\[\?[0-9;]*['+filter+r']',replace_with,mangled_text)

# def _recurse_regex(text,func):
#     size = len(text)
#     while True:
#         text=func(text)
#         if len(text)>=size:
#             return text
#         size=len(text)
# def remove_xterm_dsr(mangled_text:str,replace_with=r"\1"):
#     return _recurse_regex(mangled_text,lambda text: re.sub(r'\x1bP([\s\S]*)\x1b\\',replace_with,text))

# def remove_xterm_set_text(mangled_text:str,replace_with=r"\1"):
#     return _recurse_regex(mangled_text,lambda text: re.sub(r'\x1b\][0-9];([\s\S]*)\x07',replace_with,text))

# def remove_xterm_replacable(mangled_text:str,replace_with=r"\1",filter=r"[\^_]",suffix=r"\x1b\\"):
#     return _recurse_regex(mangled_text,lambda text: re.sub(r'\x1b'+filter+r'([\s\S]*)'+suffix,replace_with,text))

# def remove_xterm_text_options(mangled_text:str,_):
#     return remove_xterm_dsr(remove_xterm_replacable(remove_xterm_set_text(mangled_text)))
    
def remove_xterm_seq_single(xterm_content,replace_with=""):
    """
    replace xterm escape codes that follow the ESC c pattern; (single character after ESC)
    """
    fmt = "\x03\x05\x0C\x0E\x0F\x17\x18\x1A\x1C"
    return re.sub(r"\x1b[78=>DEFHMNOZc1mno\|\}~89:;`abdhjkpqrst\+"+fmt+"]",replace_with,xterm_content)

def remove_xterm_seq_double(xterm_content,replace_with=""):
    """
    replace xterm escape codes that follow the ESC c c pattern; (two characters after ESC)
    """
    return re.sub(r"(\x1b[\(\)\*\+].)|\x1b#8",replace_with,xterm_content)


XTERM_FORMAT = [remove_xterm_seq_single,remove_xterm_seq_double,remove_xterm_csi,remove_xterm_csiq]

def remove_xterm_ansi(xterm_content,replace_with=""):
    """
    replace all xterm escape codes
    """
    output = xterm_content
    for func in XTERM_FORMAT:
        output = func(output,replace_with)
    return output
