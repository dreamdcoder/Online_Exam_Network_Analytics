from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

spark_context = SparkContext(master="local",appName="exam")


def mrLog(lines):
    # lines = '201224233712 - INFO -  DSE512002 - AUDIO_ISSUE - noise/audio issue by 2018AP0453 logged for 2018AP0453'
    event_issues = ['TEST_INTERRUPTION', 'AUDIO_ISSUE', 'VIDEO_ISSUE']
    lines_split = lines.split(" - ")
    time_stamp = lines_split[0]
    subject = lines_split[2]
    log_event = lines_split[3]
    description = lines_split[4]
    if description.__contains__("dur"):
        text = description.split(" for ")[1]
        text = text.split("dur = ")
        student_id = text[0]
        chat_duration = int(text[1].strip('s'))
    else:
        student_id = description.split(" for ")[1]
        chat_duration = 0
    if log_event in event_issues or description.__contains__("failed"):
        is_issue = 1
    else:
        is_issue = 0

    return time_stamp, subject, student_id, log_event, description, chat_duration, is_issue


# print(time_stamp, subject, log_event, description, student_id, chat_duration)
if __name__ == '__main__':
    x = spark_context.textFile("hdfs://localhost:9000/logs/FlumeData.*").map(mrLog)
    # print(x.collect())
    spark = SparkSession.builder.appName("exam").enableHiveSupport().getOrCreate()
    df = spark.createDataFrame(x, ['time_stamp', 'subject', 'student_id', 'log_event', 'description', 'chat_duration',
                                   'is_issue'])
    df.show()
    df.createOrReplaceTempView("table1")
    spark.sql("drop table if exists exam_log")
    spark.sql("create table exam_log as select * from table1")
