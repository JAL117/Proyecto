TABLA_LL1 = {
    "Program": {
        "start": ["start", "Declarations", "Block", "end"]
    },
    "Declarations": {
        "declare": ["Declaration", "Declarations"],
        "int": ["Declaration", "Declarations"],
        "string": ["Declaration", "Declarations"],
        "show": [],
        "get": [],
        "if": [],
        "for": [],
        "identifier": [],
        "end": [],
        "$": []
    },
    "Declaration": {
        "declare": ["declare", "identifier", "=", "number", ";"],
        "int": ["int", "identifier", "=", "number", ";"],
        "string": ["string", "identifier", "=", "string_literal", ";"]
    },
    "Block": {
        "show": ["Statement", "Block"],
        "get": ["Statement", "Block"],
        "if": ["Statement", "Block"],
        "for": ["Statement", "Block"],
        "identifier": ["Statement", "Block"],
        "declare": ["Statement", "Block"],
        "int": ["Statement", "Block"],
        "string": ["Statement", "Block"],  
        "end": [],
        "else": [],
        "stop": [],
        "$": []
    },
   "NonEmptyBlock": {
       "show": ["Statement", "Block"],
       "get": ["Statement", "Block"],
       "if": ["Statement", "Block"],
       "for": ["Statement", "Block"],
       "identifier": ["Statement", "Block"],
       "declare": ["Statement", "Block"],
       "int": ["Statement", "Block"],
       "string": ["Statement", "Block"]
    },
    "Statement": {
        "show": ["show", "(", "Arguments", ")", ";"],
        "get": ["get", "(", "Arguments", ")", ";"],
        "if": ["Conditional"],
        "for": ["Loop"],
        "identifier": ["Assignment", ";"],
        "declare": ["Assignment", ";"],
        "int": ["Assignment", ";"],
        "string": ["Assignment", ";"]
    },
    "Arguments": {
        "string_literal": ["Argument", "ArgumentsPrime"],
        "identifier": ["Argument", "ArgumentsPrime"],
        "number": ["Argument", "ArgumentsPrime"],
        "float_number": ["Argument", "ArgumentsPrime"],
        "(": ["Argument", "ArgumentsPrime"]
    },
    "ArgumentsPrime": {
        "comma": ["comma", "Argument", "ArgumentsPrime"],
        ")": []
    },
    "Argument": {
        "string_literal": ["string_literal"],
        "identifier": ["ArithmeticExpression"],
        "number": ["ArithmeticExpression"],
        "float_number": ["ArithmeticExpression"],
        "(": ["ArithmeticExpression"]
    },
    "Conditional": {
    "if": ["if", "(", "Condition", ")", ":", "NonEmptyBlock", "OptionalElse"]
    },
    "OptionalElse": {
    "else": ["else", ":", "Block"],
    "show": [],
    "get": [],
    "if": [],
    "for": [],
    "identifier": [],
    "declare": [],
    "int": [],
    "string": [],
    "end": [],
    "stop": [],
    "$": []
    },
    "Condition": {
        "identifier": ["identifier", "ComparisonOperator", "ConditionValue"]
    },
    "ConditionValue": {
        "string_literal": ["string_literal"],
        "number": ["number"],
        "identifier": ["identifier", "ConditionPrime"]
    },
    "ConditionPrime": {
        "or": ["or", "Condition"],
        ")": []
    },
    "Loop": {
        "for": ["for", "(", "Assignment", ";", "Condition", ";", "Increment", ")", ":", "Block", "stop"]
    },
    "Assignment": {
        "identifier": ["identifier", "=", "ArithmeticExpression"],
        "declare": ["declare", "identifier", "=", "ArithmeticExpression"],
        "int": ["int", "identifier", "=", "ArithmeticExpression"],
        "string": ["string", "identifier", "=", "ArithmeticExpression"]
    },
    "Increment": {
        "increment": ["increment", "(", "number", ")"]
    },
    "ArithmeticExpression": {
        "identifier": ["Term", "ArithmeticExpressionPrime"],
        "number": ["Term", "ArithmeticExpressionPrime"],
        "float_number": ["Term", "ArithmeticExpressionPrime"],
        "(": ["Term", "ArithmeticExpressionPrime"]
    },
    "ArithmeticExpressionPrime": {
        "plus": ["plus", "Term", "ArithmeticExpressionPrime"],
        "minus": ["minus", "Term", "ArithmeticExpressionPrime"],
        ")": [],
        ";": [],
        "comma": []
    },
    "Term": {
        "identifier": ["Factor", "TermPrime"],
        "number": ["Factor", "TermPrime"],
        "float_number": ["Factor", "TermPrime"],
        "(": ["Factor", "TermPrime"]
    },
    "TermPrime": {
        "multiply": ["multiply", "Factor", "TermPrime"],
        "divide": ["divide", "Factor", "TermPrime"],
        "plus": [],
        "minus": [],
        ")": [],
        ";": [],
        "comma": []
    },
    "Factor": {
        "(": ["(", "ArithmeticExpression", ")"],
        "identifier": ["identifier"],
        "number": ["number"],
        "float_number": ["float_number"]
    },
    "ComparisonOperator":{
        "equal": ["equal"],
        "not_equal": ["not_equal"],
        "less_than": ["less_than"],
        "less_or_equal": ["less_or_equal"],
        "greater_than": ["greater_than"],
        "greater_or_equal": ["greater_or_equal"]
    }
}

