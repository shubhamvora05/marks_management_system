from django.db import models


class Standerd(models.Model):

    CBSE = "CBSE"
    GSEB = "GSEB"
    Science = "Science"
    Commerce = "Commerce"

    MediumOfStudent = ((CBSE, "CBSE"),
                       (GSEB, "GSEB"),
                       (Science, "Science"),
                       (Commerce, "Commerce"))

    Id = models.AutoField(primary_key=True)
    Std = models.PositiveIntegerField()
    Medium = models.CharField(
        max_length=11, choices=MediumOfStudent, default=GSEB)
    Div = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        stdn = str(self.Std) + " "+self.Medium
        return stdn


class studentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    HR_No = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    Middle_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Room_No = models.CharField(max_length=10)
    studentStd = models.ForeignKey(Standerd, on_delete=models.CASCADE)

    def __str__(self):
        return self.HR_No


class subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_Name = models.CharField(max_length=30)
    subjectStd = models.ForeignKey(Standerd, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_Name


class marksRecord(models.Model):
    Id = models.AutoField(primary_key=True)
    totalMarks = models.PositiveIntegerField()
    date = models.DateField()
    Subject = models.ForeignKey(subject, on_delete=models.CASCADE)

    def __str__(self):
        record = str(self.date) + " "+str(self.totalMarks)
        return record


class Marks(models.Model):
    Id = models.AutoField(primary_key=True)
    achivedMarks = models.PositiveIntegerField()
    Student = models.ForeignKey(studentInfo, on_delete=models.CASCADE)
    totalMarks = models.ForeignKey(marksRecord, on_delete=models.CASCADE)

    def __str__(self):
        record = str(self.totalMarks.date) + " "+str(self.achivedMarks)
        return record
