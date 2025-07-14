import time  # 시간 관련 함수를 사용하기 위한 모듈 임포트 (예: time.sleep)
import board  # 라즈베리 파이 또는 다른 마이크로컨트롤러의 핀을 정의하는 모듈 임포트
import busio  # I2C, SPI, UART와 같은 시리얼 통신 프로토콜을 사용하기 위한 모듈 임포트

# adafruit_bno055 라이브러리에서 BNO055_I2C 클래스를 임포트합니다.
# 이 클래스는 BNO055 센서와 I2C 통신을 쉽게 할 수 있도록 도와줍니다.
from adafruit_bno055 import BNO055_I2C 

# --- I2C 통신 설정 ---
# I2C 버스를 초기화합니다.
# board.SCL: I2C 통신의 클럭(Clock) 라인 핀 (Serial Clock)
# board.SDA: I2C 통신의 데이터(Data) 라인 핀 (Serial Data)
i2c = busio.I2C(board.SCL, board.SDA)

# --- BNO055 센서 객체 생성 ---
# 초기화된 I2C 버스를 사용하여 BNO055 센서 객체를 생성합니다.
# 이 객체를 통해 센서의 다양한 데이터를 읽어올 수 있습니다.
sensor = BNO055_I2C(i2c)

# --- 무한 루프 시작 ---
# 센서 데이터를 지속적으로 읽고 출력하기 위한 무한 루프입니다.
while True:
    # --- 센서 데이터 읽기 ---
    # BNO055_I2C 객체의 'euler' 속성을 통해 오일러 각도를 읽어옵니다.
    # BNO055 내부에 구현된 센서 퓨전 알고리즘을 통해 계산된 절대 방향 값입니다.
    # heading (방위각, Yaw): 북쪽을 기준으로 시계방향 회전 (0~360도)
    # roll (좌우 기울기): 앞뒤 축을 중심으로 한 좌우 기울기 (-180~180도)
    # pitch (앞뒤 기울기): 좌우 축을 중심으로 한 앞뒤 기울기 (-90~90도)
    heading, roll, pitch = sensor.euler

    # BNO055_I2C 객체의 'acceleration' 속성을 통해 선형 가속도 값을 읽어옵니다.
    # 중력 가속도가 제거된 순수한 선형 가속도입니다. (단위: m/s²)
    accel_x, accel_y, accel_z = sensor.acceleration

    # BNO055_I2C 객체의 'gyro' 속성을 통해 각속도(자이로스코프) 값을 읽어옵니다.
    # 센서의 회전 속도를 나타냅니다. (단위: deg/s, 초당 도)
    gyro_x, gyro_y, gyro_z = sensor.gyro

    # BNO055_I2C 객체의 'temperature' 속성을 통해 센서 내부 온도를 읽어옵니다. (단위: °C)
    temp = sensor.temperature

    # --- 데이터 출력 ---
    # f-string을 사용하여 읽어온 방향 데이터를 형식에 맞춰 출력합니다.
    # {:.2f}는 소수점 이하 두 자리까지 표시하도록 포맷팅합니다.
    print(f"Heading: {heading:.2f}°, Roll: {roll:.2f}°, Pitch: {pitch:.2f}°")
    
    # 가속도 데이터를 출력합니다.
    print(f"Acceleration (m/s²) - X: {accel_x:.2f}, Y: {accel_y:.2f}, Z: {accel_z:.2f}")
    
    # 자이로스코프 데이터를 출력합니다.
    print(f"Gyroscope (deg/s) - X: {gyro_x:.2f}, Y: {gyro_y:.2f}, Z: {gyro_z:.2f}")
    
    # 온도 데이터를 출력합니다.
    print(f"Temperature: {temp} °C")
    
    # 각 데이터 세트 구분을 위한 구분선을 출력합니다.
    print("-----------------------------")

    # --- 딜레이 ---
    # 1초 동안 프로그램 실행을 일시 중지하여 데이터가 너무 빠르게 출력되는 것을 방지합니다.
    time.sleep(1)