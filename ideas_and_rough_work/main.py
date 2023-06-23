from lexer import Lexer
from parser import Parser
from semantic_analyzer import SemanticAnalyzer
from qua_code_generator import QuaCodeGenerator

def main():
    # Read the input QASM code from a file or user input
    input_code = "..."
    
    # Create a lexer instance and tokenize the input code
    lexer = Lexer()
    tokens = lexer.tokenize(input_code)
    
    # Create a parser instance and parse the tokens
    parser = Parser()
    parse_tree = parser.parse(tokens)
    
    # Create a symbol table instance and build the symbol table
    symbol_table = SymbolTable()
    symbol_table.build(parse_tree)
    
    # Create a semantic analyzer instance and perform semantic analysis
    semantic_analyzer = SemanticAnalyzer(symbol_table)
    semantic_analyzer.analyze(parse_tree)
    
    # Create a Qua code generator instance and generate the Qua code
    qua_code_generator = QuaCodeGenerator(symbol_table)
    qua_code = qua_code_generator.generate(parse_tree)
    
    # Write the generated Qua code to a file 
    print(qua_code)

if __name__ == "__main__":
    main()
