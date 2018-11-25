
"""This application makes timetable without GUI.
Teachers: Name, number of hours per month;
Study groups: number of group, number of hours per month;
Days of the week: the number of classes on each day.

Приложение делает расписание на основе следующих данных:
Преподаватели: Фио, число часов занятий в месяц;
Учебные группы: номер, число часов занятий в месяц;
Дни недели: число занятий в каждый из дней.

Author: Narcom.

E-mail: Narcomacer@gmail.com

"""


class TimeTable(object):
    u"""Keep information about time, number of lessons and teachers.
    Содержит сведения о времени занятий, их числе ,
    группах и преподавателях.
    """

    def __init__(self, GroupList, TeachersList, HoursInDay):
        """ initiation with an empty 3D table."""
        pass


class SchoolUnit(object):
    """Teachers and groups are schoolUnits."""
    def __init__(self, name, hours):
        self.hours = int(hours)  # number of lessons in month / занятий в месяц
        self.name = str(name)


class Teacher(SchoolUnit):
    pass


class StudyGroup(SchoolUnit):
    pass


class TeachersList(list):
    u"""Keep information about teachers ."""
    def __init__(self, teachers):
        pass


class GroupsList(object):
    u"""docstring for ."""
    def __init__(self, groups):
        pass
