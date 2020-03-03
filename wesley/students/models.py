import datetime
from django.db import models
from django.urls import reverse

day_of_week = (('monday', 'Monday'), ('tuesday', 'Tuesday'), (
    'wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'))

time_choices = ((datetime.time(16, 00, 00), '16:00'),
                (datetime.time(16, 20, 00), '16:20'),
                (datetime.time(16, 40, 00), '16:40'),
                (datetime.time(17, 00, 00), '17:00'),
                (datetime.time(17, 20, 00), '17:20'),
                (datetime.time(17, 40, 00), '17:40'),
                (datetime.time(18, 00, 00), '18:00'),
                (datetime.time(18, 20, 00), '18:20'),
                (datetime.time(18, 45, 00), '18:45'),
                (datetime.time(19, 5, 00), '19:05'),
                (datetime.time(19, 25, 00), '19:25'),
                (datetime.time(20, 10, 00), '20:10'),
                (datetime.time(20, 30, 00), '20:30'),
                (datetime.time(20, 50, 00), '20:50'),
                (datetime.time(21, 15, 00), '21:15'),
                (datetime.time(21, 35, 00), '21:35'),
                (datetime.time(21, 55, 00), '21:55'),
                (datetime.time(22, 20, 00), '22:20'),
                (datetime.time(22, 40, 00), '22:40'),
                (datetime.time(23, 00, 00), '23:00'),
                (datetime.time(23, 20, 00), '23:20'), )


class Group(models.Model):
    class_name = models.CharField(unique=True, max_length=10)

    class Meta:
        ordering = ['class_name', ]

    def __str__(self):
        return self.class_name


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    room_number = models.IntegerField()

    def __str__(self):
        return '{} - {}'.format(self.name, self.room_number)


class Student(models.Model):
    korean_name = models.CharField(max_length=10)
    eng_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True)
    parents_phone = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ['group', ]
        unique_together = (("korean_name", "eng_name"),)

    def get_absolute_url(self):
        return reverse('student-detail', args=[self.id])

    def __str__(self):
        return '{} - {}({})'.format(self.korean_name, self.eng_name, self.group)


# class StudyType(models.Model):
#     study_type = models.CharField(max_length=20)

#     def __str__(self):
#         return self.study_type


class Study(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    time = models.TimeField(choices=time_choices)
    duration = models.DurationField(default=datetime.timedelta(minutes=20))

    class Meta:
        abstract = True


class Regular(Study):
    start_on = models.DateField(default=datetime.date.today)
    days_of_week = models.CharField(max_length=10, choices=day_of_week)

    def __str__(self):
        return '{} - on {} {}'.format(self.student, self.days_of_week, self.time)
    class Meta:
        ordering = ['days_of_week','time']

class Temporary(Study):
    temp_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return '{} - on {} {}'.format(self.student, self.temp_date, self.time)


class Problem(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    finished = models.BooleanField(default=False)
    problem = models.TextField()

    class Meta:
        ordering = ('date',)

    def get_absolute_url(self):
        return reverse('problem-detail', args=[self.id])

    def __str__(self):
        return '{} - {}, {}'.format(self.student, self.problem, self.date)


class Absent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField()
    why = models.CharField(max_length=100)
    have_to_check = models.BooleanField(default=False)

    class Meta:
        ordering = ('date', 'student',)

    def __str__(self):
        return '{} - {}, {}'.format(self.student, self.date, self.have_to_check)
