float raio_circulo_maior = 100;  // raio do círculo maior
float raio_circulo_menor = 25;   // raio do círculo menor
float raio_bolinha = raio_circulo_maior - raio_circulo_menor; // raio da trajetória do centro do círculo menor

float duracao = 4.0;  // duração em segundos
float fps = 60.0;
float totalFrames = duracao * fps;
float omegaCentro = TWO_PI / totalFrames;  // velocidade angular do centro

float angCentro = 0;   // ângulo do centro da bolinha
float angBola = 0;     // ângulo de rotação da bolinha

void setup() {
  size(600, 600);
  frameRate(60);
}

void draw() {
  background(240);
  translate(width/2, height/2); // origem no centro da tela

  // Atualiza ângulos
  angCentro += omegaCentro;
  angBola -= (raio_bolinha/raio_circulo_menor) * omegaCentro; // rotação da bolinha sem deslizar

  // Posição do centro da bolinha
  float cx = raio_bolinha * cos(angCentro);
  float cy = raio_bolinha * sin(angCentro);

  // Desenha círculo maior
  noFill();
  stroke(0);
  strokeWeight(2);
  ellipse(0, 0, raio_circulo_maior*2, raio_circulo_maior*2);

  // Desenha bolinha rolando
  pushMatrix();
  translate(cx, cy);
  rotate(angBola);
  fill(100, 150, 255);
  ellipse(0, 0, raio_circulo_menor*2, raio_circulo_menor*2);

  // Marca um ponto na bolinha
  fill(255, 0, 0);
  ellipse(raio_circulo_menor-5, 0, 10, 10);
  popMatrix();
}
