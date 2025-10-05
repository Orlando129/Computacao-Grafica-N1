# Computação Gráfica - N1

Este projeto contém implementações de simulações interativas utilizando diferentes tecnologias (Python/Pygame, Three.js e Processing) para demonstrar conceitos de computação gráfica, incluindo transformações 3D, operadores afins e animações interativas.

## 👨‍💻 Autores

**Luiz Belispetre, João Lucas Camilo, Orlando Telles da Silva Batista**
- GitHub: [@Luiz](https://github.com/K4L1B3)
          [@João](https://github.com/joaolucascamilo)
          [@Orlando](https://github.com/Orlando129)
- Projeto: Computação Gráfica - Avaliação N1

## � Avaliação e Pesos

### Distribuição de Notas
- **Ficha 01**: 40% da nota final
- **Ficha 02**: 60% da nota final
- **Questão 04**: Possui menor peso entre as questões da Ficha 01

## �🛠️ Pré-requisitos

- **Python 3.7+**
- **pip** (gerenciador de pacotes Python)
- **Node.js** (para servidor HTTP local - questões Three.js)
- **Processing** (para executar as questões da Ficha 02)
- **Navegador moderno** com suporte a WebGL

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

### 4. Execute o projeto

#### Questões da Ficha 01 (Python - Questões 01 e 03)
```bash
# Questão 1
python QuestoesFicha01-py/questao01.py

# Questão 3
python QuestoesFicha01-py/questao03.py
```

#### Questões da Ficha 01 (Three.js - Questões 02 e 04)

**Método 1: Servidor HTTP Local (Recomendado)**

1. Instale o http-server globalmente (se ainda não instalado):
   ```bash
   npm install -g http-server
   ```

2. Navegue até a pasta do projeto:
   ```bash
   cd QuestoesFicha01-js
   ```

3. Inicie o servidor HTTP:
   ```bash
   npx http-server -p 5500
   ```
   
   Ou se instalado globalmente:
   ```bash
   http-server -p 5500
   ```

4. Abra o navegador e acesse:
   - **Questão 2**: http://localhost:5500/questão-2-ficha-1/
   - **Questão 4**: http://localhost:5500/questao-4-ficha-1/

**Método 2: Servidor Python (Alternativa)**

```bash
cd QuestoesFicha01-js
python -m http.server 5500
```

Depois acesse: http://localhost:5500

#### Questões da Ficha 02 (Processing)
Abra os arquivos `.pde` no Processing IDE:
- **Questão 1**: `QuestoesFicha02-jar/questao01/`
- **Questão 2**: `QuestoesFicha02-jar/questao02/`
- **Questão 3**: `QuestoesFicha02-jar/questao03/`

Ou execute via linha de comando (se o Processing estiver no PATH):
```bash
# Questão 1
processing-java --sketch=QuestoesFicha02-jar/questao01 --run

# Questão 2
processing-java --sketch=QuestoesFicha02-jar/questao02 --run

# Questão 3
processing-java --sketch=QuestoesFicha02-jar/questao03 --run
```

## 📊 Estrutura do Projeto

```
Computação-Grafica-N1/
├── QuestoesFicha01-py/          # Questões Python da Ficha 01
│   ├── questao01.py             # Operadores afins com cubo
│   ├── questao03.py             # Animação do pião
│   └── how-to.md                # Instruções de execução
├── QuestoesFicha01-js/          # Questões Three.js da Ficha 01
│   ├── questão-2-ficha-1/       # Questão 2 (A, B, C)
│   ├── questao-4-ficha-1/       # Questão 4
│   └── how-to.md                # Instruções de execução
├── QuestoesFicha02-jar/         # Questões Processing da Ficha 02
│   ├── questao01/               # Animação de bola quicando
│   ├── questao02/               # Simulação de braço e antebraço
│   ├── questao03/               # Animação de círculo
│   └── how-to.md                # Instruções de execução
├── venv/                        # Ambiente virtual Python
├── requirements.txt             # Dependências Python
├── .gitignore                   # Arquivos ignorados pelo Git
└── README.md                    # Este arquivo
```

## 🔧 Dependências

### Python (Questões 01 e 03 - Ficha 01)
- **NumPy 2.3.3**: Operações matriciais e cálculos numéricos
- **Pygame 2.6.1**: Interface gráfica e animações

### Three.js (Questões 02 e 04 - Ficha 01)
- **Three.js**: Biblioteca JavaScript para renderização 3D (incluída via CDN nos arquivos HTML)
- **Servidor HTTP**: Node.js com http-server ou Python SimpleHTTPServer

### Processing (Ficha 02)
- **Processing IDE**: Ambiente de desenvolvimento para linguagem Processing
- **processing-java**: CLI para execução via linha de comando (opcional)

---

**Nota**: Este projeto foi desenvolvido como parte da avaliação N1 da disciplina de Computação Gráfica, demonstrando a implementação prática de conceitos teóricos de transformações afins e animações 3D.