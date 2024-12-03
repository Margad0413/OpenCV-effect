import cv2
import numpy as np

# 스케치 효과와 윤곽선 강조를 추가하는 함수
def apply_sketch_effect_with_edges(image, blur_intensity):
    # image: 원본 이미지
    # blur_intensity: 블러 강도 (홀수 값이어야 함)

    # 이미지를 그레이스케일로 변환하여 명암 정보를 추출
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 블러 강도를 홀수로 강제 변환 (OpenCV에서 블러 크기는 홀수여야 함)
    blur_intensity = max(1, blur_intensity | 1)
    
    # 반전된 이미지를 Gaussian Blur로 부드럽게 처리(이미지,커널크기,표준편차)
    blurred = cv2.GaussianBlur(gray, (blur_intensity, blur_intensity), 0)
    cv2.imshow("Blurred", blurred)
    # 원본 명암과 블러 이미지를 나누어 스케치 효과 생성(분자,분모, 곱해질 스칼라 값)
    sketch = cv2.divide(gray, blurred, scale=256)
    cv2.imshow("Sketch", sketch)
    return sketch

# 슬라이더 값 변경에 따라 스케치 효과를 업데이트하는 콜백 함수
def update_sketch(val):
    # val(int): 슬라이더 값

    # 현재 블러 강도로 스케치 효과를 적용
    sketch_image = apply_sketch_effect_with_edges(image, val)

    # 업데이트된 이미지를 "Sketch Effect" 창에 표시
    cv2.imshow("Sketch Effect", sketch_image)

# ---------- 메인 코드 ----------
# 이미지 파일을 로드
image_path = "dog.png"  # 사용할 이미지 파일의 경로를 설정
image = cv2.imread(image_path)  # 이미지를 읽어들임

# 이미지가 올바르게 로드되지 않은 경우 오류 메시지를 출력하고 프로그램을 종료
if image is None:
    print("Error")
    exit()

# 초기 슬라이더 값 설정
initial_blur_intensity = 25  # 초기 블러 강도 값 (홀수)

# ---------- UI 구성 ----------
# 원본 이미지를 표시
cv2.imshow("Original Image", image)  # "Original Image" 창에 원본 이미지를 띄움
update_sketch(initial_blur_intensity) # 초기 상태에서 스케치 효과를 한 번 적용하여 표시

# 스케치 효과를 보여줄 창을 생성
cv2.namedWindow("Sketch Effect")

# 슬라이더를 생성
cv2.createTrackbar(
    "Blur Intensity",  # 슬라이더 이름
    "Sketch Effect",  # 슬라이더가 표시될 창 이름
    initial_blur_intensity,  # 슬라이더 초기값
    51,  # 슬라이더 최대값
    update_sketch  # 슬라이더 값 변경 시 호출될 콜백 함수
)

# ---------- 프로그램 실행 및 종료 처리 ----------
cv2.waitKey()  # 사용자가 키를 누를 때까지 대기
cv2.destroyAllWindows()  # 생성된 모든 OpenCV 창을 닫음
