def validator_of_response(inp):
    """
    Valida a continuação do loop.
    :param inp: Mensagem do input que será vista pelo usuário.
    :return: Resposta de sim ou não no caso s/n.
    """
    while True:
        stop = str(input(inp)).lower().strip()
        if stop not in "ns" or stop in "":
            print("\033[31mThis isn't accept. try again!\033[m")
            continue
        else:
            return stop


def validator_of_name(inp):
    """
    Valida o nome inserido.
    :param inp: Mensagem do input que será vista pelo usuário.
    :return: Nome do usuário.
    """
    while True:
        word_inp = str(input(inp)).strip().replace(" ", "")
        if word_inp.isalpha() is False:
            print("\033[31mThis isn't accept. try again!\033[m")
        else:
            return word_inp
