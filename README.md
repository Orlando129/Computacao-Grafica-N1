# Computação Gráfica - N1

Este projeto contém implementações de simulações interativas em Python usando NumPy e Pygame para demonstrar conceitos de transformações 3D e operadores afins.

## 👨‍💻 Autor

**Luiz Belispetre, João Lucas Camilo, Orlando Telles da Silva Batista**
- GitHub: [@Luiz](https://github.com/K4L1B3), [@João](https://github.com/joaolucascamilo), [@Orlando](https://github.com/Orlando129)
- Projeto: Computação Gráfica - Avaliação N1

## 🛠️ Pré-requisitos

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
python QuestõesFicha01/questao01/questao01.py

# Questão 3
python QuestõesFicha01/questao03/questao03.py
```

#### Questões da Ficha 01 (Three.js - Questões 02 e 04)

**Método 1: Servidor HTTP Local (Recomendado)**

1. Instale o http-server globalmente (se ainda não instalado):
   ```bash
   npm install -g http-server
   ```

2. Navegue até a pasta do projeto:
   ```bash
   cd QuestõesFicha01
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
   - **Questão 2A**: http://localhost:5500/questao02/2questaoA.html
   - **Questão 2B**: http://localhost:5500/questao02/2questaoB.html
   - **Questão 2C**: http://localhost:5500/questao02/2questaoC.html
   - **Questão 4**: http://localhost:5500/questao04/isnaiqueA.html

**Método 2: Servidor Python (Alternativa)**

```bash
cd QuestõesFicha01
python -m http.server 5500
```

Depois acesse: http://localhost:5500

#### Questões da Ficha 02 (Processing)
Abra os arquivos `.pde` no Processing IDE:
- **Questão 1**: `QuestõesFicha02/questao01/bola_quicando.pde`
- **Questão 2**: `QuestõesFicha02/questao02/braco_antebraco.pde`
- **Questão 3**: `QuestõesFicha02/questao03/circulo.pde`

Ou execute via linha de comando (se o Processing estiver no PATH):
```bash
# Questão 1
processing-java --sketch=QuestõesFicha02/questao01 --run

# Questão 2
processing-java --sketch=QuestõesFicha02/questao02 --run

# Questão 3
processing-java --sketch=QuestõesFicha02/questao03 --run
```

## 📊 Estrutura do Projeto

```
Computação-Grafica-N1/
├── QuestõesFicha01/
│   ├── questao01/
│   │   └── questao01.py      # Operadores afins com cubo
│   ├── questao02/
│   │   ├── 2questaoA.html    # Rotação em torno de arco
│   │   ├── 2questaoB.html    # Transformações em sequência
│   │   └── 2questaoC.html    # Reflexão e rotação
│   ├── questao03/
│   │   └── questao03.py      # Animação do pião
│   └── questao04/
│       └── isnaiqueA.html    # Projeto Three.js
├── QuestõesFicha02/
│   ├── questao01/
│   │   └── bola_quicando.pde # Animação de bola quicando
│   ├── questao02/
│   │   └── braco_antebraco.pde # Simulação de braço e antebraço
│   └── questao03/
│       └── circulo.pde       # Animação de círculo
├── requirements.txt          # Dependências do projeto
└── README.md                # Este arquivo
```

## 🔧 Dependências

- **NumPy 2.3.3**: Operações matriciais e cálculos numéricos
- **Pygame 2.6.1**: Interface gráfica e animações

---

**Nota**: Este projeto foi desenvolvido como parte da avaliação N1 da disciplina de Computação Gráfica, demonstrando a implementação prática de conceitos teóricos de transformações afins e animações 3D.