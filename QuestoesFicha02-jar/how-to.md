# How to — Executar os Sketches (Windows) — Processing (Java)

Este guia explica como executar os três sketches em Processing (Java Mode) no Windows.

Sketckes:
- `QuestõesFicha02/questao01/bola_quicando.pde`
- `QuestõesFicha02/questao02/braco_antebraco.pde`
- `QuestõesFicha02/questao03/circulo.pde`

Repositório base: `C:\Users\SEU_USUARIO\three_cg\` (ajuste para a sua pasta)

---

## 1) Método recomendado: Processing IDE (GUI)

1. Baixe e instale o Processing 4:
   - Site oficial: `https://processing.org/download`
   - Extraia e abra `processing.exe`.

2. Abra cada sketch no IDE:
   - File → Open…
   - Selecione o arquivo `.pde` desejado:
     - `C:\Users\SEU_USUARIO\three_cg\QuestõesFicha02\questao01\bola_quicando.pde`
     - `C:\Users\SEU_USUARIO\three_cg\QuestõesFicha02\questao02\braco_antebraco.pde`
     - `C:\Users\SEU_USUARIO\three_cg\QuestõesFicha02\questao03\circulo.pde`
   - Se o IDE pedir para salvar em uma pasta com o nome do sketch, aceite.

3. Execute:
   - Clique no botão “Play” (▶).

Verificações visuais:
- `bola_quicando`: bola azul quica, invertendo a velocidade ao tocar paredes/chão/teto.
- `braco_antebraco`: braço (segmento 1) e antebraço (segmento 2) rotacionam por ~2s.
- `circulo`: bolinha azul rola sem deslizar em torno do círculo maior; ponto vermelho marca a rotação.

---

## 2) Método alternativo: Linha de Comando (processing-java)

Útil para rodar sem abrir o IDE (ainda abre uma janela do sketch).

1. Localize o `processing-java.exe`:
   - Ex.: `C:\Processing\processing-4.3\processing-java.exe`

2. Rode cada sketch (PowerShell):

- Questão 01 (bola quicando)
  ```powershell
  & "C:\Processing\processing-4.3\processing-java.exe" `
    --sketch "C:\Users\SEU_USUARIO\three_cg\QuestõesFicha02\questao01" `
    --run
  ```

- Questão 02 (braço e antebraço)
  ```powershell
  & "C:\Processing\processing-4.3\processing-java.exe" `
    --sketch "C:\Users\SEU_USUARIO\three_cg\QuestõesFicha02\questao02" `
    --run
  ```

- Questão 03 (círculo e bolinha rolando)
  ```powershell
  & "C:\Processing\processing-4.3\processing-java.exe" `
    --sketch "C:\Users\SEU_USUARIO\three_cg\QuestõesFicha02\questao03" `
    --run
  ```

Dicas:
- Para apresentação em tela cheia: troque `--run` por `--present`.
- Se usar CMD, remova os acentos no caminho ou use aspas e paths curtos (ou rode a partir de um caminho sem acentos).

---

## Requisitos e Notas

- Não há dependências externas — apenas Processing (Java Mode).
- Java já vem embutido no Processing 4.
- Caso o Windows SmartScreen bloqueie, permita a execução do `processing.exe`.
- Se a janela não abrir:
  - Verifique se o antivírus não bloqueou.
  - Tente rodar o IDE como Administrador.
  - Confirme se o caminho do projeto existe e contém o `.pde`.

---

## Estrutura esperada

three_cg/
└── QuestõesFicha02/
├── questao01/
│ └── bola_quicando.pde
├── questao02/
│ └── braco_antebraco.pde
└── questao03/
└── circulo.pde

Se os `.pde` estiverem em outras pastas, ajuste os caminhos nos comandos acima.

---

## Problemas comuns (Windows)

- Caminhos com acentos/espaços:
  - Use aspas em todo o path, ex.: `"C:\Users\...\QuestõesFicha02\questao01"`.
  - Ou mova o projeto para um caminho sem acentos, ex.: `C:\cg\three_cg\`.

- Performance baixa:
  - Feche outras aplicações.
  - Reduza a resolução alterando `size()` no `setup()` de cada sketch.

- Sem imagem/erro de render:
  - Atualize drivers gráficos.
  - Teste no Processing IDE antes de usar a CLI.

---