import random

from datacenter.models import *


def get_info_for_child(name):
	try:
		child = Schoolkid.objects.get(full_name__contains=name)
	except:
		print('Введено не верное имя. Введите фамилию и имя полностью')
	return child


def fix_marks(schoolkid):
	child = get_info_for_child(schoolkid)
	marks = Mark.objects.filter(schoolkid=child, points__lt=4)
	for mark in marks:
		mark.points = 5
		mark.save()

def remove_chastisements(schoolkid):
	child = get_info_for_child(schoolkid)
	chastiments = Chastisement.objects.filter(schoolkid=child)
	chastiments.delete()

def get_last_lesson_subject_for_child(child, subject):
	child = get_info_for_child(schoolkid)
	lessons = Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter)
	last_lesson = lessons.filter(subject__title__contains=subject).order_by('-date')[0]
	return last_lesson



def create_commendation(child, subject):
	commedtations_for_child = ['Молодец!', 'Отлично!', 'Хорошо!', 
		'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
		'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!',
		'Именно этого я давно ждал от тебя!',
		'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!',
		'Очень хороший ответ!', 'Талантливо!',
		'Ты сегодня прыгнул выше головы!', 'Я поражен!'
		]
	random_commetation = random.choice(commedtations_for_child)
	last_lesson = get_last_lesson_subject_for_child(child, subject)
	Commendation.objects.create(text=random_commetation, schoolkid=child, created=last_lesson.date, subject=last_lesson.subject, teacher=last_lesson.teacher)
	



