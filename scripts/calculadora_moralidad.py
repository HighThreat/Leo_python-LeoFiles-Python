"""
â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—
â•‘          ANALIZADOR DE DECISIONES MORALES                â•‘
â•‘   Basado en los principales marcos Ã©ticos filosÃ³ficos    â•‘
â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
"""

# â”€â”€â”€ Marcos Ã©ticos disponibles â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

MARCOS_ETICOS = {
    "utilitarismo": {
        "nombre":      "âš–ï¸  Utilitarismo",
        "filosofo":    "Jeremy Bentham / John Stuart Mill",
        "descripcion": "Busca la mayor felicidad para el mayor nÃºmero de personas.",
        "preguntas": [
            ("Â¿CuÃ¡ntas personas se beneficiarÃ­an de esta acciÃ³n?",
             ["Muchas (>10)",  "Algunas (3-10)", "Pocas (1-2)", "Ninguna"]),
            ("Â¿CuÃ¡ntas personas se verÃ­an perjudicadas?",
             ["Ninguna",       "Pocas (1-2)",    "Algunas (3-10)", "Muchas (>10)"]),
            ("Â¿El beneficio es a largo o corto plazo?",
             ["Largo plazo",   "Ambos",          "Corto plazo",    "Ninguno"]),
        ]
    },
    "deontologia": {
        "nombre":      "ðŸ“œ DeontologÃ­a (Kant)",
        "filosofo":    "Immanuel Kant",
        "descripcion": "Las acciones son morales si respetan el deber y los derechos universales.",
        "preguntas": [
            ("Â¿PodrÃ­as desear que TODOS hicieran lo mismo en tu situaciÃ³n?",
             ["SÃ­, sin duda",  "Probablemente",  "Dudoso",         "No"]),
            ("Â¿Tratas a las personas como fines en sÃ­ mismas (no solo como medios)?",
             ["SÃ­, siempre",   "En su mayorÃ­a",  "Parcialmente",   "No"]),
            ("Â¿Respetas los derechos fundamentales de todos los involucrados?",
             ["Completamente", "En su mayorÃ­a",  "Parcialmente",   "No"]),
        ]
    },
    "virtud": {
        "nombre":      "ðŸŒ¿ Ã‰tica de la Virtud",
        "filosofo":    "AristÃ³teles",
        "descripcion": "Pregunta quÃ© harÃ­a una persona virtuosa y de buen carÃ¡cter.",
        "preguntas": [
            ("Â¿Esta acciÃ³n refleja valentÃ­a, justicia u honestidad?",
             ["Mucho",         "Bastante",       "Algo",           "Nada"]),
            ("Â¿Te sentirÃ­a orgulloso/a de esta decisiÃ³n ante alguien que admiras?",
             ["Totalmente",    "Probablemente",  "No estoy seguro","No"]),
            ("Â¿La acciÃ³n refuerza hÃ¡bitos que te harÃ¡n mejor persona?",
             ["SÃ­, claramente","Posiblemente",   "Neutro",         "Me perjudica"]),
        ]
    },
    "contractualismo": {
        "nombre":      "ðŸ¤ Contractualismo",
        "filosofo":    "John Rawls",
        "descripcion": "Â¿SerÃ­a justa esta acciÃ³n si no supieras quÃ© rol tendrÃ­as en ella?",
        "preguntas": [
            ("Si no supieras si serÃ­as el afectado o el beneficiado, Â¿lo aceptarÃ­as?",
             ["Sin duda",      "Probablemente",  "Con reservas",   "No"]),
            ("Â¿La acciÃ³n serÃ­a aceptable para los miembros mÃ¡s vulnerables?",
             ["SÃ­",            "Mayormente sÃ­",  "Dudoso",         "No"]),
            ("Â¿PodrÃ­as defender esta decisiÃ³n pÃºblicamente ante todos los afectados?",
             ["SÃ­, fÃ¡cilmente","Con dificultad", "Apenas",         "No podrÃ­a"]),
        ]
    },
}

PUNTOS = [3, 2, 1, 0]   # puntos por cada opciÃ³n (Ã­ndice 0 = mejor)


# â”€â”€â”€ Utilidades de consola â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def linea(char="â”€", n=60):
    print(char * n)

def titulo(texto, char="â•"):
    linea(char)
    print(f"  {texto}")
    linea(char)

def pregunta_si_no(texto):
    while True:
        r = input(f"{texto} (s/n): ").strip().lower()
        if r in ("s", "si", "sÃ­", "y", "yes"):
            return True
        if r in ("n", "no"):
            return False
        print("  âš ï¸  Por favor responde 's' o 'n'.")

