from collections import defaultdict


def timeToSec(time):
    h, m, s = map(int, time.split(":"))
    return (h * 3600) + (m * 60) + s


def insertTime(start_time, end_time, totalBoard):
    start_time, end_time = timeToSec(start_time), timeToSec(end_time)
    for i in range(start_time, end_time + 1):
        totalBoard[i] += 1


def makePrefixSumList(prefixSum, totalBoard):
    for i in range(len(totalBoard)):
        prefixSum.append(prefixSum[i] + totalBoard[i])


def goAnswer(prefixSum, adv, totalPlayTimeSec):
    answer = -1
    maxValue = -1
    start = 1
    end = adv
    while end < totalPlayTimeSec:
        now = prefixSum[end] - prefixSum[start - 1]
        if now > maxValue:
            answer = start
            maxValue = now
    return answer


def solution(play_time, adv_time, logs):
    totalPlayTimeSec = timeToSec(play_time) + 1
    totalBoard = [0 for _ in range(totalPlayTimeSec)]
    for log in logs:
        start_time, end_time = log.split("-")
        insertTime(start_time, end_time, totalBoard)

    prefixSum = [0]
    makePrefixSumList(prefixSum, totalBoard)
    answerSec = goAnswer(prefixSum, timeToSec(adv_time), totalPlayTimeSec)
    print(answerSec)
