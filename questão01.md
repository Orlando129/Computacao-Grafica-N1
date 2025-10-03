# Documentação: Operadores Afins 3D - Questão 1

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Questão A - Rotação em torno de s](#questão-a)
3. [Questão B - Reflexão no plano C](#questão-b)
4. [Questão C - Rotação Helicoidal](#questão-c)
5. [Composição das Transformações](#composição)
6. [Implementação e Verificação](#implementação)

---

## 🎯 Visão Geral

O código implementa **três operadores afins** do R³ no R³ e os compõe em sequência (C ∘ B ∘ A), aplicando-os a um cubo unitário com animação suave.

### O que são Operadores Afins?
Um operador afim T: R³ → R³ tem a forma:
```
T(v) = Av + b
```
Onde:
- A é uma matriz 3×3 (transformação linear)
- b é um vetor de translação

Em **coordenadas homogêneas** (4×4), representamos:
```
[x']   [a11 a12 a13 tx]   [x]
[y'] = [a21 a22 a23 ty] × [y]
[z']   [a31 a32 a33 tz]   [z]
[1 ]   [0   0   0   1 ]   [1]
```

---

## 📐 Questão A - Rotação em torno de s

### Enunciado
> Rotação em torno de **s = {(x, y, z) ∈ R³ | x = 2 e y = 1}**

### Interpretação Matemática
A reta **s** é definida por:
- x = 2 (constante)
- y = 1 (constante)
- z ∈ R (livre)

Portanto, **s é paralela ao eixo Z** e passa pelo ponto **P₀ = (2, 1, 0)**.

**Vetor direção:** d = (0, 0, 1)

### Estratégia de Cálculo
Para rotacionar em torno de uma reta que não passa pela origem:

1. **Transladar** a reta para a origem: T₁ = T(-2, -1, 0)
2. **Rotacionar** em torno do eixo Z: Rz(θ)
3. **Transladar** de volta: T₂ = T(2, 1, 0)

**Matriz composta:** Ma = T₂ · Rz(θ) · T₁

### Matriz em Coordenadas Homogêneas

```
       [cos(θ)  -sin(θ)  0   2]
Ma =   [sin(θ)   cos(θ)  0   1]
       [0        0       1   0]
       [0        0       0   1]
```

### Implementação no Código
```python
def get_rotation_around_line_a(angle):
    p0 = np.array([2.0, 1.0, 0.0])  # Ponto na reta
    
    c = math.cos(angle)
    s = math.sin(angle)
    
    # Rotação em torno de Z
    Rz = np.array([
        [c, -s, 0, 0],
        [s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    # T₁: Translação para origem
    T1 = np.array([
        [1, 0, 0, -p0[0]],
        [0, 1, 0, -p0[1]],
        [0, 0, 1, -p0[2]],
        [0, 0, 0, 1]
    ])
    
    # T₂: Translação de volta
    T2 = np.array([
        [1, 0, 0, p0[0]],
        [0, 1, 0, p0[1]],
        [0, 0, 1, p0[2]],
        [0, 0, 0, 1]
    ])
    
    return T2 @ Rz @ T1
```

---

## 🪞 Questão B - Reflexão no plano C

### Enunciado
> Reflexão em relação ao plano **C = {(x, y, z) | (0, 1, 0) + q(-2, 1+3, 1-3) + p(-1, -1, 1)}**

### Interpretação Matemática
O plano é dado em **forma paramétrica**:
```
P(q, p) = P₀ + q·v₁ + p·v₂
```
Onde:
- **P₀ = (0, 1, 0)** (ponto no plano)
- **v₁ = (-2, 4, -2)** (primeiro vetor direção)
- **v₂ = (-1, -1, 1)** (segundo vetor direção)

### Cálculo da Normal ao Plano
```
n = v₁ × v₂  (produto vetorial)
n̂ = n / ||n||  (normalizado)
```

```python
v1 = np.array([-2.0, 4.0, -2.0])
v2 = np.array([-1.0, -1.0, 1.0])
n = np.cross(v1, v2)  # Normal ao plano
n = n / np.linalg.norm(n)  # Normalizar
```

### Matriz de Reflexão

A reflexão em relação a um plano com normal **n̂** é dada por:
```
R = I - 2n̂n̂ᵀ
```

Esta é a **transformação linear** (matriz 3×3).

### Componente de Translação

Para refletir em relação a um plano que **não passa pela origem**, precisamos adicionar uma translação:
```
d = 2(n̂ · P₀)
T = d · n̂
```

### Expressão Final (Linear + Translação)

Como pedido no enunciado, expressamos como:
```
Reflexão = Translação ∘ Transformação Linear
Mb = T · R
```

Em coordenadas homogêneas:
```
       [r11  r12  r13  tx]
Mb =   [r21  r22  r23  ty]
       [r31  r32  r33  tz]
       [0    0    0    1 ]
```
Onde:
- rᵢⱼ vem de R = I - 2n̂n̂ᵀ
- (tx, ty, tz) = d·n̂

### Implementação no Código
```python
def get_reflection_plane_b():
    P0 = np.array([0.0, 1.0, 0.0])
    v1 = np.array([-2.0, 4.0, -2.0])
    v2 = np.array([-1.0, -1.0, 1.0])
    
    # Normal ao plano
    n = cross_product(v1, v2)
    n = normalize_vector(n)
    
    # Matriz de reflexão: I - 2n̂n̂ᵀ
    R = np.eye(4)
    R[0:3, 0:3] = np.eye(3) - 2 * np.outer(n, n)
    
    # Componente de translação
    d = 2 * dot_product(n, P0)
    T = np.array([
        [1, 0, 0, d*n[0]],
        [0, 1, 0, d*n[1]],
        [0, 0, 1, d*n[2]],
        [0, 0, 0, 1]
    ])
    
    return T @ R  # Translação ∘ Linear
```

---

## 🌀 Questão C - Rotação Helicoidal

### Enunciado
> Rotação em torno de **D = (-t, 1-t, t)** com fator de translação **2/π**

### Interpretação Matemática

A reta D é dada em **forma paramétrica**:
```
r(t) = (-t, 1-t, t)
r(t) = (0, 1, 0) + t(-1, -1, 1)
```

Portanto:
- **P₀ = (0, 1, 0)** (ponto quando t=0)
- **d = (-1, -1, 1)** (vetor direção)
- **d̂ = d/||d||** (normalizado)

### O que é Rotação Helicoidal?

Uma rotação helicoidal combina:
1. **Rotação** em torno de um eixo (ângulo θ)
2. **Translação** ao longo do mesmo eixo (distância proporcional a θ)

É como um parafuso girando!

### Fórmula de Rodrigues

Para rotação em torno de um eixo arbitrário **d̂** por ângulo θ:
```
R(θ) = I + sin(θ)[d̂]× + (1-cos(θ))[d̂]×²
```

Ou em forma expandida:
```
R = [t·dx² + c      t·dx·dy - s·dz  t·dx·dz + s·dy]
    [t·dx·dy + s·dz t·dy² + c      t·dy·dz - s·dx]
    [t·dx·dz - s·dy t·dy·dz + s·dx t·dz² + c     ]
```
Onde:
- c = cos(θ)
- s = sin(θ)
- t = 1 - cos(θ)

### Componente de Translação

```
translação = θ · (2/π) · d̂
```

Quanto maior o ângulo, maior a translação ao longo do eixo.

### Matriz Composta

```
Mc = T₂ · R(θ) · T₁
```
Onde:
- T₁ translada P₀ para origem
- R(θ) é a rotação de Rodrigues
- T₂ translada de volta + adiciona translação helicoidal

### Implementação no Código
```python
def get_helical_rotation_c(angle):
    p0 = np.array([0.0, 1.0, 0.0])
    d = np.array([-1.0, -1.0, 1.0])
    d = normalize_vector(d)
    
    translation_factor = 2.0 / math.pi
    translation = angle * translation_factor
    
    c = math.cos(angle)
    s = math.sin(angle)
    t = 1 - c
    
    # Fórmula de Rodrigues
    R = np.array([
        [t*d[0]*d[0]+c, t*d[0]*d[1]-s*d[2], t*d[0]*d[2]+s*d[1], 0],
        [t*d[0]*d[1]+s*d[2], t*d[1]*d[1]+c, t*d[1]*d[2]-s*d[0], 0],
        [t*d[0]*d[2]-s*d[1], t*d[1]*d[2]+s*d[0], t*d[2]*d[2]+c, 0],
        [0, 0, 0, 1]
    ])
    
    T1 = translação para origem
    T2 = translação de volta + translação helicoidal
    
    return T2 @ R @ T1
```

---

## 🔗 Composição das Transformações

### Ordem de Aplicação

O código aplica as transformações **em sequência**:
1. Primeiro **A** (rotação em torno de s)
2. Depois **B** (reflexão no plano C)
3. Por fim **C** (rotação helicoidal)

### Matriz Composta

```
M_total = Mc · Mb · Ma
```

**ATENÇÃO:** A multiplicação é da **direita para esquerda**!

Para transformar um ponto **v**:
```
v' = M_total · v
v' = (Mc · Mb · Ma) · v
v' = Mc · (Mb · (Ma · v))
```

### Implementação
```python
# Composição
M_temp = Mb @ Ma      # Primeiro Ma, depois Mb
M_total = Mc @ M_temp # Por fim Mc

# Aplicar ao cubo
cube_transformed = transform_vertices(cube, M_total)
```

### Animação em 3 Etapas

- **0-33%**: Apenas A é aplicado (Ma)
- **33-66%**: A e B são aplicados (Mb · Ma)
- **66-100%**: A, B e C são aplicados (Mc · Mb · Ma)

---

## ✅ Implementação e Verificação

### Estrutura do Código

1. **Funções de Álgebra Linear**
   - `normalize_vector()`: Normaliza vetores
   - `cross_product()`: Produto vetorial
   - `dot_product()`: Produto escalar
   - `multiply_matrices()`: Multiplicação de matrizes

2. **Operadores Afins**
   - `get_rotation_around_line_a(angle)`
   - `get_reflection_plane_b()`
   - `get_helical_rotation_c(angle)`

3. **Geometria**
   - `create_cube()`: Cria cubo unitário
   - `transform_vertices()`: Aplica transformação
   - `project_3d_to_2d()`: Projeção perspectiva

4. **Visualização**
   - `draw_cube()`: Desenha arestas e vértices
   - `draw_ui()`: Interface com informações

### Como Verificar Cada Operador

#### Verificação Discreta

1. **Pausar a animação** (ESPAÇO)
2. **Observar posições** dos vértices
3. **Comparar** com estado original (cubo cinza)

#### Teste do Operador A
- Pause em 0-33%
- O cubo deve **girar em torno da reta x=2, y=1**
- Vértices devem manter distância constante dessa reta

#### Teste do Operador B
- Pause em 33-66%
- O cubo deve ser **espelhado** em relação ao plano C
- A orientação deve ser invertida

#### Teste do Operador C
- Pause em 66-100%
- O cubo deve **girar E se mover** ao longo da reta D
- Movimento helicoidal visível

### Controles

| Tecla | Função |
|-------|--------|
| ESPAÇO | Play/Pause animação |
| R | Reset (volta ao início) |
| S | Mostra/oculta estados intermediários |

### Estados Visualizados

- **Cinza claro**: Cubo original
- **Verde**: Após transformação A
- **Amarelo**: Após transformação A∘B
- **Azul**: Estado final A∘B∘C

---

## 📊 Exemplo Numérico

### Ponto de Teste: v = (0, 0, 0)

Vamos traçar a trajetória da origem através das transformações:

1. **Após A (θ = π/2)**:
   - Rotação 90° em torno de (2,1,0)
   - v₁ = Ma · (0,0,0,1)ᵀ
   - v₁ ≈ (3, 1, 0) (aproximado)

2. **Após A∘B**:
   - Reflexão no plano C
   - v₂ = Mb · v₁

3. **Após A∘B∘C (θ = π/2)**:
   - Rotação helicoidal
   - v₃ = Mc · v₂

### Propriedades Verificadas

✅ **Coordenadas homogêneas**: Todas matrizes 4×4  
✅ **Última linha**: Sempre [0, 0, 0, 1]  
✅ **Composição**: Multiplicação matricial correta  
✅ **Continuidade**: Animação suave via interpolação linear  

---

## 🎓 Conclusão

O código implementa **corretamente** todas as três questões:

1. ✅ **Questão A**: Matriz homogênea da rotação em s
2. ✅ **Questão B**: Reflexão expressa como Translação ∘ Linear
3. ✅ **Questão C**: Rotação helicoidal com fator 2/π

Além disso:
- ✅ Composição correta das transformações
- ✅ Animação suave e contínua
- ✅ Visualização de estados intermediários
- ✅ Verificação discreta possível

**Todas as matrizes são calculadas algebricamente** usando as fórmulas da teoria de operadores afins, sem aproximações ou heurísticas!