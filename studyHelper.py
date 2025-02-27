# 시작 모듈
import tkinter
import os

from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox
from time import strftime

# 기본 창 생성
root = Tk()

# 기본 창 설정
root.title("Study Helper")
root.geometry("809x500-500+100")
root.resizable(False, False)

# 탭 생성
# Codemy.com, https://www.youtube.com/watch?v=kqbkUKIc1Gk&feature=youtu.be 학습 및 변형
notebook = ttk.Notebook(root, width=809, height=500)
notebook.pack()

# 학습 탭
frame1 = Frame(root)
notebook.add(frame1, text="학습")

# 학점 입력
def myFinal():
    number_of_subject = int(input("과목 개수를 입력해주세요 : "))

    # 리스트
    subject_name = list()
    subject_score = list()
    subject_grade = list()

    # 반복 실행
    while len(subject_name) != number_of_subject:
        subject_name.append(input("과목명 : "))
        subject_score.append(input("성적(알파벳) : "))
        subject_grade.append(input("학점 : "))

    # 정의
    score = 0
    amount_of_grade = 0

    # for문 반복
    for index, value in enumerate(subject_score):

        # 학점 합산
        grade = int(subject_grade[index])
        amount_of_grade += grade

        # 등급 구간, 계산
        if value == 'A+':
            score += 4.3 * grade
        elif value == 'A':
            score += 4.0 * grade
        elif value == 'A-':
            score += 3.7 * grade
        elif value == 'B+':
            score += 3.3 * grade
        elif value == 'B':
            score += 3.0 * grade
        elif value == 'B-':
            score += 2.7 * grade
        elif value == 'C+':
            score += 2.3 * grade
        elif value == 'C':
            score += 2.0 * grade
        elif value == 'C-':
            score += 1.7 * grade
        elif value == 'F':
            score += 0
        else:
            amount_of_grade -= grade

    # 결과 메시지 박스
    aver = score/amount_of_grade
    messagebox.showinfo("학점 계산기","이번 학기에 들은 총 학점 : {0}\n평균 학점 : {1}"
                        "\n\n이번 학기도 수고 많으셨어요!\n이제 쉬어요!".format(amount_of_grade, round(aver, 2)))

    # 학점 별명 정의
    global mygpa
    mygpa = round(aver, 2)

# 학점 별명
def labeling():

    # while 이용해서 오류 잡기
    while True:
        try:
            if mygpa >= 4.1:
                plus = "{0}인 당신! \n공부의 신!".format(mygpa)
            elif mygpa >= 3.9:
                plus = "{0}인 당신! \n교수님의 사랑!".format(mygpa)
            elif mygpa >= 3.5:
                plus = "{0}인 당신! \n교수님의 귀염둥이!".format(mygpa)
            elif mygpa >= 3.2:
                plus = "{0}인 당신! \n성실한 이대생!".format(mygpa)
            elif mygpa >= 2.9:
                plus = "{0}인 당신! \n일탈을 꿈꾸는 소시민!".format(mygpa)
            elif mygpa >= 2.3:
                plus = "{0}인 당신! \n오락문화의 선구자!".format(mygpa)
            elif mygpa >= 1.8:
                plus = "{0}인 당신! \n영차 달팽이!".format(mygpa)
            elif mygpa >= 1.1:
                plus = "{0}인 당신! \n귀여운 플라크톤!".format(mygpa)
            else:
                plus = "{0}인 당신! \n시대를 앞서가는 혁명의 씨앗!".format(mygpa)

            # 결과 메시지 박스
            messagebox.showinfo("학점 별명", plus)
            break

        # 오류 메시지 박스
        except:
            messagebox.showinfo("학점 계산기", "학점 계산부터 해주세요!")

# 사용법 설명
message = Label(frame1, text="과목명, 성적, 학점을 순서대로 입력하고,"
                             "\n재밌는 학점 별명까지 얻으세요"
                             "\n(성적은 알파벳 대문자로 입력하고 A0는 A로 입력합니다)")
message.pack(side=BOTTOM)

# 학점 별명 위치 설정
labeling_B = Button(frame1, width=15, text = "학점 별명 얻기", font=(None, 20), fg ="green", command = labeling)
labeling_B.pack(pady=35, side=BOTTOM)

#학점 계산 위치 설정
final = Button(frame1, width=15, text = "학점 계산하기", font=(None, 20), fg ="green", command = myFinal)
final.pack(side=BOTTOM)

# 현재 파일이 있는 디렉토리를 기준으로 ewha.png 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "ewha.png")

# 배경 사진 설정
ewha = PhotoImage(file=image_path)
label9 = Label(frame1, image=ewha)
label9.pack(side="bottom")

# 시간 탭
frame2 = Frame(root)
notebook.add(frame2, text="시간")

# 날짜
# 날짜 함수 정의
def day():
    string = strftime('\n%Y %B %d')
    # Python's strftime reference, https://strftime.org 학습 및 변형
    lb2.config(text = string)

# 날짜 형식, 표시
lb2 = Label(frame2, fg = 'green', font = (None, 25, 'bold'))
lb2.pack()
day()

