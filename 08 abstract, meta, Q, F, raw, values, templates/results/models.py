from django.db import models

class StudentSubject(models.Model):
    class Meta:
        abstract = True

    student = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)


class StudentExam(StudentSubject):
    class Meta:
        db_table = "results"
        verbose_name_plural = "resultados"
        unique_together = ('student', 'subject', 'semester')

    semester = models.SmallIntegerField(default=1)
    planned = models.SmallIntegerField(default=100)
    score = models.SmallIntegerField()

    def __unicode__(self):
        return "%s:%s:%s, planned: %s, got: %s" % (self.student, 
                self.subject, self.semester, 
                self.planned, self.score
                )