def elegir_opcion(opciones, etiqueta="OpciÃ³n"):
    for i, op in enumerate(opciones, 1):
        print(f"    {i}. {op}")
    while True:
        try:
            r = int(input(f"  â–¶  Elige {etiqueta} (1-{len(opciones)}): "))
            if 1 <= r <= len(opciones):
                return r - 1          # Ã­ndice 0-based
            print(f"  âš ï¸  Ingresa un nÃºmero entre 1 y {len(opciones)}.")
        except ValueError:
            print("  âš ï¸  Ingresa un nÃºmero vÃ¡lido.")


# â”€â”€â”€ EvaluaciÃ³n por marco â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def evaluar_marco(clave, marco):
    titulo(marco["nombre"])
    print(f"  ðŸ§   FilÃ³sofo(s): {marco['filosofo']}")
    print(f"  ðŸ’¡  Principio  : {marco['descripcion']}")
    linea()
    total = 0
    for texto, opciones in marco["preguntas"]:
        print(f"\n  â“  {texto}")
        idx   = elegir_opcion(opciones)
        total += PUNTOS[idx]
        print(f"       â†’ {opciones[idx]}")
    maximo = len(marco["preguntas"]) * 3
    return total, maximo


def barra(puntos, maximo, largo=20):
    llenos   = round((puntos / maximo) * largo)
    vacios   = largo - llenos
    return "â–ˆ" * llenos + "â–‘" * vacios


def veredicto(porcentaje):
    if porcentaje >= 75:
        return "âœ…  MORALMENTE JUSTIFICADA"
    elif porcentaje >= 50:
        return "âš ï¸   MORALMENTE DUDOSA"
    elif porcentaje >= 25:
        return "ðŸ”¶  MORALMENTE PROBLEMÃTICA"
    else:
        return "âŒ  MORALMENTE INJUSTIFICADA"


# â”€â”€â”€ Flujo principal â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def main():
    print()
    titulo("ANALIZADOR DE DECISIONES MORALES", "â•")
    print("""
  Este programa analiza tu dilema moral desde cuatro grandes
  tradiciones filosÃ³ficas y te ofrece una visiÃ³n integral.

  âš¡  Responde con honestidad para obtener el mejor anÃ¡lisis.
""")

    # 1. DescripciÃ³n del dilema
    linea()
    print("  ðŸ“  Describe brevemente tu dilema moral:")
    dilema = input("  > ").strip()
    if not dilema:
        dilema = "(dilema no especificado)"

    # 2. Elegir marcos a usar
    print("\n  Â¿QuÃ© marcos Ã©ticos deseas aplicar?")
    claves_disponibles = list(MARCOS_ETICOS.keys())
    seleccionados      = []

    for clave in claves_disponibles:
        nombre = MARCOS_ETICOS[clave]["nombre"]
        if pregunta_si_no(f"  Â¿Incluir {nombre}?"):
            seleccionados.append(clave)

    if not seleccionados:
        print("\n  âš ï¸  No seleccionaste ningÃºn marco. Se usarÃ¡n todos por defecto.\n")
        seleccionados = claves_disponibles

    # 3. EvaluaciÃ³n
    resultados = {}
    for clave in seleccionados:
        print()
        puntos, maximo          = evaluar_marco(clave, MARCOS_ETICOS[clave])
        resultados[clave]       = (puntos, maximo)

    # 4. Informe final
    print("\n")
    titulo("ðŸ“Š INFORME FINAL", "â•")
    print(f"  Dilema evaluado: Â«{dilema}Â»\n")

    total_p = total_m = 0
    for clave, (pts, mx) in resultados.items():
        pct  = (pts / mx) * 100
        bar  = barra(pts, mx)
        vrd  = veredicto(pct)
        nombre = MARCOS_ETICOS[clave]["nombre"]
        print(f"  {nombre}")
        print(f"    [{bar}] {pct:5.1f}%  â†’  {vrd}")
        print()
        total_p += pts
        total_m += mx

    # Veredicto global
    pct_global = (total_p / total_m) * 100
    linea("â”€")
    print(f"  VEREDICTO GLOBAL  [{barra(total_p, total_m)}] {pct_global:.1f}%")
    print(f"  {veredicto(pct_global)}")
    linea("â”€")

    # 5. RecomendaciÃ³n cualitativa
    print("""
  ðŸ“Œ  Disclaimer:
  â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  â€¢ NingÃºn anÃ¡lisis automÃ¡tico reemplaza tu juicio personal.
  â€¢ Los marcos Ã©ticos son herramientas, no verdades absolutas.
  â€¢ Consulta a personas de confianza ante decisiones crÃ­ticas.
  â€¢ La reflexiÃ³n constante es el verdadero motor moral.
    """)

    # 6. Â¿Repetir?
    linea()
    if pregunta_si_no("  Â¿Deseas analizar otro dilema?"):
        main()
    else:
        print("\n  âœ¨  Â¡Buena suerte con tu decisiÃ³n!\n")


# â”€â”€â”€ Entrada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Programa interrumpido. Â¡Hasta pronto!\n")
