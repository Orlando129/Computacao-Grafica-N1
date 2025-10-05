float L1 = 100;  // comprimento do braço (escala, 2 -> 100 px)
float L2 = 150;  // comprimento do antebraço (3 -> 150 px)

float x0 = 400, y0 = 400;  // ombro (fixo no meio da tela)

// ângulos iniciais
float theta1 = PI/2;   // braço começa na vertical (90 graus)
float theta2 = 0;      // antebraço alinhado com o braço

// velocidades
float duracao = 2.0;    // em segundos
float fps = 60.0;
float totalFrames = duracao * fps;

float omega1 = (PI/2) / totalFrames;  // ajusta movimento para terminar em 2s
float omega2 = 2 * omega1;            // antebraço gira 2x mais rápido

void setup() {
  size(800, 600);
  frameRate(60);
}

void draw() {
  background(220);
  
  // atualizar ângulos
  if (frameCount <= totalFrames) {
    theta1 -= omega1;  // braço rotaciona
    theta2 -= omega2;  // antebraço rotaciona mais rápido
  }
  
  // calcular posições
  float x1 = x0 + L1 * cos(theta1);
  float y1 = y0 - L1 * sin(theta1);
  
  float x2 = x1 + L2 * cos(theta1 + theta2);
  float y2 = y1 - L2 * sin(theta1 + theta2);
  
  // desenhar braço
  strokeWeight(8);
  stroke(0);
  line(x0, y0, x1, y1);   // braço
  line(x1, y1, x2, y2);   // antebraço
  
  // desenhar juntas
  fill(255,0,0);
  ellipse(x0, y0, 20, 20); // ombro
  ellipse(x1, y1, 20, 20); // cotovelo
  ellipse(x2, y2, 20, 20); // mão
}
