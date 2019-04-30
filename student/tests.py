from django.test import TestCase, Client
from .models import Student
# Create your tests here.
class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name = 'test_for_post',
            sex = 1,
            email = '333@dd.com',
            profession = '程序员',
            qq = '3333',
            phone = '32222',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='zfy',
            sex=1,
            email='333@aa.com',
            profession='dd',
            qq='234234',
            phone='12123',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容跟展示不一致！')

    def test_filter(self):
        Student.objects.create(
            name='test_for_post',
            sex=1,
            email='333@dd.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )
        name = 'zzzfy'
        students = Student.objects.filte(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录'.format(name))