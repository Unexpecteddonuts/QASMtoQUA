# final code for lexer will be put in the lexer.py file, this is just a file that has code to be reused.

# import re
# from token import Token

# class Lexer:
#     def __init__(self, input_code):
#         self.input_code = input_code
#         self.tokens = []
#         self.current_position = 0

#     def tokenize(self):
#         while self.current_position < len(self.input_code):
#             match = None

#             for pattern in PATTERNS:
#                 regex, token_type = pattern
#                 match = re.match(regex, self.input_code[self.current_position:])

#                 if match:
#                     value = match.group(0)
#                     token = Token(token_type, value, self.current_position)
#                     self.tokens.append(token)
#                     self.current_position += len(value)
#                     break

#             if not match:
#                 raise Exception(f"Invalid character at position {self.current_position}")

#         return self.tokens

# PATTERNS = [
#     (r"\bqreg\b", "QREG"),
#     (r"\bcreg\b", "CREG"),
#     (r"\bmeasure\b", "MEASURE"),
#     (r"\bif\b", "IF"),
#     (r"\belse\b", "ELSE"),
#     (r"\bpi\b", "PI"),
#     (r"\bU\b", "U"),
#     (r"\bCX\b", "CX"),
#     (r"\bX\b", "X"),
#     (r"\bY\b", "Y"),
#     (r"\bZ\b", "Z"),
#     (r"\bH\b", "H"),
#     (r"\breset\b", "RESET"),
#     (r"\bbarrier\b", "BARRIER"),
#     (r"\binclude\b", "INCLUDE"),
#     (r"\bOPENQASM\b", "OPENQASM"),
#     (r"\binclude\b", "INCLUDE"),
#     (r"\bint\b", "INT"),
#     (r"\bfloat\b", "FLOAT"),
#     (r"\bexp\b", "EXP"),
#     (r"\blog\b", "LOG"),
#     (r"\bsin\b", "SIN"),
#     (r"\bcos\b", "COS"),
#     (r"\btan\b", "TAN"),
#     (r"\basin\b", "ASIN"),
#     (r"\bacos\b", "ACOS"),
#     (r"\batan\b", "ATAN"),
#     (r"\bsqrt\b", "SQRT"),
#     (r"\bmin\b", "MIN"),
#     (r"\bmax\b", "MAX"),
#     (r"\babs\b", "ABS"),
#     (r"\bexp2\b", "EXP2"),
#     (r"\blog2\b", "LOG2"),
#     (r"\binteger\b", "INTEGER"),
#     (r"\bboolean\b", "BOOLEAN"),
#     (r"\bbit\b", "BIT"),
#     (r"\bstring\b", "STRING"),
#     (r"\binclude\b", "INCLUDE"),
#     (r"\bqubit\b", "QUBIT"),
#     (r"\bqubits\b", "QUBITS"),
#     (r"\bopaque\b", "OPAQUE"),
#     (r"\bgate\b", "GATE"),
#     (r"\bmeasure\b", "MEASURE"),
#     (r"\bbarrier\b", "BARRIER"),
#     (r"\bcreg\b", "CREG"),
#     (r"\bqreg\b", "QREG"),
#     (r"\bOPENQASM\b", "OPENQASM"),
#     (r"\binclude\b", "INCLUDE"),
#     (r"\breal\b", "REAL"),
#     (r"\bif\b", "IF"),
#     (r"\belse\b", "ELSE"),
#     (r"\bwhile\b", "WHILE"),
#     (r"\bfor\b", "FOR"),
#     (r"\bin\b", "IN"),
#     (r"\bto\b", "TO"),
#     (r"\bstep\b", "STEP"),
#     (r"\breturn\b", "RETURN"),
#     (r"\bprint\b", "PRINT"),
#     (r"\bnot\b", "NOT"),
#     (r"\band\b", "AND"),
#     (r"\bor\b", "OR"),
#     (r"\bxor\b", "XOR"),
#     (r"\btrue\b", "TRUE"),
#     (r"\bfalse\b", "FALSE"),
#     (r"\bnull\b", "NULL"),
#     (r"\bvar\b", "VAR"),
#     (r"\bconst\b", "CONST"),
#     (r"\bdef\b", "DEF"),
#     (r"\bclass\b", "CLASS"),
#     (r"\bimport\b", "IMPORT"),
#     (r"\bas\b", "AS"),
#     (r"\bfrom\b", "FROM"),
#     (r"\bglobal\b", "GLOBAL"),
#     (r"\bnonlocal\b", "NONLOCAL"),
#     (r"\btry\b", "TRY"),
#     (r"\bexcept\b", "EXCEPT"),
#     (r"\bfinally\b", "FINALLY"),
#     (r"\braise\b", "RAISE"),
#     (r"\bassert\b", "ASSERT"),
#     (r"\bwith\b", "WITH"),
#     (r"\bas\b", "AS"),
#     (r"\byield\b", "YIELD"),
#     (r"\blambda\b", "LAMBDA"),
#     (r"\bNone\b", "NONE"),
#     (r"\bself\b", "SELF"),
#     (r"\bcls\b", "CLS"),
#     (r"\b\d+\b", "NUMBER"),
#     (r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", "IDENTIFIER"),
#     (r"\+", "PLUS"),
#     (r"-", "MINUS"),
#     (r"\*", "MULTIPLY"),
#     (r"/", "DIVIDE"),
#     (r"\(", "LPAREN"),
#     (r"\)", "RPAREN"),
#     (r"\{", "LBRACE"),
#     (r"\}", "RBRACE"),
#     (r"\[", "LBRACKET"),
#     (r"\]", "RBRACKET"),
#     (r",", "COMMA"),
#     (r";", "SEMICOLON"),
#     (r":", "COLON"),
#     (r"=", "EQUALS"),
#     (r"==", "EQUALS_EQUALS"),
#     (r"!=", "NOT_EQUALS"),
#     (r"<", "LESS_THAN"),
#     (r">", "GREATER_THAN"),
#     (r"<=", "LESS_THAN_EQUALS"),
#     (r">=", "GREATER_THAN_EQUALS"),
#     (r"\.", "DOT"),
#     (r"\"", "DOUBLE_QUOTE"),
#     (r"\'", "SINGLE_QUOTE"),
#     (r"\\", "BACKSLASH"),
#     (r"\|", "PIPE"),
#     (r"&", "AMPERSAND"),
#     (r"\^", "CARET"),
#     (r"%", "MODULO"),
#     (r"~", "TILDE"),
#     (r"@", "AT"),
#     (r"!", "EXCLAMATION_MARK"),
#     (r"\?", "QUESTION_MARK"),
#     (r"\n", "NEWLINE"),
#     (r"\s+", None)
# ]
