# 👾 RARL

## ´´Receptor de Alertas em Rede Local´´

Este código implementa um receptor de alertas via rede local (LAN) utilizando protocolo UDP.

O sistema fica escutando mensagens JSON enviadas por outros dispositivos e, ao receber um alerta, exibe uma notificação nativa do Windows usando a biblioteca Winotify.
O objetivo principal do script é atuar como um cliente de monitoramento, notificando o usuário sobre modificações em arquivos compartilhados ou monitorados.

## ´´Funcionamento Geral´´

Fluxo do sistema:

  Outro computador/sistema
          ↓
   Envia pacote UDP JSON
          ↓
   Socket recebe dados
          ↓
   JSON é convertido em dicionário Python
          ↓
   Notificação do Windows é criada
          ↓
   Usuário recebe popup visual + som

## ´´Biblioteca padrão do Python utilizada para comunicação em rede.´´

Funções usadas:

Criação do socket UDP
Escuta de mensagens na rede
Recebimento de pacotes

## ´´json.´´

Responsável por converter os dados recebidos no formato JSON para objetos Python.

Exemplo esperado:

{
    "nome": "arquivo.txt",
    "data": "07/05/2026 10:15",
    "original": "usuario_original"
}

## ´´winotify´´

Biblioteca responsável por gerar notificações nativas do Windows 10/11.

Recursos usados:

Popup toast notification
Sons personalizados
Botão de ação
Ícone personalizado

## ´´Constante Global.´´

PORTA_REDE = 9999

Define a porta UDP utilizada para receber os alertas.

Observações
Todos os dispositivos precisam usar a mesma porta.
A porta deve estar liberada no firewall do Windows.

## ´´Função Principal.´´

iniciar_receptor()

Responsável por:

  Criar o socket UDP
  Escutar mensagens continuamente
  Interpretar os dados recebidos
  Exibir notificações no Windows

## ´´Análise Linha por Linha.´´

´´Criação do socket´´

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

## Explicação

Cria um socket:

  AF_INET
  → utiliza IPv4
  SOCK_DGRAM
  → protocolo UDP
  
Características do UDP

  Mais rápido
  Sem confirmação de entrega
  Ideal para alertas rápidos
  Não mantém conexão contínua
  
Bind do socket

sock.bind(("0.0.0.0", PORTA_REDE))

Explicação

Faz o programa escutar em:

0.0.0.0

Que significa:

## ´´Escutar em todas as interfaces de rede disponíveis.´´

Exemplos:

  Wi-Fi
  Ethernet
  Rede local
  VPN

## ´´Compatibilidade.´´

Sistema	      Compatível

Windows 10	  Sim
Windows 11	  Sim
Linux	        Não
macOS	        Não

## ´´Resumo Técnico.´´

Item               Tecnologia
Comunicação        UDP
Porta              9999
Formato	           JSON
Notificação	       Windows Toast
Biblioteca visual	 Winotify
Rede	             LAN
Protocolo          IPv4
