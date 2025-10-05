## 📋 Descrição do Projeto

O projeto implementa simulações interativas em Python usando NumPy e Pygame para demonstrar conceitos fundamentais de computação gráfica:

### Questão 1 - Operadores Afins Notórios
Implementação de três operadores afins fundamentais:
- **A)** Rotação em torno de uma reta `s = {(x,y,z) | x=2 e y=1}`
- **B)** Reflexão em relação ao plano `C = {(x,y,z) | (0,1,0) + q(-2,4,-2) + p(-1,-1,1)}`
- **C)** Rotação helicoidal em torno da reta `D = (-t, 1-t, t)` com fator de translação `2/π`
- Composição final: **C∘B∘A** aplicada a um cubo unitário

### Questão 3 - Animação de Pião com Movimento Composto
Simulação de um pião executando movimentos compostos:
- Pião inicia com bico em `(1,2,0)`
- Gira **4 voltas** em torno do eixo `r = {(x,y,z) | x=1+q, y=2-q, z=0}` a cada período `t`
- Eixo `r` gira **1 volta** em torno do eixo `s = {(x,y,z) | x=2, y=1}` a cada período `t`

## 🛠️ Pré-requisitos

- **Python 3.7+**
- **pip** (gerenciador de pacotes Python)

## 🚀 Instalação e Execução

### 1. Clone o repositório
```bash
git clone https://github.com/Orlando129/Computacao-Grafica-N1.git
cd Computacao-Grafica-N1
```

### 2. Crie um ambiente virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute as questões

#### Questão 1 - Operadores Afins
```bash
python QuestõesFicha01/questao01.py
```

#### Questão 3 - Animação do Pião
```bash
python QuestõesFicha01/questao03.py
```

## 🎮 Controles das Simulações

### Questão 1 - Operadores Afins
- **ESPAÇO**: Play/Pause da animação
- **R**: Reset da animação
- **S**: Mostrar/ocultar etapas intermediárias
- **M**: Imprimir matrizes dos operadores no console
- **ESC**: Sair da aplicação

### Questão 3 - Animação do Pião
- **ESPAÇO**: Mostrar/ocultar matrizes no console
- **ESC**: Sair da aplicação

## 📊 Estrutura do Projeto

```
Computação-Grafica-N1/
├── QuestõesFicha01/
│   ├── questao01.py          # Operadores afins com cubo
│   └── questao03.py          # Animação do pião
├── requirements.txt          # Dependências do projeto
├── venv/                    # Ambiente virtual
└── README.md               # Este arquivo
```

## 🔬 Detalhes Técnicos

### Questão 1
- **Matemática**: Implementa operadores afins usando coordenadas homogêneas 4x4
- **Visualização**: Cubo unitário submetido às transformações
- **Composição**: Demonstra a ordem correta de aplicação das transformações
- **Matrizes**: Exibe as matrizes de transformação no console

### Questão 3
- **Transformações Compostas**: Rotações em torno de eixos arbitrários
- **Matriz de Rodrigues**: Para rotações em torno de eixos não-canônicos
- **Animação em Tempo Real**: 60 FPS com visualização suave
- **Física**: Movimento composto com múltiplas rotações simultâneas

## 🧮 Conceitos Matemáticos Implementados

1. **Coordenadas Homogêneas**: Sistema 4x4 para transformações afins
2. **Matriz de Rodrigues**: Rotação em torno de eixo arbitrário
3. **Composição de Transformações**: Multiplicação de matrizes na ordem correta
4. **Reflexão em Planos**: Usando vetores normais e produto escalar
5. **Rotação Helicoidal**: Combinação de rotação e translação
6. **Projeção 3D→2D**: Para visualização em tela

## 📈 Saídas do Programa

### Console
- Matrizes de transformação 4x4 em coordenadas homogêneas
- Informações sobre ângulos e posições em tempo real
- Debug de operações matemáticas

### Visualização
- Animações interativas em tempo real
- Objetos 3D projetados em 2D
- Interface com informações dinâmicas
- Controles visuais e legendas

## 🔧 Dependências

- **NumPy 2.3.3**: Operações matriciais e cálculos numéricos
- **Pygame 2.6.1**: Interface gráfica e animações
