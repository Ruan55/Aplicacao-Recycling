from models.usuario import Usuario, PontosDeColeta, MaterialReciclavel
from services.servico_usuarios import UsuarioServicos, PontosDeColetaServicos, MaterialReciclavelServicos
from repositories.usuario_repositorios import UsuarioRepositorio, PontosDeColetaRepositorio, MaterialReciclavelRepositorio
from config.connection import Session
import os

def main():
    session = Session()
    repository = UsuarioRepositorio(session)
    service = UsuarioServicos(repository)

    while True:

        print("=== Recycling Eletronics Tech ===")
        print("1 - Cadastrar usuario")
        print("2 - Cadastrar ponto de coleta")
        print("3 - Cadastrar material reciclavel")
        print("4 - Listar informações do usuario")
        print("5 - Excluir Usuario")
        print("6 - Sair")
        opcoes = int(input("Escolha uma das opções acima: "))

        match opcoes:

            case 1:
                os.system("cls || clear")
                nome = str(input("Digite o seu nome: "))
                email = str(input("Digite o seu email: "))
                senha = str(input("Digite a sua senha: "))

                usuario = Usuario(nome=nome, email=email, senha=senha)
                session.add(usuario)
                session.commit()
                print()
            case 2:
                os.system("cls || clear")
                nome = str(input("Digite o nome do ponto de coleta: "))
                endereco = str(input("Digite o endereço do ponto de coleta: "))
                horariodefuncionamento = str(input("Digite o horário de funcionamento do ponto de coleta: "))

                pontosdecoleta = PontosDeColeta(nome=nome, endereco=endereco, hoarioFuncionamento=horariodefuncionamento)
                session.add(pontosdecoleta)
                session.commit()
                print()
            case 3:
                os.system("cls || clear")
                tipo = str(input("Digite o tipo de material reciclavel: "))
                descricao = str(input("Digite a descrição do seu material reciclavel: "))

                materialreciclavel = MaterialReciclavel(tipo=tipo, descricao=descricao)
                session.add(materialreciclavel)
                session.commit()
                print()
            case 4:
                os.system("cls || clear")
                informacoes_usuarios = session.query(Usuario).all()
                for usuario in informacoes_usuarios:
                    print(f"{usuario.nome} - {usuario.email} - {usuario.senha}")
                informacoes_pontos_de_coleta = session.query(PontosDeColeta).all()
                for pontosdecoleta in informacoes_pontos_de_coleta:
                    print(f"{pontosdecoleta.nome} - {pontosdecoleta.endereco} - {pontosdecoleta.horarioFuncionamento}")
                informacoes_material_reciclavel = session.query(MaterialReciclavel).all()
                for materialreciclavel in informacoes_material_reciclavel:
                    print(f"{materialreciclavel.tipo} - {materialreciclavel.descricao}")
            case 5:
                os.system("cls || clear")
                usuario_email = str(input("Digite o email do usuario: "))
                usuario = session.query(Usuario).filter_by(email=usuario_email).first()
                if usuario:
                    session.delete(usuario)
                    session.commit()
                    print("Usuario deletado com sucesso!")
                else:
                    print("Usuario não encontrado")
            case 6:
                os.system("cls || clear")
                print("Saindo... Até logo!")
                break

if __name__ == "__main__":
    os.system("cls || clear")
    main()            