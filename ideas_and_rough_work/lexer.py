# This code has been decrepated and a new code with the PLY Lexer will be implemented
# import re

# class Lexer:
#     def __init__(self):
#         self.token_patterns = [
#             ("COMMENT", r"//.*"),
#             ("KEYWORD", r"(OPENQASM|include|qreg|creg|gate|measure|reset|barrier|if|else|elif|opaque|unitary)"),
#             ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
#             ("NUMBER", r"\d+(\.\d+)?"),
#             ("STRING", r"\".*\""),
#             ("SYMBOL", r"[\[\]\{\}\(\),;+\-*/^=]"),
#             ("WHITESPACE", r"\s+")
#         ]
    
#     def tokenize(self, code):
#         tokens = []
#         while code:
#             match = None
#             for token_name, pattern in self.token_patterns:
#                 regex = re.compile(pattern)
#                 match = regex.match(code)
#                 if match:
#                     value = match.group(0)
#                     tokens.append((token_name, value))
#                     code = code[len(value):]
#                     break
#             if not match:
#                 raise ValueError("Invalid token: " + code)
#         return tokens

