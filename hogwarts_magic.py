import random


class Wizard:
    def __init__(self, name, patronus, birth_year):
        self.name = name
        self.patronus = patronus
        self.birth_year = birth_year
        self.house = None
        self.wand = None
        self.skill = 0.2  # 0.0 (bad) to 1.0 (good)

    def __gt__(self, other):
        return self.skill > other.skill

    def __eq__(self, other):
        return (
                self.name == other.name
                and self.patronus == other.patronus
                and self.birth_year == other.birth_year
        )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', '{self.patronus}', {self.birth_year})"

    def change_skill(self, amount):
        self.skill += amount
        if self.skill > 1.0:
            self.skill = 1.0

    def assign_wand(self, wand):
        self.wand = wand
        print(f"{self.name} has a {self.wand} wand.")

    def assign_house(self, house):
        self.house = house
        house.add_member(self)

    def cast_spell(self, spell):
        if self.wand:
            effect = self.wand.cast_spell(spell, self)
            if effect:
                print(f"{self.name} cast {effect}!")
            else:
                print(f"{self.name} failed to cast {spell.name}!")
        else:
            print(f"{self.name} has no wand!")


class Professor(Wizard):
    def __init__(self, name, patronus, birth_year, subject=None):
        super().__init__(name, patronus, birth_year)
        self.subject = subject

    def assign_wand(self, wand):
        super().assign_wand(wand)
        self.change_skill(0.2)

    def assess_student(self, student, grade):
        if self.subject in student.subject_grades:
            print(
                f"{self.name} assessed {student.name} in "
                f"{self.subject}. The grade is {grade}%."
            )
            student.take_exam(self.subject, grade)
        else:
            print(
                f"{student.name} doesn't study {self.subject}."
            )


class Student(Wizard):
    def __init__(self, name, patronus, birth_year, school_year=1):
        super().__init__(name, patronus, birth_year)
        self.school_year = school_year
        self.subject_grades = {}

    def __str__(self):
        return f"{self.name} (House: {self.house} | Year {self.school_year})"

    def assign_house_using_sorting_hat(self, school):
        house_name = random.choice(school.get_house_names())
        house = school.get_house(house_name)
        self.assign_house(house)

    def take_exam(self, subject, grade):
        self.subject_grades[subject] = grade

    def assign_subjects(self, subjects):
        self.subject_grades = {subject: None for subject in subjects}


class House:
    def __init__(self, name, founder, colours, animal):
        self.name = name
        self.founder = founder
        self.colours = colours
        self.animal = animal
        self.members = []
        self.points = 0

    def __iter__(self):
        return iter(self.members)

    def __str__(self):
        return self.name

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def update_points(self, points):
        self.points += points

    def get_house_details(self):
        return {
            "name": self.name,
            "founder": self.founder,
            "colours": self.colours,
            "animal": self.animal,
            "points": self.points
        }


class Wand:
    def __init__(self, wood, core, length, power=0.5):
        self.wood = wood
        self.core = core
        self.length = length
        self.power = power  # 0.0 (weak) to 1.0 (strong)

    def cast_spell(self, spell, wizard):
        if spell.is_successful(self, wizard):
            return spell.effect
        return None  # Explicitly return None (for readability)


class Spell:
    def __init__(self, name, effect, difficulty):
        self.name = name
        self.effect = effect
        self.difficulty = difficulty  # 0.0 (easy) to 1.0 (hard)

    def is_successful(self, wand, wizard):
        success_rate = (
                (1 - self.difficulty)
                * wand.power
                * wizard.skill
        )
        return random.random() < success_rate


class Hogwarts:
    _houses = {
        "Gryffindor": House(
            "Gryffindor", "Godric Gryffindor", ["scarlet", "gold"], "lion"
        ),
        "Slytherin": House(
            "Slytherin", "Salazar Slytherin", ["green", "silver"], "serpent"
        ),
        "Ravenclaw": House(
            "Ravenclaw", "Rowena Ravenclaw", ["blue", "bronze"], "eagle"
        ),
        "Hufflepuff": House(
            "Hufflepuff", "Helga Hufflepuff", ["yellow", "black"], "badger"
        ),
    }

    def get_house_names(self):
        return list(self._houses.keys())

    def get_house(self, house_name):
        return self._houses.get(house_name, None)










