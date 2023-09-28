import winrm

# Dirección IP o nombre de host del equipo remoto
remote_host = 'localhost'
# Puerto de WinRM (predeterminado es 5985)
winrm_port = 5985

# Crea una sesión de WinRM
session = winrm.Session(
    remote_host,
    auth=(None, None),  # Deja en blanco para que solicite la autenticación
    transport='ntlm',
    server_cert_validation='ignore'
)

# Comando para habilitar una regla de firewall (ejemplo: File and Printer Sharing)
command = 'netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes'

# Ejecuta el comando a través de WinRM
result = session.run_ps(command)

# Verifica si la operación se completó con éxito
if result.status_code == 0:
    print("Regla del firewall habilitada correctamente.")
else:
    print(f"Hubo un error al habilitar la regla del firewall. Código de estado: {result.status_code}")
