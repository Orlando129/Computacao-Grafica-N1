import pygame
import numpy as np
import math

# Inicialização
pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Operadores Afins 3D - Composição A∘B∘C")
clock = pygame.time.Clock()

# Cores
BLACK = (15, 23, 42)
WHITE = (226, 232, 240)
BLUE = (59, 130, 246)
LIGHT_BLUE = (96, 165, 250)
GRAY = (100, 116, 139)
GREEN = (34, 197, 94)
YELLOW = (234, 179, 8)
SLATE_BG = (30, 41, 59)

# Funções de álgebra linear
def normalize_vector(v):
    """Normaliza um vetor 3D"""
    mag = np.linalg.norm(v)
    return v / mag if mag > 0 else v

def cross_product(a, b):
    """Produto vetorial"""
    return np.cross(a, b)

def dot_product(a, b):
    """Produto escalar"""
    return np.dot(a, b)

def multiply_matrices(a, b):
    """Multiplica duas matrizes 4x4"""
    return np.dot(a, b)

def compose_matrices(matrices):
    """Compõe múltiplas matrizes"""
    result = matrices[0]
    for matrix in matrices[1:]:
        result = multiply_matrices(result, matrix)
    return result

# QUESTÃO A: Rotação em torno da reta s = {(x,y,z) | x=2 e y=1}
def get_rotation_around_line_a(angle):
    """
    Rotação em torno da reta paralela ao eixo Z passando por (2, 1, 0)
    Matriz em coordenadas homogêneas: T(2,1,0) · Rz(θ) · T(-2,-1,0)
    """
    p0 = np.array([2.0, 1.0, 0.0])  # Ponto na reta
    
    c = math.cos(angle)
    s = math.sin(angle)
    
    # Matriz de rotação em torno de Z
    Rz = np.array([
        [c, -s, 0, 0],
        [s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    # Translação para origem
    T1 = np.array([
        [1, 0, 0, -p0[0]],
        [0, 1, 0, -p0[1]],
        [0, 0, 1, -p0[2]],
        [0, 0, 0, 1]
    ])
    
    # Translação de volta
    T2 = np.array([
        [1, 0, 0, p0[0]],
        [0, 1, 0, p0[1]],
        [0, 0, 1, p0[2]],
        [0, 0, 0, 1]
    ])
    
    return compose_matrices([T2, Rz, T1])

# QUESTÃO B: Reflexão em relação ao plano C
def get_reflection_plane_b():
    """
    Reflexão no plano C = {(x,y,z) | (0,1,0) + q(-2, 1+3, 1-3) + p(-1, -1, 1)}
    onde P0 = (0,1,0), v1 = (-2, 4, -2), v2 = (-1, -1, 1)
    Expressão: Transformação Linear seguida de Translação
    """
    P0 = np.array([0.0, 1.0, 0.0])
    v1 = np.array([-2.0, 4.0, -2.0])  # (-2, 1+3, 1-3)
    v2 = np.array([-1.0, -1.0, 1.0])
    
    # Normal ao plano (produto vetorial v1 x v2)
    n = cross_product(v1, v2)
    n = normalize_vector(n)
    
    # TRANSFORMAÇÃO LINEAR: Matriz de reflexão R = I - 2*n*n^T
    R = np.eye(4)
    R[0:3, 0:3] = np.eye(3) - 2 * np.outer(n, n)
    
    # TRANSLAÇÃO: Para refletir em relação ao plano que não passa pela origem
    # A fórmula é: T(2*d*n) onde d = distância da origem ao plano
    d = dot_product(n, P0)  # distância da origem ao plano
    T = np.array([
        [1, 0, 0, 2*d*n[0]],
        [0, 1, 0, 2*d*n[1]],
        [0, 0, 1, 2*d*n[2]],
        [0, 0, 0, 1]
    ])
    
    # COMPOSIÇÃO: Transformação Linear seguida de Translação = T · R
    return multiply_matrices(T, R)

# QUESTÃO C: Rotação helicoidal em torno de D = (-t, 1-t, t)
def get_helical_rotation_c(angle):
    """
    Rotação helicoidal em torno da reta D = (-t, 1-t, t)
    Linha paramétrica: (0, 1, 0) + t(-1, -1, 1)
    com fator de translação 2/π
    """
    # Reta D: ponto P0 = (0, 1, 0), direção d = (-1, -1, 1)
    P0 = np.array([0.0, 1.0, 0.0])  # Quando t=0
    d = np.array([-1.0, -1.0, 1.0])  # Direção da reta
    d = normalize_vector(d)
    
    # Fator de translação ao longo do eixo
    translation_factor = 2.0 / math.pi
    translation = angle * translation_factor
    
    # Parâmetros para rotação de Rodrigues
    c = math.cos(angle)
    s = math.sin(angle)
    t = 1 - c
    
    # Matriz de rotação em torno do eixo d (Rodrigues)
    R = np.array([
        [t*d[0]*d[0]+c, t*d[0]*d[1]-s*d[2], t*d[0]*d[2]+s*d[1], 0],
        [t*d[0]*d[1]+s*d[2], t*d[1]*d[1]+c, t*d[1]*d[2]-s*d[0], 0],
        [t*d[0]*d[2]-s*d[1], t*d[1]*d[2]+s*d[0], t*d[2]*d[2]+c, 0],
        [0, 0, 0, 1]
    ])
    
    # Translação para origem
    T1 = np.array([
        [1, 0, 0, -P0[0]],
        [0, 1, 0, -P0[1]],
        [0, 0, 1, -P0[2]],
        [0, 0, 0, 1]
    ])
    
    # Translação de volta + translação helicoidal
    T2 = np.array([
        [1, 0, 0, P0[0] + translation*d[0]],
        [0, 1, 0, P0[1] + translation*d[1]],
        [0, 0, 1, P0[2] + translation*d[2]],
        [0, 0, 0, 1]
    ])
    
    # COMPOSIÇÃO: T2 · R · T1
    return compose_matrices([T2, R, T1])

def print_matrices_info():
    """Imprime informações sobre as matrizes dos operadores"""
    print("=== MATRIZES DOS OPERADORES AFINS ===\n")
    
    # Operador A - Rotação 90° em torno de s
    Ma = get_rotation_around_line_a(math.pi/2)
    print("A) Rotação 90° em torno de s = {(x,y,z) | x=2, y=1}")
    print("Matriz homogênea 4x4:")
    print(Ma)
    print()
    
    # Operador B - Reflexão no plano C
    Mb = get_reflection_plane_b()
    print("B) Reflexão no plano C = {(x,y,z) | (0,1,0) + q(-2,4,-2) + p(-1,-1,1)}")
    print("Transformação Linear seguida de Translação:")
    print(Mb)
    print()
    
    # Operador C - Rotação helicoidal 90°
    Mc = get_helical_rotation_c(math.pi/2)
    print("C) Rotação helicoidal 90° em torno de D = (-t, 1-t, t)")
    print("Fator de translação: 2/π")
    print("Matriz homogênea 4x4:")
    print(Mc)
    print()
    
    # Composição C∘B∘A
    M_total = multiply_matrices(Mc, multiply_matrices(Mb, Ma))
    print("Composição C∘B∘A:")
    print(M_total)
    print("\n" + "="*50 + "\n")

def interpolate_matrix(M1, M2, t):
    """Interpola linearmente entre duas matrizes"""
    return M1 * (1 - t) + M2 * t

# Criar cubo (lado 1)
def create_cube():
    """Cria vértices de um cubo unitário"""
    s = 0.5
    vertices = np.array([
        [-s, -s, -s], [s, -s, -s], [s, s, -s], [-s, s, -s],  # Face traseira
        [-s, -s, s], [s, -s, s], [s, s, s], [-s, s, s]       # Face frontal
    ])
    return vertices

# Arestas do cubo
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Traseira
    (4, 5), (5, 6), (6, 7), (7, 4),  # Frontal
    (0, 4), (1, 5), (2, 6), (3, 7)   # Conexões
]

def transform_vertices(vertices, matrix):
    """Aplica transformação a todos os vértices"""
    homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    transformed = homogeneous @ matrix.T
    return transformed[:, :3]

def project_3d_to_2d(point, scale=70, distance=5):
    """Projeção perspectiva simples"""
    factor = distance / (distance + point[2])
    x = WIDTH // 2 + point[0] * scale * factor
    y = HEIGHT // 2 - point[1] * scale * factor
    return int(x), int(y)

def draw_cube(surface, vertices, color, width=2):
    """Desenha o cubo na tela"""
    for edge in cube_edges:
        p1 = project_3d_to_2d(vertices[edge[0]])
        p2 = project_3d_to_2d(vertices[edge[1]])
        pygame.draw.line(surface, color, p1, p2, width)
    
    # Desenhar vértices
    for vertex in vertices:
        p = project_3d_to_2d(vertex)
        pygame.draw.circle(surface, color, p, 4)

def draw_text(surface, text, pos, font_size=20, color=WHITE):
    """Desenha texto na tela"""
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

def draw_ui(surface, progress, current_step, show_steps):
    """Desenha interface do usuário"""
    # Fundo para UI
    pygame.draw.rect(surface, SLATE_BG, (10, 10, 450, 150), border_radius=10)
    
    draw_text(surface, "Composicao: C o B o A", (20, 20), 24, WHITE)
    draw_text(surface, current_step, (20, 50), 20, LIGHT_BLUE)
    draw_text(surface, f"Progresso: {progress*100:.1f}%", (20, 80), 18, WHITE)
    
    draw_text(surface, "Controles:", (20, 110), 18, WHITE)
    draw_text(surface, "ESPACO: Play/Pause | R: Reset | S: Etapas | M: Matrizes", (20, 130), 16, GRAY)
    
    # Legenda
    y_start = HEIGHT - 120
    pygame.draw.rect(surface, SLATE_BG, (10, y_start, 200, 110), border_radius=10)
    
    draw_text(surface, "Legenda:", (20, y_start + 10), 18, WHITE)
    pygame.draw.line(surface, (*GRAY, 80), (20, y_start + 35), (50, y_start + 35), 2)
    draw_text(surface, "Original", (60, y_start + 28), 16, GRAY)
    
    if show_steps:
        pygame.draw.line(surface, (*GREEN, 120), (20, y_start + 55), (50, y_start + 55), 2)
        draw_text(surface, "Apos A", (60, y_start + 48), 16, GREEN)
        
        pygame.draw.line(surface, (*YELLOW, 120), (20, y_start + 75), (50, y_start + 75), 2)
        draw_text(surface, "Apos A o B", (60, y_start + 68), 16, YELLOW)
    
    pygame.draw.line(surface, BLUE, (20, y_start + 95), (50, y_start + 95), 3)
    draw_text(surface, "Final", (60, y_start + 88), 16, BLUE)

# Loop principal
def main():
    print("=== QUESTÃO 1 - OPERADORES AFINS ===")
    print("Pressione 'M' durante a execução para ver as matrizes")
    print("Iniciando com as matrizes dos operadores...\n")
    
    # Imprimir matrizes na inicialização
    print_matrices_info()
    
    running = True
    animating = False
    show_steps = True
    progress = 0.0
    
    cube = create_cube()
    I = np.eye(4)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    animating = not animating
                elif event.key == pygame.K_r:
                    progress = 0.0
                    animating = False
                elif event.key == pygame.K_s:
                    show_steps = not show_steps
                elif event.key == pygame.K_m:
                    print_matrices_info()
        
        # Atualizar progresso
        if animating:
            progress += 0.003
            if progress >= 1.0:
                progress = 0.0
        
        # Determinar etapa atual e calcular matrizes
        if progress < 0.33:
            # Etapa A: Rotação
            t = progress / 0.33
            angle = t * 2 * math.pi
            Ma = get_rotation_around_line_a(angle)
            Mb = I
            Mc = I
            current_step = "A: Rotacao em torno de s (x=2, y=1)"
        elif progress < 0.66:
            # Etapa B: Reflexão
            t = (progress - 0.33) / 0.33
            Ma = get_rotation_around_line_a(2 * math.pi)
            Mb_full = get_reflection_plane_b()
            Mb = interpolate_matrix(I, Mb_full, t)
            Mc = I
            current_step = "B: Reflexao no plano C"
        else:
            # Etapa C: Rotação helicoidal
            t = (progress - 0.66) / 0.34
            angle = t * 2 * math.pi
            Ma = get_rotation_around_line_a(2 * math.pi)
            Mb = get_reflection_plane_b()
            Mc = get_helical_rotation_c(angle)
            current_step = "C: Rotacao helicoidal em D"
        
        # COMPOSIÇÃO: M_total = Mc · Mb · Ma
        M_temp = multiply_matrices(Mb, Ma)
        M_total = multiply_matrices(Mc, M_temp)
        
        # Transformar cubo
        cube_transformed = transform_vertices(cube, M_total)
        
        # Estados intermediários
        cube_after_a = transform_vertices(cube, Ma)
        cube_after_ab = transform_vertices(cube, multiply_matrices(Mb, Ma))
        
        # Renderizar
        screen.fill(BLACK)
        
        # Desenhar cubo original
        draw_cube(screen, cube, (*GRAY, 80), 1)
        
        # Desenhar estados intermediários
        if show_steps:
            if progress >= 0.33:
                draw_cube(screen, cube_after_a, (*GREEN, 120), 2)
            if progress >= 0.66:
                draw_cube(screen, cube_after_ab, (*YELLOW, 120), 2)
        
        # Desenhar cubo final
        draw_cube(screen, cube_transformed, BLUE, 3)
        
        # Desenhar UI
        draw_ui(screen, progress, current_step, show_steps)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()