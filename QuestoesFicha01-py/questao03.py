import numpy as np
import pygame
import math
import sys

# Configurações
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
T_PERIOD = 4.0  # Período t em segundos

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

class PiaoAnimator:
    def __init__(self):
        # Posição inicial do pião
        self.piao_inicial = np.array([1.0, 2.0, 0.0, 1.0])  # Coordenadas homogêneas
        
        # Escala para visualização
        self.scale = 150  # Aumentado para melhor visualização
        self.offset_x = WINDOW_WIDTH // 2
        self.offset_y = WINDOW_HEIGHT // 2
        
    def matriz_translacao(self, tx, ty, tz):
        """Matriz de translação 4x4"""
        return np.array([
            [1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1]
        ])
    
    def matriz_rotacao_z(self, angulo):
        """Matriz de rotação em torno do eixo Z"""
        c = math.cos(angulo)
        s = math.sin(angulo)
        return np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    
    def matriz_rotacao_eixo_arbitrario(self, ponto, direcao, angulo):
        """
        Matriz de rotação em torno de um eixo arbitrário
        ponto: ponto do eixo
        direcao: vetor direção do eixo (normalizado)
        angulo: ângulo de rotação
        """
        # Normalizar direção
        u = direcao / np.linalg.norm(direcao)
        ux, uy, uz = u
        
        c = math.cos(angulo)
        s = math.sin(angulo)
        
        # Matriz de rotação de Rodrigues
        R = np.array([
            [c + ux*ux*(1-c), ux*uy*(1-c) - uz*s, ux*uz*(1-c) + uy*s, 0],
            [uy*ux*(1-c) + uz*s, c + uy*uy*(1-c), uy*uz*(1-c) - ux*s, 0],
            [uz*ux*(1-c) - uy*s, uz*uy*(1-c) + ux*s, c + uz*uz*(1-c), 0],
            [0, 0, 0, 1]
        ])
        
        # Translação para origem, rotação, translação de volta
        T1 = self.matriz_translacao(-ponto[0], -ponto[1], -ponto[2])
        T2 = self.matriz_translacao(ponto[0], ponto[1], ponto[2])
        
        return T2 @ R @ T1
    
    def calcular_transformacao(self, tempo):
        """
        Calcula a matriz de transformação composta no tempo t
        """
        # Ângulos baseados no tempo
        # Pião gira 4 voltas em t segundos: 4 * 2π * (tempo/T_PERIOD)
        angulo_piao = 4 * 2 * math.pi * (tempo / T_PERIOD)
        
        # Eixo r gira 1 volta em t segundos: 2π * (tempo/T_PERIOD)
        angulo_eixo_r = 2 * math.pi * (tempo / T_PERIOD)
        
        # TRANSFORMAÇÃO 1: Rotação do pião em torno do eixo r
        # Eixo r: x = 1 + q, y = 2 - q, z = 0
        # Ponto do eixo r: (1, 2, 0)
        # Direção do eixo r: (1, -1, 0) normalizado
        ponto_r = np.array([1, 2, 0])
        direcao_r = np.array([1, -1, 0])
        direcao_r = direcao_r / np.linalg.norm(direcao_r)
        
        M1 = self.matriz_rotacao_eixo_arbitrario(ponto_r, direcao_r, angulo_piao)
        
        # TRANSFORMAÇÃO 2: Rotação do eixo r em torno do eixo s
        # Eixo s: x = 2, y = 1, z livre (direção z)
        # Ponto do eixo s: (2, 1, 0)
        # Direção do eixo s: (0, 0, 1)
        ponto_s = np.array([2, 1, 0])
        direcao_s = np.array([0, 0, 1])
        
        M2 = self.matriz_rotacao_eixo_arbitrario(ponto_s, direcao_s, angulo_eixo_r)
        
        # Transformação composta: primeiro M1, depois M2
        M_total = M2 @ M1
        
        return M_total, M1, M2
    
    def projetar_3d_para_2d(self, ponto_3d):
        """Projeta ponto 3D para 2D (projeção ortográfica)"""
        # Ajustando offsets para centralizar o pião na tela
        # Subtrai a posição média do movimento (aproximadamente 1.5, 1.5) multiplicada pela escala
        x = int((ponto_3d[0] - 1.5) * self.scale + self.offset_x)
        y = int(-(ponto_3d[1] - 1.5) * self.scale + self.offset_y)  # Inverter Y
        return (x, y)
    
    def desenhar_eixos(self, screen, M2):
        """Desenha os eixos r e s"""
        # Eixo s (fixo): x = 2, y = 1
        p1_s = np.array([2, 1, -2, 1])
        p2_s = np.array([2, 1, 2, 1])
        
        pos1_s = self.projetar_3d_para_2d(p1_s)
        pos2_s = self.projetar_3d_para_2d(p2_s)
        pygame.draw.line(screen, BLUE, pos1_s, pos2_s, 5)  # Eixo s mais grosso
        
        # Eixo r (rotacionado): aplicar M2 aos pontos do eixo r
        # Pontos do eixo r original
        p1_r = np.array([0, 3, 0, 1])  # q = -1
        p2_r = np.array([2, 1, 0, 1])  # q = 1
        
        # Aplicar rotação M2
        p1_r_rot = M2 @ p1_r
        p2_r_rot = M2 @ p2_r
        
        pos1_r = self.projetar_3d_para_2d(p1_r_rot)
        pos2_r = self.projetar_3d_para_2d(p2_r_rot)
        pygame.draw.line(screen, GREEN, pos1_r, pos2_r, 5)  # Eixo r mais grosso
    
    def desenhar_piao(self, screen, posicao):
        """Desenha o pião como um formato mais realista e visível"""
        pos_2d = self.projetar_3d_para_2d(posicao)
        
        # Corpo principal do pião (círculo maior)
        pygame.draw.circle(screen, RED, pos_2d, 20)
        pygame.draw.circle(screen, (200, 0, 0), pos_2d, 20, 3)  # Borda
        
        # Círculo interno menor
        pygame.draw.circle(screen, (255, 100, 100), pos_2d, 12)
        
        # Ponto central
        pygame.draw.circle(screen, WHITE, pos_2d, 3)
        
        # Linhas indicando orientação e rotação
        orientacao1 = np.array([posicao[0] + 0.15, posicao[1], posicao[2], 1])
        orientacao2 = np.array([posicao[0], posicao[1] + 0.15, posicao[2], 1])
        or1_2d = self.projetar_3d_para_2d(orientacao1)
        or2_2d = self.projetar_3d_para_2d(orientacao2)
        
        pygame.draw.line(screen, YELLOW, pos_2d, or1_2d, 3)
        pygame.draw.line(screen, CYAN, pos_2d, or2_2d, 3)
    
    def imprimir_matrizes(self, tempo, M_total, M1, M2):
        """Imprime as matrizes de transformação"""
        print(f"\n=== TEMPO: {tempo:.2f}s ===")
        print("\nMatriz M1 (Rotação do pião em torno do eixo r):")
        print(M1)
        print("\nMatriz M2 (Rotação do eixo r em torno do eixo s):")
        print(M2)
        print("\nMatriz Total M = M2 * M1:")
        print(M_total)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Animação do Pião - Questão 3")
    clock = pygame.time.Clock()
    
    animator = PiaoAnimator()
    
    tempo = 0.0
    rodando = True
    mostrar_matrizes = True
    
    print("=== SIMULAÇÃO DO PIÃO ===")
    print("Pressione ESC para sair")
    print("Pressione ESPAÇO para mostrar/ocultar matrizes no console")
    
    while rodando:
        dt = clock.tick(FPS) / 1000.0  # Delta time em segundos
        tempo += dt
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False
                elif event.key == pygame.K_SPACE:
                    mostrar_matrizes = not mostrar_matrizes
                    print(f"Exibição de matrizes: {'ON' if mostrar_matrizes else 'OFF'}")
        
        # Calcular transformações
        M_total, M1, M2 = animator.calcular_transformacao(tempo)
        
        # Aplicar transformação ao pião
        posicao_piao = M_total @ animator.piao_inicial
        
        # Imprimir matrizes periodicamente
        if mostrar_matrizes and int(tempo * 4) % 4 == 0 and tempo > 0:
            animator.imprimir_matrizes(tempo, M_total, M1, M2)
        
        # Desenhar
        screen.fill(BLACK)
        
        # Desenhar eixos
        animator.desenhar_eixos(screen, M2)
        
        # Desenhar pião
        animator.desenhar_piao(screen, posicao_piao)
        
        # Informações na tela
        font = pygame.font.Font(None, 36)
        texto_tempo = font.render(f"Tempo: {tempo:.2f}s", True, WHITE)
        screen.blit(texto_tempo, (10, 10))
        
        texto_pos = font.render(f"Pião: ({posicao_piao[0]:.2f}, {posicao_piao[1]:.2f}, {posicao_piao[2]:.2f})", True, WHITE)
        screen.blit(texto_pos, (10, 50))
        
        # Legenda
        legenda = [
            "Azul: Eixo s (x=2, y=1)",
            "Verde: Eixo r (rotaciona)",
            "Vermelho: Pião",
            "Amarelo/Ciano: Orientação do pião",
            "ESC: Sair | ESPAÇO: Matrizes"
        ]
        for i, linha in enumerate(legenda):
            texto = pygame.font.Font(None, 24).render(linha, True, WHITE)
            screen.blit(texto, (10, WINDOW_HEIGHT - 100 + i * 25))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
