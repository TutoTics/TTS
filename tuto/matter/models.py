from django.db import models

from users.models import Student, Teacher


class Semester(models.Model):
    TYPE_CHOICES = [
        ('Primero', 'Primero'),
        ('Segundo', 'Segundo'),
        ('Tercero', 'Tercero'),
        ('Cuarto', 'Cuarto'),
        ('Quinto', 'Quinto'),
        ('Sexto', 'Sexto'),
        ('Septimo', 'Séptimo'),
        ('Octavo', 'Octavo'),
        ('Noveno', 'Noveno'),
        ('Decimo', 'Décimo'),

    ]

    number = models.CharField(
        verbose_name="Número", max_length=20, choices=TYPE_CHOICES,
    )

    class Meta:
        verbose_name = ('Semestre')
        verbose_name_plural = ('Semestres')

    def __str__(self):
        return self.number


class Matter(models.Model):
    name = models.CharField(
        verbose_name="Nombre", max_length=20
    )
    schedule = models.DateTimeField(verbose_name="Horario")
    semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE, verbose_name='Semestre',
    )

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return self.name


class Inscription(models.Model):

    date = models.DateTimeField(
        verbose_name="Fecha de inscripcion", auto_now_add=True
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name=('Estudiante'),
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name=('Profesor'),
    )
    matter = models.ForeignKey(
        Matter, on_delete=models.CASCADE, verbose_name=('Materia'),
    )

    class Meta:
        verbose_name = 'Incripcion'
        verbose_name_plural = 'Incripciones'
        unique_together = ('student', 'teacher', 'matter')

    def __str__(self):
        return f'Regitro de inscripción #{self.pk}'
