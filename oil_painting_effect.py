import cv2
import numpy as np

# 오일 페인팅 효과를 이미지에 추가하는 함수
def apply_oil_painting_effect(image, size):
    # image: 원본 이미지
    # size: 필터 크기 (값이 클수록 효과가 부드러워짐)
    
    # 오일 페인팅 효과를 OpenCV의 xphoto 모듈을 사용해 적용
    oil_painting = cv2.xphoto.oilPainting(image, size, 1)
    return oil_painting

# 슬라이더 값 변경에 따라 오일 페인팅 효과를 업데이트하는 콜백 함수
def update_oil_painting(val):
    # val(int): 슬라이더 값 (필터 크기를 결정)
    
    size = max(1, val | 1)  # 필터 크기를 홀수로 강제 변환 (OpenCV 요구사항)
    
    # 현재 필터 크기를 사용하여 오일 페인팅 효과 적용
    updated_image = apply_oil_painting_effect(image, size)
    
    # 업데이트된 이미지를 "Oil Painting Effect" 창에 표시
    cv2.imshow("Oil Painting Effect", updated_image)

# ---------- 메인 코드 ----------

# 이미지 파일을 로드
image_path = "dog.png"  # 사용하려는 이미지 파일의 경로를 설정
image = cv2.imread(image_path)  # 이미지를 읽어들임

# 이미지가 올바르게 로드되지 않은 경우 오류 메시지를 출력하고 프로그램을 종료
if image is None:
    print("Error")
    exit()

# 초기 슬라이더 값 설정
max_size = 10  # 슬라이더 최대값 (필터 크기의 범위)
initial_size = 5  # 초기값은 슬라이더 중앙 값으로 설정

# ---------- UI 구성 ----------

# 원본 이미지를 표시
cv2.imshow("Original Image", image)  # "Original Image" 창에 원본 이미지를 띄움
update_oil_painting(initial_size) # 초기 상태에서 오일 페인팅 효과를 한 번 적용하여 표시

# 오일 페인팅 효과를 보여줄 창을 생성
cv2.namedWindow("Oil Painting Effect")

# 슬라이더를 생성
cv2.createTrackbar(
    "Effect Size",  # 슬라이더 이름
    "Oil Painting Effect",  # 슬라이더가 표시될 창 이름
    initial_size,  # 슬라이더 초기값
    max_size,  # 슬라이더 최대값
    update_oil_painting  # 슬라이더 값 변경 시 호출될 콜백 함수
)

# ---------- 프로그램 실행 및 종료 처리 ----------
cv2.waitKey()  # 사용자가 키를 누를 때까지 대기
cv2.destroyAllWindows()  # 생성된 모든 OpenCV 창을 닫음
