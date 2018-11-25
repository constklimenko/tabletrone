
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
    u"""Keeps information about time, number of lessons and teachers.
    Содержит сведения о времени занятий, их числе ,
    группах и преподавателях.
    """

    def __init__(self, GroupsList, TeachersList, HoursInDay):
        """ initiation with an empty 3D table."""
        self.groupsList = GroupsList
        self.teachersList = TeachersList

        self.table = [[[
                      0
                      for _ in range(GroupsList.len)]
                      for _ in range(TeachersList.len)]
                      for _ in range(HoursInDay.summHours)]

    def fillTable(self):
        # заполняет таблицу на основе уже внесенных данных
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


class HoursInDay(object):
    u"""Keep information about number of lessons per day."""
    def __init__(self,
                 monday=5,
                 tuesday=5,
                 wednesday=5,
                 thursday=5,
                 friday=5,
                 saturday=0,
                 sunday=0):
        self.list = [monday, tuesday, wednesday,
                     thursday, friday, saturday, sunday]
        self.summHours = (monday + tuesday + wednesday +
                          thursday + friday + saturday + sunday)


class TeachersList(list):
    u"""Keep information about teachers ."""
    def __init__(self, *teachers):
        self.list = teachers
        self.len = len(self.list)


class GroupsList(object):
    u"""Keep information about study groups."""
    def __init__(self, *groups):
        self.list = groups
        self.len = len(self.list)
