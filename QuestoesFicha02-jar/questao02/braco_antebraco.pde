float comprimento_braco = 100;  // comprimento do braço (escala, 2 -> 100 px)
float comprimento_antebraco = 150;  // comprimento do antebraço (3 -> 150 px)

float posicao_ombro = 400, y0 = 400;  // ombro (fixo no meio da tela)

// ângulos iniciais
float angulo_braco = PI/2;   // braço começa na vertical (90 graus)
float angulo_antebraco = 0;      // antebraço alinhado com o braço

// velocidades
float duracao = 7.0;    // em segundos
float fps = 60.0;
float totalFrames = duracao * fps;

float velocidade_braco = (PI/2) / totalFrames;  // ajusta movimento para terminar em 7s
float velocidade_antebraco = 2 * velocidade_braco;            // antebraço gira 2x mais rápido

void setup() {
  size(800, 600); //tamanho da tela
  frameRate(60);
}

void draw() {
  background(220);
  
  // atualizar ângulos
  if (frameCount <= totalFrames) { //A cada quadro (frame), diminui o valor dos ângulos -> rotação sentido horário.
    angulo_braco -= velocidade_braco;  // braço rotaciona
    angulo_antebraco -= velocidade_antebraco;  // antebraço rotaciona mais rápido
  }
  
  // calcular posições (Estou utilizando cos e sin para converter o comprimento e o ângulo em coordenadas x/y.)
  float posicao_cotovelo_x = posicao_ombro + comprimento_braco * cos(angulo_braco);
  float posicao_cotovelo_y = y0 - comprimento_braco * sin(angulo_braco);
  
  float posicao_mao_x = posicao_cotovelo_x + comprimento_antebraco * cos(angulo_braco + angulo_antebraco);
  float posicao_mao_y = posicao_cotovelo_y - comprimento_antebraco * sin(angulo_braco + angulo_antebraco);
  
  // desenhar braço
  strokeWeight(8);
  stroke(0);
  line(posicao_ombro, y0, posicao_cotovelo_x, posicao_cotovelo_y);   // braço
  line(posicao_cotovelo_x, posicao_cotovelo_y, posicao_mao_x, posicao_mao_y);   // antebraço
  
  // desenhar juntas
  fill(255,0,0);
  ellipse(posicao_ombro, y0, 20, 20); // ombro
  ellipse(posicao_cotovelo_x, posicao_cotovelo_y, 20, 20); // cotovelo
  ellipse(posicao_mao_x, posicao_mao_y, 20, 20); // mão
}
