float raio = 30;
float x, y;
float vx, vy;
float g = 0.5;

// Configurações iniciais
void setup() {
  size(800, 600);
  x = raio;                 // canto inferior esquerdo
  y = height - raio;
  
  vx = 3.3;                 // velocidade horizontal (aprox. 4s ida/volta)
  vy = -15;                 // velocidade vertical inicial
}

void draw() {
  background(20);

  // Atualiza movimento
  vy += g;   // aplica gravidade
  x += vx;
  y += vy;

  // Colisão paredes (esquerda/direita)
  if (x + raio > width || x - raio < 0) {
    vx *= -1;
  }

  // Colisão chão
  if (y + raio > height) {
    y = height - raio;
    vy *= -1;
  }

  // Colisão teto
  if (y - raio < 0) {
    y = raio;
    vy *= -1;
  }

  // Desenhar bola
  fill(155, 190, 230);
  noStroke();
  ellipse(x, y, raio*2, raio*2);
}
