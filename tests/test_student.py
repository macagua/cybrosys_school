# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestStudent(common.TransactionCase):

    def setUp(self):
        super(TestStudent, self).setUp()
        # 'school.student' instance model
        self.student = self.env['school.student']

        # create an student record
        self.student1 = self.student.create({
            'name': 'Diego Alejandro Tirado Caballero',
            'age': 1,
            'gender': 'male',
            'student_dob': '2017-10-01',
            'student_blood_group': 'B+',
            'nationality': self.env.ref('base.cl').id,
            'level_education': 'kinder_garden'
        })

        self.student2 = self.student.create({
            'name': 'Miguel Angel Tirado Caballero',
            'age': 3,
            'gender': 'male',
            'student_dob': '2018-05-01',
            'student_blood_group': 'B+',
            'nationality': self.env.ref('base.ve').id,
            'level_education': 'primary'
        })

    def test_compute_level_education(self):
        # This function test the '_compute_level_education' function functionality
        # Here 'level_education' of student setting using the 'age'

        # check level_education of the student1
        self.assertEqual(self.student1.level_education, 'kinder_garden')

        # check level_education of the student2
        self.assertEqual(self.student2.level_education, 'primary')

        # change the age of student2
        self.student1.write({
            'age': 3,
        })

        # again check the level_education of student
        self.assertEqual(self.student1.level_education, 'primary')

        _logger.info("Your 'TestStudent' test was successful!")
