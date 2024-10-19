import random

def criar_predio_com_elevador():
  
  predio = [[0 for _ in range(3)] for _ in range(6)]
  
  elevador = {
    "andar_atual": 0,
    "destino": None,
    "estado": 0
  }

  return predio, elevador


def status_apartamentos(predio):

  apartamentos_ocupados_total = 0
  apartamentos_vazios_total = 0
  apartamentos_existentes_total = 0

  apartamentos_ocupados_por_andar = {}
  apartamentos_vazios_por_andar = {}

  for andar, apartamentos in enumerate(predio):
    apartamentos_ocupados = sum(1 for apt in apartamentos if apt == 1)
    apartamentos_vazios = sum(1 for apt in apartamentos if apt == 0)
    apartamentos_existentes = len(apartamentos)

    apartamentos_ocupados_total += apartamentos_ocupados
    apartamentos_vazios_total += apartamentos_vazios
    apartamentos_existentes_total += apartamentos_existentes

    apartamentos_ocupados_por_andar[andar] = apartamentos_ocupados
    apartamentos_vazios_por_andar[andar] = apartamentos_vazios

  return {
    "ocupados_total": apartamentos_ocupados_total,
    "vazios_total": apartamentos_vazios_total,
    "existentes_total": apartamentos_existentes_total,
    "ocupados_por_andar": apartamentos_ocupados_por_andar,
    "vazios_por_andar": apartamentos_vazios_por_andar
  }


def adicionar_pessoa_no_apartamento(predio, andar):
  
  apartamentos = predio[andar]

  if 0 in apartamentos:
    apartamento_index = apartamentos.index(0)
    predio[andar][apartamento_index] = 1
    print(f"Pessoa alocada no andar {andar}, apartamento {apartamento_index}.")
  
  else:
    print("Todos os apartamentos estão ocupados.")


def remover_pessoa_do_apartamento(predio, andar):
    
    apartamentos = predio[andar]
    
    if 1 in apartamentos:
      apartamento_index = apartamentos.index(1)
      predio[andar][apartamento_index] = 0
      print(f"Pessoa removida do andar {andar}, apartamento {apartamento_index}.")
    
    else:
      print("Nenhuma pessoa para remover, todos os apartamentos estão vazios.")


def viajar_elevador(elevador, predio, origem, destino):
  
  print(f"\nElevador vai do andar {origem} para o andar {destino}.")
  
  if elevador["estado"] == 1:
    
    if origem != 0 and destino == 0:
      remover_pessoa_do_apartamento(predio, origem)
    
    elif origem == 0 and destino != 0:
      adicionar_pessoa_no_apartamento(predio, destino)

  elevador["origem"] = destino
  elevador["destino"] = None
  elevador["estado"] = 0
  
  print(f"Estado do elevador após a viagem: {elevador}")


def calcular_probabilidade_movimento(elevador, status):

  probabilidade_movimentar = 0
  probabilidade_permanecer = 0

  if elevador["andar_atual"] == 0:
    
    if elevador["estado"] == 0:
    
      if status["ocupados_total"] > 0:
        probabilidade_movimentar = status["ocupados_total"] /  status["existentes_total"]
        probabilidade_permanecer = status["vazios_total"] /  status["existentes_total"]
    
      else:
        probabilidade_movimentar = 0
        probabilidade_permanecer = 1
    
    elif elevador["estado"] == 1:
      probabilidade_permanecer = 0
      probabilidade_movimentar = 1


  elif elevador["andar_atual"] != 0:
    
    if elevador["estado"] == 0:
      probabilidade_movimentar = 0.5
      probabilidade_permanecer = 0.5
    
    elif elevador["estado"] == 1:
      probabilidade_permanecer = 0
      probabilidade_movimentar = 1

  return probabilidade_movimentar, probabilidade_permanecer


def sortear_movimento_com_probabilidade(probabilidade_movimentar, probabilidade_permanecer):
  opcoes = ['movimentar', 'permanecer']
  probabilidades = [probabilidade_movimentar, probabilidade_permanecer]
  resultado = random.choices(opcoes, probabilidades)[0]
  return resultado


def probabilidade_movimento_por_andar(opcoes, elevador, status):
  probabilidades = {}

  if opcoes == 'movimentar':
    
    if elevador["andar_atual"] == 0:
      
      if elevador["estado"] == 0:
        probabilidade_movimentar_destino_terreo = 0
        probabilidades[0] = probabilidade_movimentar_destino_terreo
        
        for andar in range(1, len(status["ocupados_por_andar"])):
          probabilidade_movimentar_destino_andar = status["ocupados_por_andar"][andar] / status["existentes_total"]
          probabilidades[andar] = probabilidade_movimentar_destino_andar

      elif elevador["estado"] == 1:
        probabilidade_movimentar_destino_terreo = 0
        probabilidades[0] = probabilidade_movimentar_destino_terreo
        
        for andar in range(1, len(status["vazios_por_andar"])):
          probabilidade_movimentar_destino_andar = status["vazios_por_andar"][andar] / status["existentes_total"]
          probabilidades[andar] = probabilidade_movimentar_destino_andar


    elif elevador["andar_atual"] != 0:
      
      if elevador["estado"] == 0:
        
        if status["ocupados_total"] == status["existentes_total"]:
          probabilidade_movimentar_destino_terreo = 0
          probabilidades[0] = probabilidade_movimentar_destino_terreo
          
          for andar in range(1, len(status["ocupados_por_andar"])):
            probabilidade_movimentar_destino_andar = status["ocupados_por_andar"][andar] / status["existentes_total"]
            probabilidades[andar] = probabilidade_movimentar_destino_andar
        
        else:
          probabilidade_movimentar_destino_terreo = status["vazios_total"] / status["ocupados_total"]

          for andar in range(1, len(status["ocupados_por_andar"])):
            probabilidade_movimentar_destino_andar = status["ocupados_por_andar"][andar] / status["existentes_total"]
            probabilidades[andar] = probabilidade_movimentar_destino_andar
      
      elif elevador["estado"] == 1:
        probabilidade_movimentar_destino_terreo = 1
        probabilidades[0] = probabilidade_movimentar_destino_terreo

  return probabilidades


"""def chamar_elevador(predio, elevador):
  destino = sortear_destino_com_probabilidade(predio, elevador)
  if destino is not None:
    print(f"\nElevador chamado para o andar {destino}.")
    viajar_elevador(elevador, predio, elevador["origem"], destino)
    apartamento = encontrar_apartamento_ocupado(predio, destino)
    if apartamento is not None:
      elevador["estado"] = "ocupado"
    else:
      elevador["estado"] = "vazio"
  else:
    print("Nenhum destino encontrado, ninguém chamou o elevador.")"""
