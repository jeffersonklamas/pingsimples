#-----------------------------------------------------------
#
# Desenvolvendo código # para verificação de Ping básico
#
#-----------------------------------------------------------

# Pacotes
import os
from termcolor import colored

# Limpa tela ao iniciar a execução.
os.system('clear') or None

# Decoração básica
print(colored('$' * 120, 'blue', attrs=['dark']))

# Solicitação ao Usuário
ip_ou_host = input('\nDigite IP ou host a ser verificado: ')

# Decoração básica
print(colored('=' * 120, 'magenta', attrs=['dark']))

# Chamando comandos do sistema
os.system('ping -c 6 {}\n'.format(ip_ou_host))

# Decoração básica
print(colored('#' * 120, 'red', attrs=['dark']))
print('\n')
