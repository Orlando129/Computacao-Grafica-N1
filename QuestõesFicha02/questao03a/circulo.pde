float R = 100;  // raio do círculo maior
float r = 25;   // raio do círculo menor
float Rc = R - r; // raio da trajetória do centro do círculo menor

float duracao = 4.0;  // segundos
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
  angBola -= (Rc/r) * omegaCentro; // rotação da bolinha sem deslizar

  // Posição do centro da bolinha
  float cx = Rc * cos(angCentro);
  float cy = Rc * sin(angCentro);

  // Desenha círculo maior
  noFill();
  stroke(0);
  strokeWeight(2);
  ellipse(0, 0, R*2, R*2);

  // Desenha bolinha rolando
  pushMatrix();
  translate(cx, cy);
  rotate(angBola);
  fill(100, 150, 255);
  ellipse(0, 0, r*2, r*2);

  // Marca um ponto na bolinha
  fill(255, 0, 0);
  ellipse(r-5, 0, 10, 10);
  popMatrix();
}
