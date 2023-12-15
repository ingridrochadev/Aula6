def realizar_divisao(entrada):
    try:
        divisao = 1 / entrada
        print(f"Resultado da divisão: {divisao}")
    except ZeroDivisionError:
        print("Não é possível fazer divisões por zero.") 
    except TypeError:
        print(f"Erro de tipo.")
    except Exception:
        print(f"Erro genérico.")
    finally:
        print("Olá! Meu nome é Ingrid!")

# Teste 1: Erro de divisão por zero
entrada1 = 0
entrada2 = 'teste'
entrada3 = 2

realizar_divisao(entrada1)
realizar_divisao(entrada2)
realizar_divisao(entrada3)