# 시간
# 시간 함수 정의
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    # 실시간 시간
    # Python | after method in Tkinter, https: // www.geeksforgeeks.org 학습 및 변형
    lbl.after(1000, time)

# 시간 형식, 표시
lbl = Label(frame2, bg = 'green', fg = 'white', font = (None, 25, 'bold'))
lbl.pack()
time()

# 빈 공간
space = Label(frame2, text = "\n", font = (None, 3))
space.pack()


# 타이머
# 정의
Type_tab2 = 0
One = 0

# 타이머 시작 함수
# Basic date and time types, https://docs.python.org/3/library/datetime.html 학습 및 변형
# GeeksforGeeks, https://www.geeksforgeeks.org/create-countdown-timer-using-python-tkinter/ 학습 및 변형
def tab2_submit():
    global Type_tab2, One, Hour, Min, Sec

    if (Type_tab2 == 1):
        return
    if (One == 0):
        One = 1
        Hour = int(timer_1.get())
        Min = int(timer_2.get())
        Sec = int(timer_3.get())

    t = datetime.time(Hour, Min, Sec)
    time_label.configure(text=t, font=(None, 45))
    Sec -= 1
    if (Sec < 0):
        if (Hour + Min + Sec == -1):
            Hour = int(timer_1.get())
            Min = int(timer_2.get())
            Sec = int(timer_3.get())

            # 완료
            messagebox.showinfo("타이머", "시간이 다 되었습니다!")
            time_label.configure(text=t, font=(None, 45))
            One = 0
            return
        Min -= 1
        Sec = 59
        if (Min < 0):
            Hour -= 1
            Min = 59
    root.after(1000, tab2_submit)

# 정의
timer_1 = StringVar()
timer_2 = StringVar()
timer_3 = StringVar()


# hour 위치 설정
labelframe1 = LabelFrame(frame2, text="Hour")
labelframe1.pack(pady=5)

# The Tkinter Scale Widget, http://effbot.org/tkinterbook/scale.htm 학습 및 변형
scale_1 = ttk.Scale(labelframe1, orient=HORIZONTAL, length=300, variable=timer_1,
                    command=lambda x: timer_1.set('%d' % (float(x) + 0.5)), from_=0, to=23)
scale_1.grid()

# The Tkinter Spinbox Widget, http://effbot.org/tkinterbook/spinbox.htm 학습 및 변형
spinbox_1 = Spinbox(labelframe1, from_=0, to=23, width=5)
spinbox_1.grid(row=0, column=1)

# min 위치 설정
labelframe2 = LabelFrame(frame2, text="Min")
labelframe2.pack(pady=5)

scale_2 = ttk.Scale(labelframe2, orient=HORIZONTAL, length=300, variable=timer_2,
                    command=lambda x: timer_2.set('%d' % (float(x) + 0.5)), from_=0, to=59)
scale_2.grid()

spinbox_2 = Spinbox(labelframe2, from_=0, to=59, textvariable=timer_2, width=5)
spinbox_2.grid(row=0, column=1)

# sec 위치 설정
labelframe3 = LabelFrame(frame2, text="Sec")
labelframe3.pack(pady=5)

scale_3 = ttk.Scale(labelframe3, orient=HORIZONTAL, length=300, variable=timer_3,
                    command=lambda x: timer_3.set('%d' % (float(x) + 0.5)), from_=0, to=59)
scale_3.grid()

spinbox_3 = Spinbox(labelframe3, from_=0, to=59, textvariable=timer_3, width=5)
spinbox_3.grid(row=0, column=1)


# 시작 위치 설정
button_1 = ttk.Button(frame2, text="시작", width = 10, command=tab2_submit)
button_1.pack(pady=10)

# 카운트다운 표시
time_label = Label(frame2, text="00:00:00", fg= "green", font=(None, 45))
time_label.pack()

# 사용법 설명
message = Label(frame2, text="시간을 확인하거나, 시간을 설정하여 타이머를 이용하세요")
message.pack(side=BOTTOM)


# 메모 탭
frame3 = Frame(root)
notebook.add(frame3, text="메모")

# 텍스트 메모
textbox = Text(frame3, width=105, height=3, font=(None, 20), highlightbackground = "green")
textbox.pack()

# 그리는 메모
# 함수 정의
# The Tkinter Canvas Widget, https://effbot.org/tkinterbook/canvas.htm 학습 및 변형
def paint(event):
    x1, y1 = (event.x - 5), (event.y - 5)
    x2, y2 = (event.x + 5), (event.y + 5)
    w.create_oval(x1, y1, x2, y2, fill= "green", outline= "green", width=10)

# 캔버스 설정
w = Canvas(frame3, width=500, height=150, background='beige', cursor="pencil")
w.pack(expand=YES, fill=BOTH)
w.bind("<B1-Motion>", paint)

# 사용법 설명
message = Label(frame3, text="텍스트 박스에 입력하거나, 마우스를 이용해서 그리세요")
message.pack(side=BOTTOM)

# 지우기 함수
def Click():
    delete2 = w.delete(ALL)

# 지우기 버튼 설정
button1 = Button(frame3, text = "지우기", padx=10, pady=5, command=Click, fg='red')
button1.pack(side=BOTTOM)

# 최종 실행
mainloop()
