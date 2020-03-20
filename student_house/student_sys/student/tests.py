from django.test import TestCase
from django.test import Client

from .models import Student
# Create your tests here.
class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
                name='ZL',
                sex=1,
                email='zl@123456.com',
                profession='Protoss',
                qq='123456',
                phone='13579',
                )
    
    def test_create_and_sex_show(self):
        student=Student.objects.create(
                name='ZY',
                sex=2,
                email='zy@123456.com',
                profession='cute',
                qq='123456',
                phone='13579',
                )
        self.assertEqual(student.sex_show,'女','性别字段内容跟展示不一致！')

    def test_filter(self):
        Student.objects.create(
                name='ZY',
                sex=2,
                email='zy@123456.com',
                profession='cute',
                qq='123456',
                phone='13579',
                )
        name='ZY'
        students=Student.objects.filter(name=name)
        self.assertEqual(students.count(),1,'应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):
        client=Client()
        response=client.get('/')
        self.assertEqual(response.status_code,200,'status code must be 200!')

    def test_post_student(self):
        """docstring for test_post_student"""
        client=Client()
        data=dict(
                name='test_for_post',
                sex=1,
                email='test@post.com',
                profession='Test',
                qq='123456',
                phone='1345',
                )
        response=client.post('/',data)
        self.assertEqual(response.status_code,302,'status code must be 302!')

        response=client.get('/')
        self.assertTrue(b'test_for_post' in response.content,
                        'response content must contain `test_for_post`')