TOKENS_SINCRONIZACION = {
    "Program": ["start", "end", "$"],
    "Declarations": ["show", "get", "if", "for", "end", "$"],
    "Declaration": [";", "show", "get", "if", "for", "end", "$"],
    "Block": ["end", "else", "stop", "$"],
    "NonEmptyBlock": ["else", "stop", "end", "$"],
    "Statement": [";", "show", "get", "if", "for", "identifier", "end", "else", "stop", "$"],
    "Arguments": [")", ";", "$"],
    "ArgumentsPrime": [")", ";", "$"],
    "Argument": ["comma", ")", ";", "$"],
    "Conditional": [":", "else", "end", "show", "get", "if", "for", "identifier", "$"],
    "OptionalElse": ["show", "get", "if", "for", "identifier", "end", "$"],
    "Condition": [")", ";", ":", "$"],
    "ConditionValue": [")", ";", ":", "$"],
    "ConditionPrime": [")", ";", ":", "$"],
    "Loop": [":", "stop", "end", "show", "get", "if", "for", "identifier", "$"],
    "Assignment": [";", "end", "else", "stop", "$"],
    "Increment": [")", ";", "$"],
    "ArithmeticExpression": [")", ";", "comma", "$"],
    "ArithmeticExpressionPrime": [")", ";", "comma", "$"],
    "Term": ["plus", "minus", ")", ";", "comma", "$"],
    "TermPrime": ["plus", "minus", ")", ";", "comma", "$"],
    "Factor": ["multiply", "divide", "plus", "minus", ")", ";", "comma", "$"],
    "ComparisonOperator": [")", ";", ":", "$"]
}

NOMBRES_LEGIBLES = {
    "Program": "bloque de programa",
    "Declarations": "declaración de variables",
    "Declaration": "declaración de variable",
    "Block": "bloque de código",
    "NonEmptyBlock": "bloque de código no vacío",
    "Statement": "sentencia",
    "Arguments": "argumentos de función",
    "ArgumentsPrime": "argumentos adicionales",
    "Argument": "argumento",
    "Conditional": "estructura condicional",
    "OptionalElse": "bloque 'else' opcional",
    "Condition": "condición",
    "ConditionValue": "valor de condición",
    "ConditionPrime": "condición adicional (OR)",
    "Loop": "bucle para",
    "Assignment": "asignación de variable",
    "Increment": "incremento",
    "ArithmeticExpression": "expresión aritmética",
    "ArithmeticExpressionPrime": "expresión aritmética (sumas/restas)",
    "Term": "término",
    "TermPrime": "término (multiplicaciones/divisiones)",
    "Factor": "factor",
    "ComparisonOperator": "operador de comparacion"
}

TOKENS_SUGERIDOS = {
    ";": "Falta un punto y coma (;) al final de la sentencia",
    ")": "Falta un paréntesis de cierre",
    "(": "Falta un paréntesis de apertura",
    ":": "Falta el símbolo de dos puntos (:) después de la condición",
    "=": "Falta el operador de asignación (=)",
    "stop": "Falta la palabra clave 'stop' para cerrar el bucle",
    "equal": "Se esperaba un operador de igualdad (equal)",
    "not_equal": "Se esperaba un operador diferente (not_equal)",
    "less_than": "Se esperaba un operador de menor que (less_than)",
    "less_or_equal": "Se esperaba un operador de menor o igual que (less_or_equal)",
    "greater_than": "Se esperaba un operador de mayor que (greater_than)",
    "greater_or_equal": "Se esperaba un operador de mayor o igual que (greater_or_equal)"
}

CASOS_CORRECTOS = [
    """
    start
    int x = 10;
    show("El valor de x es: ", x);
    end
    """,
    """
    start
    int i = 0;
    for (i = 0; i less_than 3; increment(1)):
        show(i);
    stop
    end
    """,
    """
    start
    string oper = "";
    int num = 0;
    show("Ingrese un número");
    get(num);
    int doble = num multiply 2;
    show("El doble es: ", doble);
    end
    """,
]

