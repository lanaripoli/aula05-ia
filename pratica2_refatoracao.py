# Prática 2 — Refatoração com IA
# Comparação: código original (mal estruturado) x código refatorado

# ============================================================
# ❌ CÓDIGO ORIGINAL — mal estruturado (fornecido para a IA)
# ============================================================

def f(l):
    s = 0
    m = 0
    for i in range(len(l)):
        s = s + l[i]
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
    r1 = s / len(l)
    r2 = m
    return r1, r2

n = [4, 8, 15, 16, 23, 42]
x, y = f(n)
print(x)
print(y)


# ============================================================
# ✅ CÓDIGO REFATORADO — boas práticas aplicadas pela IA
# ============================================================

def calculate_average(numbers: list[float]) -> float:
    """
    Calcula a média aritmética de uma lista de números.

    Args:
        numbers (list[float]): Lista com os valores numéricos.

    Returns:
        float: A média dos valores da lista.
    """
    total = sum(numbers)
    return total / len(numbers)


def find_maximum(numbers: list[float]) -> float:
    """
    Encontra o maior valor em uma lista de números.

    Args:
        numbers (list[float]): Lista com os valores numéricos.

    Returns:
        float: O maior valor encontrado na lista.
    """
    return max(numbers)


def analyze_numbers(numbers: list[float]) -> dict:
    """
    Analisa uma lista de números e retorna média e valor máximo.

    Args:
        numbers (list[float]): Lista com os valores a serem analisados.

    Returns:
        dict: Dicionário contendo 'average' e 'maximum'.
    """
    return {
        "average": calculate_average(numbers),
        "maximum": find_maximum(numbers),
    }


# ===== Uso =====
sample_numbers = [4, 8, 15, 16, 23, 42]
result = analyze_numbers(sample_numbers)

print(f"Média:   {result['average']:.2f}")
print(f"Máximo:  {result['maximum']}")


# ============================================================
# 📝 MELHORIAS IDENTIFICADAS (análise comparativa)
# ============================================================

"""
PROBLEMA 1 — Nome de função sem significado
  Antes:  def f(l)
  Depois: def calculate_average / def find_maximum / def analyze_numbers
  Por quê: Nomes descritivos deixam o código autoexplicativo.

PROBLEMA 2 — Variáveis genéricas
  Antes:  s, m, r1, r2, l, i, n, x, y
  Depois: total, maximum, average, numbers, result
  Por quê: Variáveis com nomes reais facilitam a leitura e manutenção.

PROBLEMA 3 — Loop desnecessário com range(len())
  Antes:  for i in range(len(l)): s = s + l[i]
  Depois: total = sum(numbers)
  Por quê: Python já tem funções nativas (sum, max) para isso. Mais limpo e eficiente.

PROBLEMA 4 — Retorno de múltiplos valores sem estrutura
  Antes:  return r1, r2  (tupla sem contexto)
  Depois: return {"average": ..., "maximum": ...}  (dicionário com chaves claras)
  Por quê: O dicionário deixa explícito o que cada valor representa.

PROBLEMA 5 — Ausência de documentação
  Antes:  zero comentários ou docstrings
  Depois: docstrings em cada função com Args e Returns
  Por quê: Documentação é essencial para manutenção e trabalho em equipe.

PROBLEMA 6 — Função com responsabilidade dupla
  Antes:  a função f() calculava média E máximo ao mesmo tempo
  Depois: funções separadas para cada responsabilidade (princípio da responsabilidade única)
  Por quê: Cada função deve fazer apenas uma coisa.
"""
