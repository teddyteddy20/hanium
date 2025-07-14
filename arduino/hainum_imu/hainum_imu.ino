#include <Wire.h>
#include <Adafruit_BNO055.h>
#include <Adafruit_Sensor.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);  // 주소 0x28 (ADR이 GND일 때)

void setup() {
  Serial.begin(115200);
  delay(1000);

  if (!bno.begin()) {
    Serial.println("BNO055 연결 실패! 전원 또는 I2C 연결을 확인하세요.");
    while (1);
  }

  bno.setExtCrystalUse(true);  // 정확도를 높이기 위한 외부 크리스탈 사용 설정
}

void loop() {
  sensors_event_t event;
  bno.getEvent(&event);

  Serial.print("Heading: ");
  Serial.print(event.orientation.x);
  Serial.print("  Pitch: ");
  Serial.print(event.orientation.y);
  Serial.print("  Roll: ");
  Serial.println(event.orientation.z);

  delay(500);
}
