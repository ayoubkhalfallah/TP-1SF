from ply import lex, yacc

def p_uml_diagram(p):
    "uml_diagram : STARTUML elements ENDUML"
    p[0] = ("UML", p[2])

def p_elem(p):
    "elements : elements element"
    p[0] = p[1] + [p[2]]

def p_elem_single(p):
    "elements : element"
    p[0] = [p[1]]

def p_elem_actor(p):
    "element : ACTOR ID COLON ACTOR_TXT COLON"
    p[0] = ("Actor", p[2], p[4])

def p_elem_usecase(p):
    "element : USECASE ID COLON USE_CASE_TXT COLON"
    p[0] = ("UseCase", p[2], p[4])

def p_elem_package(p):
    "element : PACKAGE ID LBRACE elements RBRACE"
    p[0] = ("Package", p[2], p[4])

def p_elem_inheritance(p):
    "element : ID INHERIT ID"
    p[0] = ("Inheritance", p[1], p[3])

def p_elem_relation_includes(p):
    "element : ID INCLUDES ID"
    p[0] = ("Includes", p[1], p[3])

def p_eleme_relation_extends(p):
    "element : ID EXTENDS ID"
    p[0] = ("Extends", p[1], p[3])

def p_error(p):
    raise SyntaxError(f"error at {p.value if p else 'EOF'}")

parser = yacc.yacc()



