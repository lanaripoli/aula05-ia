# Prática 1 — IA como Copiloto
# Função que verifica se um número é primo

# ===== VERSÃO INICIAL (gerada pela IA) =====

def is_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Teste
numero = 17
if is_primo(numero):
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")


# ===== VERSÃO OTIMIZADA (clean code, boas práticas) =====

import math

def is_prime(number: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é aquele divisível apenas por 1 e por ele mesmo.
    Esta versão otimizada verifica divisores apenas até a raiz quadrada
    do número, reduzindo o número de iterações necessárias.

    Args:
        number (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
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


# ===== Exemplos de uso =====

test_numbers = [1, 2, 3, 4, 13, 17, 20, 97, 100]

for num in test_numbers:
    result = "primo ✅" if is_prime(num) else "não primo ❌"
    print(f"{num:>4} → {result}")
