import cv2
import numpy as np

#이미지에 색상 반전 효과를 추가 함수
def inverted_effect(image, invert_strength):
    #image: 이미지
    #invert_strength: 반전강도

    inverted = invert_strength - image  # 완전 반전된 이미지

    return inverted

#슬라이더 값 변경에 따라 색상 반전 효과를 업데이트하는 콜백함수
def update_inversion(val):
    # val(int): 슬라이더 값.
    
    # 현재 강도 값에 따라 새로운 반전 이미지를 생성
    inverted_image = inverted_effect(image, val)
    
    # 업데이트된 반전 이미지를 "Inverted Image" 창에 표시
    cv2.imshow("Inverted Image", inverted_image)


# ---------- 메인 코드 ----------
# 이미지 파일을 불러오기
image_path = "dog.png"  # 사용하려는 이미지 파일의 경로를 설정한다.
image = cv2.imread(image_path)  # 이미지를 읽어들인다.

# 이미지가 올바르게 로드되지 않은 경우 오류 메시지를 출력하고 프로그램을 종료
if image is None:
    print("Error")
    exit()

# 초기 슬라이더 값 설정
initial_invert_strength = 255  # 슬라이더 초기값: 최대 반전 강도 (255)


# ---------- UI 구성 ----------
# 원본 이미지를 표시
cv2.imshow("Original Image", image)  # "Original Image" 창에 원본 이미지를 띄운다
update_inversion(initial_invert_strength) # 초기 상태에서 반전 효과를 한 번 적용하여 표시

# 반전 효과를 보여줄 창을 생성
cv2.namedWindow("Inverted Image")

# 슬라이더를 생성
cv2.createTrackbar(
    "Invert Strength",  # 슬라이더 이름
    "Inverted Image",  # 슬라이더가 표시될 창 이름
    initial_invert_strength,  # 슬라이더 초기값
    255,  # 슬라이더 최대값 (0~255 범위)
    update_inversion  # 슬라이더 값 변경 시 호출될 콜백 함수
)


# ---------- 프로그램 실행 및 종료 처리 ----------
cv2.waitKey()  # 사용자가 키를 누를 때까지 대기
cv2.destroyAllWindows()  # 생성된 모든 OpenCV 창을 닫는다