CASOS_INCORRECTOS = [
    """
    start
    int x = 10
    show(x)
    end
    """,
    """
    start
    int a = 5;
    if (a plus 5):
        show(a);
    end
    """,
    """
    start
    int i = 0;
    for (i = 0; i less_than 3; increment(1)):
        show(i);
    end
    """,
    """
    start
    int x = "texto";
    show(x);
    end
    """,
    """
    start
    int a = 5;
    if (a equal 5)
    show(a);
    end
    """
]

def lexer(entrada):
    tokens = []
    entrada = entrada.replace("\n", " ").replace("\t", " ")
    i = 0
    linea = 1
    columna = 1
    posiciones = []  
    
    while i < len(entrada):
        char = entrada[i]
        
        if char == '\n':
            linea += 1
            columna = 1
        
        if char.isspace():
            if char == '\n':
                linea += 1
                columna = 1
            else:
                columna += 1
            i += 1
            continue
        
        token_pos = (linea, columna)
        
        if entrada[i:i+5].lower() == "start":
            tokens.append("start")
            posiciones.append(token_pos)
            i += 5
            columna += 5
        elif entrada[i:i+3].lower() == "end":
            tokens.append("end")
            posiciones.append(token_pos)
            i += 3
            columna += 3
        elif entrada[i:i+7].lower() == "declare":
            tokens.append("declare")
            posiciones.append(token_pos)
            i += 7
            columna += 7
        elif entrada[i:i+3].lower() == "int":
            tokens.append("int")
            posiciones.append(token_pos)
            i += 3
            columna += 3
        elif entrada[i:i+6].lower() == "string":
            tokens.append("string")
            posiciones.append(token_pos)
            i += 6
            columna += 6
        elif entrada[i:i+4].lower() == "show":
            tokens.append("show")
            posiciones.append(token_pos)
            i += 4
            columna += 4
        elif entrada[i:i+3].lower() == "get":
            tokens.append("get")
            posiciones.append(token_pos)
            i += 3
            columna += 3
        elif entrada[i:i+2].lower() == "if":
            tokens.append("if")
            posiciones.append(token_pos)
            i += 2
            columna += 2
        elif entrada[i:i+4].lower() == "else":
            tokens.append("else")
            posiciones.append(token_pos)
            i += 4
            columna += 4
        elif entrada[i:i+3].lower() == "for":
            tokens.append("for")
            posiciones.append(token_pos)
            i += 3
            columna += 3
        elif entrada[i:i+9].lower() == "increment":
            tokens.append("increment")
            posiciones.append(token_pos)
            i += 9
            columna += 9
        elif entrada[i:i+4].lower() == "stop":
            tokens.append("stop")
            posiciones.append(token_pos)
            i += 4
            columna += 4
        elif entrada[i:i+5].lower() == "plus":
            tokens.append("plus")
            posiciones.append(token_pos)
            i += 4
            columna += 4
        elif entrada[i:i+5].lower() == "minus":
            tokens.append("minus")
            posiciones.append(token_pos)
            i += 5
            columna += 5
        elif entrada[i:i+8].lower() == "multiply":
            tokens.append("multiply")
            posiciones.append(token_pos)
            i += 8
            columna += 8
        elif entrada[i:i+6].lower() == "divide":
            tokens.append("divide")
            tokens.append("divide")
            posiciones.append(token_pos)
            i += 6
            columna += 6
        elif entrada[i:i+5].lower() == "equal":
            tokens.append("equal")
            posiciones.append(token_pos)
            i += 5
            columna += 5
        elif entrada[i:i+9].lower() == "not_equal":
            tokens.append("not_equal")
            posiciones.append(token_pos)
            i += 9
            columna += 9
        elif entrada[i:i+9].lower() == "less_than":
            tokens.append("less_than")
            posiciones.append(token_pos)
            i += 9
            columna += 9
        elif entrada[i:i+12].lower() == "less_or_equal":
            tokens.append("less_or_equal")
            posiciones.append(token_pos)
            i += 12
            columna += 12
        elif entrada[i:i+11].lower() == "greater_than":
            tokens.append("greater_than")
            posiciones.append(token_pos)
            i += 11
            columna += 11
        elif entrada[i:i+14].lower() == "greater_or_equal":
            tokens.append("greater_or_equal")
            posiciones.append(token_pos)
            i += 14
            columna += 14
        elif entrada[i:i+2].lower() == "or":
            tokens.append("or")
            posiciones.append(token_pos)
            i += 2
            columna += 2
        elif char == ";":
            tokens.append(";")
            posiciones.append(token_pos)
            i += 1
            columna += 1
        elif char == "(":
            tokens.append("(")
            posiciones.append(token_pos)
            i += 1
            columna += 1
        elif char == ")":
            tokens.append(")")
            posiciones.append(token_pos)
            i += 1
            columna += 1
        elif char == ":":
            tokens.append(":")
            posiciones.append(token_pos)
            i += 1
            columna += 1
        elif char == "=":
            tokens.append("=")
            posiciones.append(token_pos)
            i += 1
            columna += 1
        elif char == ",": 
            tokens.append("comma")
            posiciones.append(token_pos)
            i += 1
            columna += 1
        elif char == '"':
            j = i + 1
            while j < len(entrada) and entrada[j] != '"':
                j += 1
            if j < len(entrada):
                tokens.append("string_literal")
                posiciones.append(token_pos)
                columna += (j - i + 1)
                i = j + 1
            else:
                tokens.append("ERROR")
                posiciones.append(token_pos)
                break
        elif char.isdigit():
            j = i
            while j < len(entrada) and (entrada[j].isdigit() or entrada[j] == "."):
                j += 1
            token = entrada[i:j]
            if token.count(".") == 1 and token.replace(".", "").isdigit():
                tokens.append("float_number")
            else:
                tokens.append("number")
            posiciones.append(token_pos)
            columna += (j - i)
            i = j
        else:
            j = i
            while j < len(entrada) and (entrada[j].isalnum() or entrada[j] == "_"):
                j += 1
            if j > i:  
                tokens.append("identifier")
                posiciones.append(token_pos)
                columna += (j - i)
                i = j
            else:
                tokens.append(f"ERROR_TOKEN_{char}")
                posiciones.append(token_pos)
                i += 1
                columna += 1
    
    tokens.append("$")
    posiciones.append((linea, columna))
    return tokens, posiciones

