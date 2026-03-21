# ============================================================
# CLASSE DISCIPLINA
# ============================================================
class Disciplina:
    """ Representa uma disciplina do curso de Sistemas de Informação.
    Na Lógica de Predicados:
    - Cada objeto Disciplina é um FATO da base de conhecimento.
    - Predicados representados:, Disciplina(d), Area(d, a), Obrigatoria(d)
    Eletiva(d), Requisito(d, r) """

    def __init__(self, codigo, nome, area,
                 obrigatoria=False, bloco=None, requisito=None):
        self.codigo = codigo              # Código da disciplina
        self.nome = nome                  # Nome da disciplina
        self.area = area                  # Área de conhecimento
        self.obrigatoria = obrigatoria    # True = obrigatória | False = eletiva
        self.bloco = bloco                # Bloco/período do curso
        self.requisito = requisito        # Pré-requisito
# ============================================================
# CLASSE SISTEMA DE RECOMENDAÇÃO
# ============================================================
class SistemaRecomendacao:
    """ Sistema Inteligente de Apoio ao Aluno (SIAA)
    Baseado em:
    - Lógica de Predicados de Primeira Ordem
    - Quantificador Universal (∀)
    - Quantificador Existencial (∃)
    - Inferência lógica por Modus Ponens """
    def __init__(self):
        # Base de conhecimento do sistema
        self.disciplinas = self._carregar_disciplinas()

    # ========================================================
    # BASE DE CONHECIMENTO
    # ========================================================
    def _carregar_disciplinas(self):
        """
        Cria a base de conhecimento contendo:
        - Disciplinas obrigatórias do curso
        - Disciplinas eletivas
        """
        return [

            # ---------------- OBRIGATÓRIAS ----------------
            Disciplina("SI06008", "Programação de Computadores I",
                       "Programação", obrigatoria=True, bloco=2),

            Disciplina("SI06014", "Programação de Computadores II",
                       "Programação", obrigatoria=True, bloco=3,
                       requisito="Programação de Computadores I"),

            Disciplina("SI06017", "Estrutura de Dados",
                       "Programação", obrigatoria=True, bloco=3,
                       requisito="Programação de Computadores II"),

            Disciplina("SI06019", "Banco de Dados I",
                       "Dados", obrigatoria=True, bloco=4),

            Disciplina("SI06026", "Redes de Computadores",
                       "Infraestrutura", obrigatoria=True, bloco=5),

            Disciplina("SI06038", "Lógica Aplicada a Sistemas de Informação",
                       "Fundamentos", obrigatoria=True, bloco=6),

            # ---------------- ELETIVAS ----------------
            Disciplina("EL001", "Mineração de Dados",
                       "Dados", requisito="Banco de Dados I"),

            Disciplina("EL002", "Inteligência Artificial",
                       "IA", requisito="Lógica Aplicada a Sistemas de Informação"),

            Disciplina("EL003", "Sistemas Distribuídos Avançados",
                       "Infraestrutura", requisito="Redes de Computadores"),

            Disciplina("EL004", "Computação Gráfica",
                       "Visual", requisito="Programação de Computadores II"),

            Disciplina("EL005", "Desenvolvimento de Jogos",
                       "Desenvolvimento", requisito="Programação de Computadores II"),
        ]

    # ========================================================
    # OBTÉM DISCIPLINAS OBRIGATÓRIAS
    # ========================================================
    def listar_obrigatorias(self):
        """
        Retorna todas as disciplinas obrigatórias.
        """
        return [d for d in self.disciplinas if d.obrigatoria]

    # ========================================================
    # EXECUÇÃO DO SISTEMA
    # ========================================================
    def executar(self):
        print("=" * 70)
        print("SISTEMA INTELIGENTE DE APOIO AO ALUNO (SIAA)")
        print("=" * 70)

        nome_aluno = input("Digite o nome do aluno: ").strip()

        # ====================================================
        # REGRA LÓGICA 1 — HISTÓRICO ACADÊMICO
        #
        # ∀d [ Cursou(aluno, d) ∧ Obrigatoria(d) → Aptidao(aluno) ]
        # ====================================================
        print("\nSelecione as DISCIPLINAS OBRIGATÓRIAS já cursadas:")

        obrigatorias = self.listar_obrigatorias()

        for i, d in enumerate(obrigatorias, 1):
            print(f"{i}. {d.nome}")

        try:
            entrada = input("\nDigite os números separados por vírgula: ")
            indices = [int(i.strip()) - 1 for i in entrada.split(",")]

            cursadas = [obrigatorias[i].nome for i in indices]

            # ====================================================
            # QUANTIFICADOR UNIVERSAL (∀)
            #
            # Para toda disciplina eletiva e:
            # se o aluno cursou o requisito de e,
            # então e é uma disciplina apta.
            # ====================================================
            eletivas = [d for d in self.disciplinas if not d.obrigatoria]

            aptas = [
                d for d in eletivas
                if d.requisito in cursadas
            ]

            if not aptas:
                print("\nNenhuma disciplina eletiva disponível para seu histórico.")
                return

            # ====================================================
            # REGRA LÓGICA 2 — INTERESSE
            #
            # ∀x [ Interesse(aluno, a) ∧ Area(x, a) → Recomendar(x) ]
            # ====================================================
            print("\nSelecione a área de interesse:")

            areas = sorted(set(d.area for d in aptas))

            for i, area in enumerate(areas, 1):
                print(f"{i}. {area}")

            escolha = int(input("\nEscolha a área: "))
            area_interesse = areas[escolha - 1]

            # ====================================================
            # INFERÊNCIA — MODUS PONENS
            #
            # Premissa: Se a disciplina pertence à área de interesse,
            # então deve ser recomendada.
            # ====================================================
            recomendadas = [
                d for d in aptas if d.area == area_interesse
            ]

            print("\n" + "=" * 70)
            print(f" RECOMENDAÇÃO ACADÊMICA PARA: {nome_aluno.upper()}")
            print("=" * 70)

            for d in recomendadas:
                print(f"{d.nome} | Área: {d.area}")

            print("\nFundamentação: Inferência lógica por Modus Ponens.")

        except (ValueError, IndexError):
            print("\nErro: Entrada inválida. Tente novamente.")

# ============================================================
# EXECUÇÃO
# ============================================================
if __name__ == "__main__":
    sistema = SistemaRecomendacao()
    sistema.executar()
