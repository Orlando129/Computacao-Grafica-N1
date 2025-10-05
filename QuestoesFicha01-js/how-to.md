# Projeto Three.js - Computação Gráfica

Este projeto contém demonstrações interativas de transformações 3D usando Three.js, organizadas em três questões práticas de computação gráfica.

## 📋 Visão Geral

O projeto demonstra diferentes conceitos de computação gráfica através de visualizações 3D interativas:

- **Questão A**: Rotação em torno de um arco centrado em um ponto específico
- **Questão B**: Sequência de transformações (Rotação → Escala → Translação) com animação em etapas
- **Questão C**: Reflexão no plano e rotação, com duas modalidades de visualização

## 🚀 Como Executar

### Pré-requisitos

- Node.js instalado (para usar o servidor HTTP)
- Navegador moderno com suporte a WebGL

### Método 1: Servidor HTTP Local (Recomendado)

1. **Instale o http-server globalmente** (se ainda não instalado):
   ```bash
   npm install -g http-server
   ```

2. **Navegue até a pasta do projeto**:
   ```bash
   cd /caminho/para/three_cg
   ```

3. **Inicie o servidor HTTP**:
   ```bash
   npx http-server -p 5500
   ```
   
   Ou se instalado globalmente:
   ```bash
   http-server -p 5500
   ```

4. **Abra o navegador** e acesse:
   - http://127.0.0.1:5500
   - http://localhost:5500

### Método 2: Servidor Python (Alternativa)

Se preferir usar Python:

```bash
# Python 3
python -m http.server 5500

# Python 2
python -m SimpleHTTPServer 5500
```

Depois acesse: http://localhost:5500

### Método 3: Abrir Diretamente (Limitado)

⚠️ **Nota**: Alguns recursos podem não funcionar devido às restrições CORS do navegador
- Abra qualquer arquivo `.html` diretamente no navegador

## 📁 Estrutura do Projeto
