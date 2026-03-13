import os
import shutil
from pathlib import Path

# Diretórios
ori_ui_dir = r"c:\Users\Almeida\Desktop\Trabalhos\hospital-app\UI"
dest_dir = r"c:\Users\Almeida\Desktop\Trabalhos\hospital-app\interfaces"

# Mapeamento de ficheiros existentes para copiar
copy_mappings = {
    "medicos\Adiar.ui": "formAdiarConsulta.ui",
    "medicos\AdicionarMedicamento.ui": "formAdicionarMedicamento.ui",
    "medicos\Login.ui": "formLogin.ui",
    "medicos\Medicos.ui": "formMedicos.ui",
    "medicos\NovaReceita.ui": "formNovaReceita.ui",
    "Utentes\utente.ui": "formUtente.ui",
}

print("📋 Copiando ficheiros .ui existentes...")
for src, dest in copy_mappings.items():
    src_path = os.path.join(ori_ui_dir, src)
    dest_path = os.path.join(dest_dir, dest)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)
        print(f"✅ {src} → {dest}")
    else:
        print(f"❌ {src} não encontrado")

print("\n✨ Ficheiros copiados para interfaces/")
