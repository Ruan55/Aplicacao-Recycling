from models.usuario import Usuario, PontosDeColeta, MaterialReciclavel
from repositories.usuario_repositorios import UsuarioRepositorio, PontosDeColetaRepositorio, MaterialReciclavelRepositorio

class UsuarioServicos:
    def __init__(self, repository: UsuarioRepositorio) -> None:
        self.repository = repository

    def cadastrar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            registrado = self.repository.procurar_por_email_do_usuario(email=usuario.email)

            if registrado:
                print("Usuário já cadastrado!")
                return
            
            self.repository.salvar_usuario(usuario=usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as error:
            print(f"Erro ao salvar o usuário: {error}")
        except Exception as error:
            print(f"Ocorreu um erro inesperado: {error}")

    def listar_todos_os_usuarios(self):
        return self.repository.listar_usuarios()
    
class PontosDeColetaServicos:
    def __init__(self, repository: PontosDeColetaRepositorio) -> None:
        self.repository = repository

    def cadastrar_ponto_de_coleta(self, nome: str, endereco: str, horariodefuncionamento: str):
        try:
            pontodecoleta = PontosDeColeta(nome=nome, endereco=endereco, hoarioFuncionamento=horariodefuncionamento)

            registrado = self.repository.procurar_pontos_de_coleta_por_nome(nome=pontodecoleta.nome)

            if registrado:
                print("Ponto de coleta cadastrado!")
                return
            
            self.repository.salvar_pontos_de_coleta(pontosdecoleta=pontodecoleta)
            print("Ponto de coleta cadastrado com sucesso!")
        except TypeError as error:
            print(f"Erro aos salvar o ponto de coleta: {error}")
        except Exception as error:
            print(f"Ocorreu um erro inesperado: {error}")


class MaterialReciclavelServicos:
    def __init__(self, repository: MaterialReciclavelRepositorio) -> None:
        self.repository = repository
    
    def cadastrar_material_reciclavel(self, nome: str, tipo: str, descricao: str):
        try:
            materialreciclavel = MaterialReciclavel(nome=nome, tipo=tipo, descricao=descricao)
            
            self.repository.salvar_tipo_material_reciclavel(materialreciclavel=materialreciclavel)
            print("Material Reciclavel cadastrado com sucesso!")
        except TypeError as error:
            print(f"Erro aos salvar o material reciclavel: {error}")
        except Exception as error:
            print(f"Ocorreu um erro inesperado: {error}")