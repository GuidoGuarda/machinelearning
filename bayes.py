import numpy as np
def bayes_theorem(probA, probBgivenA, probB):
    """
    Calcula a probabilidade de A dado B utilizando o teorema de Bayes.

    Parameters:
    probA (float): Probabilidade a priori de A.
    probBgivenA (float): Probabilidade de B dado A.
    probB (float): Probabilidade a priori de B.

    Returns:
    float: Probabilidade de A dado B.
    """
    return (probA * probBgivenA) / probB


# Probabilidades fornecidas
pevasao = 0.2                         # P(evasao)
pdesempenhoruim = 0.3                 # P(desempenhoruim)
pdesempruim_evadiu = 0.7              # P(desempenhoruim | evadiu)

# Cálculo da probabilidade de evasão dado baixo desempenho
resultado = bayes_theorem(pevasao, pdesempruim_evadiu, pdesempenhoruim)

# Exibindo o resultado
print(f"A probabilidade de evasão escolar, se o aluno teve um desempenho ruim é de aproximadamente: {resultado:.2f}%")
