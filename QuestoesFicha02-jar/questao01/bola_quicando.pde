float raio = 30; //Tamanho da bola
float x, y; //Coordenadas da posição atual da bola
float vx, vy; //Velocidade da bola eixo x e y
float g = 0.5; //Aceleração da gravidade

// Configurações iniciais
void setup() {
  size(800, 600); //Tamanho da tela
  x = raio;                 // canto inferior esquerdo
  y = height - raio; //posicionando a bola no canto inferior esquerdo, sem atravessar as bordas.
  
  vx = 3.3;                 // velocidade horizontal (aprox. 4s ida/volta) positivo -> direita
  vy = -15;                 // velocidade vertical inicial negativo -> sobe
}

void draw() {
  background(20);

  // Atualiza movimento
  vy += g;   // aplica gravidade
  x += vx;
  y += vy;

  // Colisão paredes (esquerda/direita)
  if (x + raio > width || x - raio < 0) {
    vx *= -1; //inverte a posição
  }

  // Colisão chão
  if (y + raio > height) {
    y = height - raio;
    vy *= -1;
  }

  // Desenhar bola
  fill(155, 190, 230);
  noStroke();
  ellipse(x, y, raio*2, raio*2); // construindo esfera e dizendo que o diametro é o raio*2
}
