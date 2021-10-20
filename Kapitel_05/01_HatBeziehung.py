class Studiengang:
    def __init__(self, hochschule, name):
        self.hochschule = hochschule
        self.name = name

## -------------------------------------------

class Kurs:
    def __init__(self, name):
        self.name = name
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def __str__(self):
        s = "KURS: " + self.name + "\n"
        for student in self.students:
            s += student.vorname + " " + student.nachname + " " + student.studiengang.name + "\n"
        return s
## -------------------------------------------

class Student:
    def __init__(self, vorname, nachname, geschlecht, studiengang):
        self.matrikelnummer = ""
        self.vorname = vorname
        self.nachname = nachname
        self.adresse = ""
        self.studiengang = studiengang
        self.geschlecht = geschlecht


geomatik = Studiengang("HABG", "Geomatik")
architektur = Studiengang("HABG", "Architektur")

student1 = Student("Hans", "Meier", "m", geomatik)
student2 = Student("Alexandra", "Müller", "w", geomatik)
student3 = Student("Joachim", "Huber", "m", architektur)

student3.studiengang = geomatik

prog = Kurs("Programmieren")
prog.addStudent(student1)
prog.addStudent(student2)
prog.addStudent(student3)

dbv = Kurs("DBV")
dbv.addStudent(student1)
dbv.addStudent(student3)

print(prog)
print(dbv)

student1.vorname = "Franz"

print(prog)