from general import FieldSubjects, GlobalStat
from random import randint
from game import settings


class Point(FieldSubjects):

    # def __init__(self, *a, **k):
    #     super(FieldSubjects, self).__init__(*a, **k)
    def __init__(self, *a, **k):
        super().__init__(*a, **k)

        self.value = randint(settings.POINT_MIN_VALUE, settings.POINT_MAX_VALUE)

    def interaction(self, ob=None, x=None, y=None):
        GlobalStat.update_score(self.value)
        return True
