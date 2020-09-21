#파이게임 라이브러리 및 게임 엔진 초기화
import pygame
pygame.init()

#색상 정의
BLACK = (0,0,0)
WHITE = (255,255,255)

#새 윈도우 열기
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#사용자가 게임을 종료하기 전까지 루프는 계속됨
carryOn = True

#화면 갱신 시간 제어
clock = pygame.time.Clock()


#-------------메인 프로그램 루프--------------
while carryOn:
    #----메인 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False #루프를 빠져나가는 플래그 변수 
    #----게임 로직

    #----렌더링 코드
    screen.fill(BLACK) #화면을 검정으로 깨끗이 
    pygame.draw.line(screen, WHITE, [349,0],[349,500],5)

    #----화면 갱신(페이지 교체)
    pygame.display.flip()
    #----프레임 조정
    clock.tick(60)
    
pygame.quit()    
