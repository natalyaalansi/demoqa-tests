from demoqa_tests.model.data import user
from demoqa_tests.model.pages import app

def test_submit_practise_form():
    student = user.sample_female_student

    (
        app.registration_form

            .open()

            .fill_full_name(student.firstname, student.lastname)
            .fill_email(student.email)
            .select_gender(student.gender)
            .fill_phone_number(student.mobile)
            .select_birthday(student.birthday)
            .fill_subjects(student.subjects)
            .set_hobbies(student.hobbies)
            .select_picture(student.picture)
            .fill_address(student.address)
            .scroll_to_bottom()
            .set_state(student.state)
            .set_city(student.city)
            .submit()

            .assert_form_sent(
                ('Student Name', f'{student.firstname} {student.lastname}'),
                ('Student Email', student.email),
                ('Gender', student.gender.name),
                ('Mobile', student.mobile),
                ('Date of Birth', student.birthday),
                ('Subjects', ', '.join([subject.value for subject in student.subjects])),
                ('Hobbies', ', '.join([hobby.value for hobby in student.hobbies])),
                ('Picture', student.picture),
                ('Address', student.address),
                ('State and City', f'{student.state} {student.city}')
            )
    )
