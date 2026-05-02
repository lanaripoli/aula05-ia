# Explicação: Verificação de Número Primo em Python

## O que é um número primo?

Um número primo é aquele que só pode ser dividido por **1** e por **ele mesmo**, sem deixar resto. Exemplos: 2, 3, 5, 7, 11, 13...

---

## Versão inicial (gerada pela IA)

```python
def is_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

### Explicação linha por linha

| Linha | Código | O que faz |
|-------|--------|-----------|
| 1 | `def is_primo(n):` | Define a função chamada `is_primo` que recebe um número `n` |
| 2 | `if n < 2:` | Verifica se o número é menor que 2 (que não pode ser primo) |
| 3 | `return False` | Retorna False: o número não é primo |
| 4 | `for i in range(2, n):` | Testa todos os divisores de 2 até n-1 |
| 5 | `if n % i == 0:` | Verifica se a divisão tem resto zero (ou seja, é divisível) |
| 6 | `return False` | Se encontrou divisor, não é primo — retorna False |
| 7 | `return True` | Se nenhum divisor foi encontrado, é primo! |

> ⚠️ **Problema desta versão:** ela testa todos os números de 2 até `n-1`, o que é lento para números grandes.

---

## Versão otimizada (Clean Code + boas práticas)

```python
import math

def is_prime(number: int) -> bool:
    """
    Verifica se um número inteiro é primo.
    """
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    upper_limit = int(math.sqrt(number)) + 1
    for divisor in range(3, upper_limit, 2):
        if number % divisor == 0:
            return False

    return True
```

### Explicação linha por linha

| Linha | Código | O que faz |
|-------|--------|-----------|
| 1 | `import math` | Importa a biblioteca matemática para usar a raiz quadrada |
| 3 | `def is_prime(number: int) -> bool:` | Define a função com **type hints** — deixa claro o tipo de entrada e saída |
| 4–6 | `"""..."""` | **Docstring**: documenta o que a função faz (boa prática!) |
| 7 | `if number < 2:` | Números menores que 2 nunca são primos |
| 10 | `if number == 2:` | O número 2 é primo (único par primo), trata separado |
| 13 | `if number % 2 == 0:` | Elimina todos os outros pares de uma vez (rápido!) |
| 16 | `upper_limit = int(math.sqrt(number)) + 1` | **Otimização principal:** só precisa testar até a raiz quadrada |
| 17 | `for divisor in range(3, upper_limit, 2):` | Testa apenas números **ímpares** a partir de 3 (pula os pares) |
| 18 | `if number % divisor == 0:` | Se encontrou divisor, não é primo |
| 21 | `return True` | Passou por todos os testes → é primo! |

---

## Por que a versão otimizada é melhor?

| Critério | Versão inicial | Versão otimizada |
|----------|---------------|-----------------|
| Testando o número 97 | Faz 95 iterações | Faz apenas 4 iterações |
| Nome da função | `is_primo` (mistura português/inglês) | `is_prime` (padrão inglês consistente) |
| Documentação | Nenhuma | Docstring completa |
| Type hints | Não tem | Tem (`int -> bool`) |
| Testa pares desnecessariamente | Sim | Não |

---

## Resumo das melhorias aplicadas

- ✅ **Nome em inglês e consistente** (`is_prime`)
- ✅ **Type hints** para deixar o código mais claro
- ✅ **Docstring** documentando a função
- ✅ **Eliminação antecipada** de casos especiais (< 2, par)
- ✅ **Loop até raiz quadrada** — muito mais eficiente
- ✅ **Pula números pares** no loop (step de 2)

---

*Gerado com apoio do GitHub Copilot — Aula 05 — Programação Assistida com IA*
