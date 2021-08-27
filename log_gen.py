from _datetime import datetime
import time
from random import randrange

log_path = 'C:/Dummy'
log_start = datetime.now().strftime("%y%m%d%H%M%S")
chat_start = None
chat_end = None
exam_log_file = "student_" + log_start + ".log"
logging_level = "INFO"

with open(log_path + "/" + exam_log_file, 'w+') as f:
    f.writelines([])


def test_start(student_ID, subject):
    log_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    event = "TEST_STARTED"
    description = "test started by " + student_ID + " logged for " + student_ID
    log_text = log_time + " - " + logging_level + " -  " + subject + " - " + event + " - " + description + "\n"
    with open(log_path + "/" + exam_log_file, 'a') as f:
        f.writelines(log_text)


def test_inter(student_ID, subject):
    log_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    event = "TEST_INTERRUPTION"
    description = "test interrupted by " + student_ID + " logged for " + student_ID
    log_text = log_time + " - " + logging_level + " -  " + subject + " - " + event + " - " + description + "\n"
    with open(log_path + "/" + exam_log_file, 'a') as f:
        f.writelines(log_text)


def test_end(student_ID, subject):
    log_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    event = "TEST_ENDED"
    description = "test ended by " + student_ID + " logged for " + student_ID
    log_text = log_time + " - " + logging_level + " -  " + subject + " - " + event + " - " + description + "\n"
    with open(log_path + "/" + exam_log_file, 'a') as f:
        f.writelines(log_text)


def chat(student_ID, subject, proctor_ID, dur):
    lines = []
    log_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    event = "CHAT_START"
    chat_start = datetime.now().strftime("%y%m%d%H%M%S")
    description = "chat initiated by " + student_ID + " with proctor " + proctor_ID + " logged for " + student_ID
    log_text = log_time + " - " + logging_level + " -  " + subject + " - " + event + " - " + description + "\n"
    lines.append(log_text)
    time.sleep(dur)
    log_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    event = "CHAT_END"
    description = "chat ended by " + student_ID + " with proctor " + proctor_ID + " logged for " + student_ID
    if event == "CHAT_END":
        chat_end = datetime.now().strftime("%y%m%d%H%M%S")
        duration = str(int(chat_end) - int(chat_start))
        log_text = log_time + " - " + logging_level + " -  " + subject + " - " + event + " - " + description + " dur = " + duration + "s" + "\n"
    lines.append(log_text)
    with open(log_path + "/" + exam_log_file, 'a') as f:
        f.writelines(lines)


def audio_issue(student_ID, subject):
    log_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    event = "AUDIO_ISSUE"
    description = "noise/audio issue by " + student_ID + " logged for " + student_ID
    log_text = log_time + " - " + logging_level + " -  " + subject + " - " + event + " - " + description + "\n"
    with open(log_path + "/" + exam_log_file, 'a') as f:
        f.writelines(log_text)


def video_issue(student_ID, subject):
    log_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    event = "VIDEO_ISSUE"
    description = "video issue by " + student_ID + " logged for " + student_ID
    log_text = log_time + " - " + logging_level + " -  " + subject + " - " + event + " - " + description + "\n"
    with open(log_path + "/" + exam_log_file, 'a') as f:
        f.writelines(log_text)


def image_upload(student_ID, subject, status):
    log_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    event = "IMAGE_UPLOAD"
    if status == 0:
        description = "image upload " + "failed" + " by " + student_ID + " logged for " + student_ID
    else:
        description = "image upload " + "success" + " by " + student_ID + " logged for " + student_ID
    log_text = log_time + " - " + logging_level + " -  " + subject + " - " + event + " - " + description + "\n"
    with open(log_path + "/" + exam_log_file, 'a') as f:
        f.writelines(log_text)


subject = ["DSE512001", "DSE512002","DSE512003", "DSE512004"]

for i in range(26, 50):
    student_ID = "2018AP045" + str(i)
    proctor_ID = str(randrange(1, 6))
    for sub in subject:
        test_start(student_ID, sub)
        if i % 2 == 0:
            test_inter(student_ID, sub)
        chat(student_ID, sub, proctor_ID, randrange(5, 10))
        image_upload(student_ID, sub, randrange(0, 2))
        if i % 4 == 1:
            video_issue(student_ID,sub)
        if i % 3 == 0:
            audio_issue(student_ID,sub)
        test_end(student_ID, sub)
