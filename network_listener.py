import socket
import json
from winotify import Notification, audio

PORTA_REDE = 9999

def iniciar_receptor():
    # Prepara o socket para escutar avisos na rede local
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", PORTA_REDE))
    
    print(f"Ouvinte iniciado! Aguardando alertas na porta {PORTA_REDE}...")
    
    while True:
        try:
            # Aguarda receber uma mensagem
            dados, endereco = sock.recvfrom(1024)
            info = json.loads(dados.decode('utf-8'))
            
            print(f"Alerta recebido de {endereco[0]}!")
            
            # Dispara o popup do Windows
            notificacao = Notification(
                app_id="🟡 Alerta de Segurança!",
                title="Modificação de Arquivo detectada!",
                msg=f"Arquivo: {info['nome']}\n {info['data']}\n Original: {info['original']}",
                icon=r"C:\Users\matheus\Desktop\CFPM\assets\\geodrive.png", # Ajuste o caminho se necessário nestes PCs
                duration="long"
            )
            notificacao.set_audio(audio.LoopingAlarm10, loop=False)
            notificacao.add_actions(label="Abrir Pasta de Destino", launch="C:\\Users\\matheus\\Desktop\\CFPM\\checkfolder")
            notificacao.show()
            
        except Exception as e:
            print(f"Erro ao processar aviso recebido: {e}")

if __name__ == "__main__":
    iniciar_receptor()
