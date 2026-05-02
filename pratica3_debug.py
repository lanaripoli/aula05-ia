# Prática 3 — Debug com IA
# Código com erros propositais para identificação e correção

# ============================================================
# ❌ CÓDIGO COM ERROS (fornecido para a IA debugar)
# ============================================================

# ERRO 1 — Erro de sintaxe: faltando ":" no final do if
# ERRO 2 — Erro de lógica: usando "=" (atribuição) em vez de "==" (comparação)
# ERRO 3 — Erro de nome: variável 'resultado' usada antes de ser definida no else
# ERRO 4 — Erro de indentação: o return está fora da função

def verificar_aprovacao(nota)
    if nota = 7:
        print("Aprovado com nota exata!")
    elif nota > 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    return resultado  # ← ERRO: só existe se entrar no elif/else, não no if

aluno = "Maria"
nota_aluno = 8.5
verificar_aprovacao(nota_aluno)
print(f"{aluno} ficou: {resultado}")  # ← ERRO: resultado fora do escopo


# ============================================================
# 🔍 ANÁLISE DOS ERROS (feita com apoio da IA)
# ============================================================

"""
ERRO 1 — Sintaxe (SyntaxError)
  Linha:   def verificar_aprovacao(nota)
  Causa:   Falta o ":" obrigatório no final da definição de função.
  Correção: def verificar_aprovacao(nota):

ERRO 2 — Lógica (não gera exceção, mas funciona errado)
  Linha:   if nota = 7:
  Causa:   "=" é atribuição, não comparação. Em Python isso gera SyntaxError.
  Correção: if nota == 7:

ERRO 3 — NameError / UnboundLocalError
  Linha:   return resultado
  Causa:   Se nota == 7, o código entra no primeiro if e `resultado` nunca é
           definido, então o return vai lançar erro.
  Correção: Definir resultado = "Aprovado com nota exata!" dentro do if.

ERRO 4 — Escopo / NameError
  Linha:   print(f"{aluno} ficou: {resultado}")
  Causa:   `resultado` é uma variável local da função; fora dela, não existe.
  Correção: Capturar o retorno da função em uma variável.
"""


# ============================================================
# ✅ CÓDIGO CORRIGIDO
# ============================================================

def verificar_aprovacao(nota: float) -> str:
    """
    Verifica se um aluno foi aprovado com base na nota.

    Args:
        nota (float): A nota do aluno (de 0 a 10).

    Returns:
        str: Mensagem indicando o resultado ('Aprovado' ou 'Reprovado').
    """
    if nota == 7:
        resultado = "Aprovado com nota exata!"
    elif nota > 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    return resultado


# ===== Uso correto =====
aluno = "Maria"
nota_aluno = 8.5

status = verificar_aprovacao(nota_aluno)
print(f"{aluno} ficou: {status}")

# Testando outros casos
notas_teste = [5.0, 7.0, 9.5, 3.0]
nomes_teste = ["João", "Ana", "Pedro", "Luiza"]

print("\n--- Resultados da turma ---")
for nome, nota in zip(nomes_teste, notas_teste):
    print(f"{nome}: {verificar_aprovacao(nota)}")
