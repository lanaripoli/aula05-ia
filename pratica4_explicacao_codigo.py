# Prática 4 — IA Explicando Código
# A IA vai explicar o código refatorado da Prática 2, linha por linha

# ============================================================
# CÓDIGO DA PRÁTICA 2 (refatorado) — para explicação
# ============================================================

def calculate_average(numbers: list[float]) -> float:
    total = sum(numbers)
    return total / len(numbers)

def find_maximum(numbers: list[float]) -> float:
    return max(numbers)

def analyze_numbers(numbers: list[float]) -> dict:
    return {
        "average": calculate_average(numbers),
        "maximum": find_maximum(numbers),
    }

sample_numbers = [4, 8, 15, 16, 23, 42]
result = analyze_numbers(sample_numbers)
print(f"Média:   {result['average']:.2f}")
print(f"Máximo:  {result['maximum']}")


# ============================================================
# 💬 EXPLICAÇÃO LINHA POR LINHA (gerada pela IA)
# ============================================================

"""
LINHA 1: def calculate_average(numbers: list[float]) -> float:
  → Define uma função chamada calculate_average.
  → Ela recebe um parâmetro chamado numbers, que deve ser uma lista de números
    decimais (list[float]).
  → O "-> float" indica que a função vai retornar um número decimal.
  → Isso se chama "type hint" (dica de tipo) e deixa o código mais legível.

LINHA 2: total = sum(numbers)
  → Cria a variável total e guarda nela a soma de todos os valores da lista.
  → sum() é uma função nativa do Python que soma todos os itens de uma lista.
  → Exemplo: sum([4, 8, 15]) retorna 27.

LINHA 3: return total / len(numbers)
  → Retorna o resultado de total dividido pela quantidade de itens da lista.
  → len(numbers) retorna quantos itens há na lista.
  → Dividindo a soma pelo total de itens, obtemos a média aritmética.

-------------------------------------------------------------

LINHA 5: def find_maximum(numbers: list[float]) -> float:
  → Define a função find_maximum (encontrar máximo).
  → Também recebe uma lista de floats e retorna um float.

LINHA 6: return max(numbers)
  → Usa a função nativa max() do Python para encontrar e retornar o maior valor
    da lista diretamente.
  → Exemplo: max([4, 8, 42]) retorna 42.

-------------------------------------------------------------

LINHA 8: def analyze_numbers(numbers: list[float]) -> dict:
  → Define a função principal analyze_numbers (analisar números).
  → Recebe uma lista de floats e retorna um dicionário (dict).

LINHAS 9-12: return {"average": ..., "maximum": ...}
  → Retorna um dicionário com duas chaves:
      "average" → resultado da função calculate_average
      "maximum" → resultado da função find_maximum
  → Usar dicionário é mais claro do que retornar uma tupla sem nome,
    porque cada valor fica identificado pela chave.

-------------------------------------------------------------

LINHA 14: sample_numbers = [4, 8, 15, 16, 23, 42]
  → Cria uma lista chamada sample_numbers com seis números inteiros.
  → Esses são os dados que vamos analisar.

LINHA 15: result = analyze_numbers(sample_numbers)
  → Chama a função analyze_numbers passando nossa lista.
  → O resultado (um dicionário com 'average' e 'maximum') é guardado em result.

LINHA 16: print(f"Média:   {result['average']:.2f}")
  → Imprime a média formatada com 2 casas decimais.
  → f"..." é uma f-string (string formatada) do Python.
  → :.2f significa "formate como decimal com 2 casas".
  → Exemplo de saída: Média:   18.00

LINHA 17: print(f"Máximo:  {result['maximum']}")
  → Imprime o valor máximo encontrado na lista.
  → Exemplo de saída: Máximo:  42
"""

# ============================================================
# 🧠 O que aprendemos com essa prática?
# ============================================================

"""
A IA foi capaz de:
  ✅ Identificar o propósito de cada função
  ✅ Explicar o uso de funções nativas do Python (sum, max, len)
  ✅ Detalhar o que são type hints e f-strings
  ✅ Justificar as escolhas de design (dicionário vs tupla)
  ✅ Mostrar exemplos práticos de saída

Isso mostra que um código BEM ESCRITO (com boas práticas)
é mais fácil até para a própria IA entender e explicar! 🚀
"""
