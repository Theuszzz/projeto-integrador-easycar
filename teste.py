import os
import django
import sys
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easycar.settings')
django.setup()

from django.contrib.auth.models import User
from users.models import PerfilCliente
from cars.models import Carro
from rentals.models import Aluguel
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db.models import ProtectedError

def limpar_banco_teste():
    print("Limpando dados antigos de teste...")
    Aluguel.objects.all().delete()
    Carro.objects.filter(placa__in=['TEST-9999', 'TEST-8888']).delete()
    PerfilCliente.objects.all().delete()
    users_to_clean = ['func_teste', 'cli_teste', 'cli_impostor', 'cli_joao', 'cli_maria']
    User.objects.filter(username__in=users_to_clean).delete()

def rodar_testes():
    try:
        limpar_banco_teste()
        print("\nIniciando criação de dados...")

        func = User.objects.create_user('func_teste', 'func@teste.com', '123')
        cli = User.objects.create_user('cli_teste', 'cli@teste.com', '123')
        
        perfil = PerfilCliente.objects.create(
            user=cli, cnh='11111111111', telefone='11999999999', endereco='Rua A'
        )
        print(f"Cliente Base criado: {cli.username}")

        user_joao = User.objects.create_user('cli_joao', 'joao@teste.com', '123', first_name='João', last_name='Silva')
        perfil_joao = PerfilCliente.objects.create(
            user=user_joao,
            cnh='22222222222',
            telefone='11888888888',
            endereco='Av. Paulista, 1000'
        )
        print(f"Cliente criado: {user_joao.first_name} ({user_joao.username})")

        user_maria = User.objects.create_user('cli_maria', 'maria@teste.com', '123', first_name='Maria', last_name='Souza')
        perfil_maria = PerfilCliente.objects.create(
            user=user_maria,
            cnh='33333333333',
            telefone='21999997777',
            endereco='Rua Copacabana, 50'
        )
        print(f"Cliente criado: {user_maria.first_name} ({user_maria.username})")

        carro = Carro.objects.create(
            modelo='Carro Principal', placa='TEST-9999', ano=2024, status='disponivel', valor_diaria=120.00
        )
        print(f"Carro criado: {carro}")

        print("\nTeste 1: Impedir CNH duplicada...")
        cli_impostor = User.objects.create_user('cli_impostor', 'fake@teste.com', '123')
        try:
            PerfilCliente.objects.create(
                user=cli_impostor,
                cnh='11111111111',
                telefone='11888888888',
                endereco='Rua B'
            )
            print("ERRO: Permitiu CNH duplicada.")
        except IntegrityError:
            print("OK: Bloqueou CNH duplicada.")

        print("\nTeste 2: Impedir Placa duplicada...")
        try:
            Carro.objects.create(
                modelo='Carro Clone',
                placa='TEST-9999',
                ano=2024,
                valor_diaria=120.00
            )
            print("ERRO: Permitiu placa duplicada.")
        except IntegrityError:
            print("OK: Bloqueou placa duplicada.")

        print("\nTeste 3: Criar Aluguel...")
        aluguel = Aluguel.objects.create(
            perfil_cliente=perfil,
            carro=carro,
            funcionario=func,
            data_inicio=date.today(),
            data_fim=date.today() + timedelta(days=5),
            valor_total=500.00
        )
        
        qtd_registros = func.alugueis_registrados.count()
        if qtd_registros == 1:
            print("OK: Aluguel criado e vinculado.")
        else:
            print("ERRO: Vínculo falhou.")

        print("\nTeste 4: Impedir exclusão de carro alugado...")
        try:
            carro.delete()
            print("ERRO: Apagou carro alugado.")
        except ProtectedError:
            print("OK: Proteção funcionando.")

        print("\nTeste 5: Impedir exclusão de funcionário com histórico...")
        try:
            func.delete()
            print("ERRO: Apagou funcionário com histórico.")
        except ProtectedError:
            print("OK: Proteção funcionando.")

        print("\nTeste 6: Validar datas...")
        aluguel_ruim = Aluguel(
            perfil_cliente=perfil,
            carro=carro,
            funcionario=func,
            data_inicio=date.today(),
            data_fim=date.today() - timedelta(days=1),
            valor_total=100
        )
        try:
            aluguel_ruim.clean()
            print("ERRO: Clean não acusou data inválida.")
        except ValidationError:
            print("OK: Data inválida detectada.")

    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == '__main__':
    rodar_testes()