def analizar_entrada(entrada):
    tokens, posiciones = lexer(entrada)
    print(f"Tokens generados: {tokens}")
    
    errores = []
    
    pila = ["$", "Program"]
    indice = 0
    max_iteraciones = 1000  
    
    iteraciones = 0
    recuperando = False
    contexto_actual = "Program" 
    
    def sincronizar():
        nonlocal indice, recuperando, contexto_actual
        
        tokens_sincronizacion = TOKENS_SINCRONIZACION.get(contexto_actual, [";", "end", "$"])
        
        while indice < len(tokens) and tokens[indice] not in tokens_sincronizacion:
            indice += 1
            
        recuperando = False
        if indice < len(tokens):
            print(f"Sincronizado en token: {tokens[indice]} (índice {indice})")
        
    while pila and indice < len(tokens):
        if iteraciones > max_iteraciones:
            errores.append(f"Error: Análisis detenido después de {iteraciones} iteraciones (posible bucle infinito)")
            break
        
        iteraciones += 1
        
        if recuperando:
            sincronizar()
            if indice >= len(tokens):
                break
        
        top = pila.pop()
        print(f"Iteración {iteraciones}: Pila={pila + [top]}, Top={top}, Token actual={tokens[indice]} (índice={indice})")
        
        if top in TABLA_LL1:
            contexto_actual = top
        
        if top in TABLA_LL1:
            if tokens[indice] in TABLA_LL1[top]:
                produccion = TABLA_LL1[top][tokens[indice]]
                if produccion:
                    pila.extend(reversed(produccion))
                    print(f"Expansión: {top} -> {produccion} con token {tokens[indice]}")
                else:
                    print(f"Producción vacía para {top} con token {tokens[indice]}")
            else:
                linea, columna = posiciones[indice]
                expected = list(TABLA_LL1[top].keys())
                
                msg_error = f"Error sintáctico en línea {linea}, columna {columna}: Token inesperado '{tokens[indice]}'"
                
                if expected:
                    nombre_amigable = NOMBRES_LEGIBLES.get(top, top)
                    msg_error += f". Se esperaba un {nombre_amigable} que comienza con: {', '.join(expected)}"
                
                if tokens[indice] in TOKENS_SUGERIDOS:
                    msg_error += f". Sugerencia: {TOKENS_SUGERIDOS[tokens[indice]]}"
                
                errores.append(msg_error)
                print(msg_error)
                
                recuperando = True
                
                if top in TOKENS_SUGERIDOS:
                    pila.append(top) 
                    errores[-1] += f" - Insertando '{top}' implícito y continuando"
        
        else:
            if top == tokens[indice]:
                indice += 1
                print(f"Coincidencia: {top} == {tokens[indice-1]}")
            else:
                linea, columna = posiciones[indice]
                
                msg_error = f"Error sintáctico en línea {linea}, columna {columna}: Se esperaba '{top}' pero se encontró '{tokens[indice]}'"
                errores.append(msg_error)
                print(msg_error)
                
                recuperando = True
    
    if pila and pila != ["$"] and indice < len(tokens) - 1:
        errores.append("Error sintáctico: Código incompleto o estructura no cerrada correctamente")
    
    if errores:
        return f"Código con {len(errores)} errores:\n" + "\n".join(errores)
    else:
        return "Código válido!"