#define RPWM1 2
#define LPWM1 3
#define R_EN1 22
#define L_EN1 23
volatile long encoder_count1 = 0; 


#define RPWM2 4 
#define LPWM2 5 
#define R_EN2 24 
#define L_EN2 25
volatile long encoder_count2 = 0; 

#define RPWM3 6 
#define LPWM3 7 
#define R_EN3 26 
#define L_EN3 27
volatile long encoder_count3 = 0; 

#define RPWM4 8 
#define LPWM4 9
#define R_EN4 28 
#define L_EN4 29
volatile long encoder_count4 = 0; 

void rampMotor1Forward(int targetPWM, int delayStep = 10, int stepSize = 5);

int pwm = 200;  // 목표 PWM 값

void setup() {
  pinMode(RPWM1, OUTPUT);
  pinMode(LPWM1, OUTPUT);
  pinMode(R_EN1, OUTPUT);
  pinMode(L_EN1, OUTPUT);

  digitalWrite(R_EN1, HIGH);
  digitalWrite(L_EN1, HIGH);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String msg = Serial.readStringUntil('\n');
    msg.trim();

    if (msg == "GoForward") {
      
      Serial.println("▶ SEND 명령 수신: 모터1 전진 시작");
      rampMotor1Forward(pwm); // 전진
      delay(3000);            // 3초 전진
      rampMotor1Forward(0);   // 정지
    }
  }
}

// 부드럽게 모터1 PWM 제어 (정방향)
void rampMotor1Forward(int targetPWM, int delayStep = 10, int stepSize = 5) {
  static int currentPWM = 0;

  if (targetPWM > currentPWM) {
    for (int i = currentPWM; i <= targetPWM; i += stepSize) {
      analogWrite(RPWM1, 0);          // 역방향 OFF
      analogWrite(LPWM1, i);          // 정방향 ON
      delay(delayStep);
    }
  } else {
    for (int i = currentPWM; i >= targetPWM; i -= stepSize) {
      analogWrite(RPWM1, 0);
      analogWrite(LPWM1, i);
      delay(delayStep);
    }
  }

  currentPWM = targetPWM;
}
