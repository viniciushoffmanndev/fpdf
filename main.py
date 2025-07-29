from fpdf import FPDF

# Conteúdo do capítulo 1
<<<<<<< HEAD
=======
titulo = "O Primeiro Script que Mudou Tudo"
>>>>>>> efffe7a (feat(main): Alterado o print())
conteudo = """
Capítulo 1: O Primeiro Script que Mudou Tudo

Era uma tarde comum, mas aquele simples arquivo .py mudaria para sempre a forma como eu via problemas.
Na tela, o cursor piscava, esperando por algo. Eu digitei:

python
print("Olá, mundo!")

E ao pressionar Enter, algo mágico aconteceu. Pela primeira vez, eu havia dado uma instrução para o computador - e ele obedeceu.
Mas aquilo era só o começo.

Nos dias seguintes, mergulhei em estruturas de controle, listas, dicionários e funções. Descobri que com for e if, eu podia automatizar tarefas que antes levavam horas. Com def, eu criava minhas próprias ferramentas. E com import, eu trazia o poder de bibliotecas inteiras para o meu projeto.

Foi então que percebi: programar não é apenas escrever código. É transformar ideias em soluções.
"""

# Criar o PDF com formatação aprimorada
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_left_margin(20)
pdf.set_right_margin(20)
pdf.set_font("Helvetica", size=12)

# Adicionar o conteúdo com alinhamento justificado e espaçamento entre parágrafos
for paragrafo in conteudo.strip().split('\n\n'):
    pdf.multi_cell(0, 8, paragrafo, align='J')
    pdf.ln(4)  # Espaço entre parágrafos

# Salvar o PDF
pdf.output("O Primeiro Script que Mudou Tudo.pdf")

<<<<<<< HEAD
print("Relatório PDF formatado gerado com sucesso: relatorio_estrutura_cocalgpt_formatado.pdf")
=======
print(f"Criado com sucesso: {titulo}.pdf !")
>>>>>>> efffe7a (feat(main): Alterado o print())

