import os

def converter_interfaces():
    # Converte os ficheiros .ui na pasta UI/medicos e UI/Utentes para ficheiros .py na pasta interfaces
    
    if not os.path.exists("interfaces"):
        os.makedirs("interfaces")
        
    ficheiros_ui = [
        ("UI/medicos/Adiar.ui", "interfaces/formAdiar.py"),
        ("UI/medicos/Login.ui", "interfaces/formLogin.py"),
        ("UI/medicos/Medicos.ui", "interfaces/formMedicos.py"),
        ("UI/Utentes/utente.ui", "interfaces/formUtente.py")
    ]
    
    for ui, py in ficheiros_ui:
        print(f"A converter {ui} para {py}...")
        os.system(f"pyuic5 {ui} -o {py}")
        
    print("Conversões concluídas!")

if __name__ == "__main__":
    converter_interfaces()