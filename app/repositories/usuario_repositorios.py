from models.usuario import Usuario, PontosDeColeta, MaterialReciclavel
from sqlalchemy.orm import Session

class UsuarioRepositorio:
    def __init__(self, session: Session) -> None:
        self.session = Session

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()

    def procurar_por_email_do_usuario(self, email:str):
        return self.session.query(Usuario).filter_by(email = email).first()
    
    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()

    def listar_usuarios(self):
        return self.session.query(Usuario).all()
    
class PontosDeColetaRepositorio:
    def __init__(self, session: Session):
        self.session = Session

    def salvar_pontos_de_coleta(self, pontosdecoleta: PontosDeColeta):
        self.session.add(pontosdecoleta)
        self.session.commit()
    
    def procurar_pontos_de_coleta_por_nome(self, nome:str):
        return self.session.query(PontosDeColeta).filter_by(nome = nome).first()

    def listar_horario_de_funcionamento_pontos_de_coleta(self):
        return self.session.query(PontosDeColeta).all()
    
class MaterialReciclavelRepositorio:
    def __init__(self, session: Session):
        self.session = Session
    
    def salvar_tipo_material_reciclavel(self, materialreciclavel: MaterialReciclavel):
        self.session.add(materialreciclavel)
        self.session.commit()

    def salvar_descricao_material_reciclavel(self, materialreciclavel: MaterialReciclavel):
        self.session.add(materialreciclavel)
        self.session.commit()