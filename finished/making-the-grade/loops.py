def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    for index in range(len(student_scores)):
        student_scores[index] = round(student_scores[index])
    return student_scores


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    fails = 0
    for score in student_scores:
        if score < 41:
            fails = fails + 1
    return fails


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    return best_scores


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    step = round((highest - 40) / 4)
    grades = [41]
    for index in range(3):
        next_grade = grades[index] + step
        grades.append(next_grade)
    return grades


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    ranks = []
    for index in range(len(student_scores)):
        rank = str(index + 1) + '. ' + \
            student_names[index] + ': ' + str(student_scores[index])
        ranks.append(rank)
    return ranks


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    perfect_score = []
    for student in student_info:
        if student[1] == 100:
            perfect_score = student
            break
    return perfect_score
