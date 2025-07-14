const int mq2Pin = A0;
const int mq7Pin = A1;
const int mq135Pin = A2;

// 보정된 R0 값 (깨끗한 공기에서 측정한 값, 예시값)
float R0_MQ2 = 5.0;
float R0_MQ7 = 10.0;
float R0_MQ135 = 15.0;

// 센서별 로드 저항값 (보드에 따라 다를 수 있음)
const float RL_MQ2 = 5.0;     // kΩ
const float RL_MQ7 = 10.0;    // kΩ
const float RL_MQ135 = 20.0;  // kΩ

void setup() {
  Serial.begin(9600);
}

void loop() {
  readSensor(mq2Pin, R0_MQ2, RL_MQ2, "MQ-2");
  readSensor(mq7Pin, R0_MQ7, RL_MQ7, "MQ-7");
  readSensor(mq135Pin, R0_MQ135, RL_MQ135, "MQ-135");

  Serial.println("--------");
  delay(2000);  // 2초마다 측정
}

void readSensor(int analogPin, float R0, float RL, String label) {
  int rawADC = analogRead(analogPin);
  float voltage = rawADC * (5.0 / 1023.0);
  float RS = (5.0 - voltage) / voltage * RL;   // Rs 계산
  float ratio = RS / R0;

  // 데이터시트 기반 추정 공식 (근사)
  float a, b;
  if (label == "MQ-2") {
    a = 100.0;
    b = -1.5;
  } else if (label == "MQ-7") {
    a = 70.0;
    b = -1.4;
  } else if (label == "MQ-135") {
    a = 110.0;
    b = -1.2;
  }

  float ppm = a * pow(ratio, b);

  // 출력
  Serial.print(label);
  Serial.print(" | Raw: ");
  Serial.print(rawADC);
  Serial.print(" | Voltage: ");
  Serial.print(voltage, 2);
  Serial.print("V | Rs: ");
  Serial.print(RS, 2);
  Serial.print("kΩ | Ratio: ");
  Serial.print(ratio, 2);
  Serial.print(" | Estimated PPM: ");
  Serial.println(ppm, 1);
}
