def validator(cpf):
    if len(cpf) == 11:
        cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]

    prototype_cpf = cpf.split("-")[0].replace(".", "")

    prototype_cpf += _calculator_cpf(prototype_cpf)
    prototype_cpf += _calculator_cpf(prototype_cpf)

    new_cpf = prototype_cpf[:3] + "." + prototype_cpf[3:6] + "." + prototype_cpf[6:9] + "-" + prototype_cpf[9:]

    print(f'\nValidating {cpf}\n...')
    print("Valid CPF!" if cpf == new_cpf else f"Invalid CPF!")


def _calculator_cpf(cpf):
    counts = []
    start = 11 if len(cpf) > 9 else 10
    for i, v in enumerate(range(start, 1, -1)):
        num = int(cpf[i]) * v
        counts.append(num)

    total = sum(counts)
    num_generated = 11 - (total % 11)
    return "0" if num_generated > 9 else str(num_generated)
