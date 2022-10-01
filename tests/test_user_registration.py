import datetime
from demoqa_tests.model.pages import registration_form
from demoqa_tests.model.data import user

def test_submit_practise_form():

    registration_form.given_opened()

    registration_form.fill_full_name('natalya', 'alansi')
    registration_form.fill_email('nalansi@yahoo.com')
    registration_form.select_gender(user.Gender.Male)
    registration_form.fill_phone_number('0123456789')
    registration_form.select_birthday(datetime.date(1993, 7, 24))
    registration_form.fill_subjects('Computer Science')
    registration_form.select_hobbies(user.Hobby.Sports)
    registration_form.select_picture('minion.png')
    registration_form.fill_address('Tbilisi')
    registration_form.scroll_to_bottom()
    registration_form.set_state('NCR')
    registration_form.set_city('Delhi')
    registration_form.submit()

    registration_form.check_submitted_user(
        [
            ('Student Name', 'natalya alansi'),
            ('Student Email', 'nalansi@yahoo.com'),
            ('Gender', 'Male'),
            ('Mobile', '0123456789'),
            ('Date of Birth', '24 July,1993'),
            ('Subjects', 'Computer Science'),
            ('Hobbies', 'Sports'),
            ('Picture', 'minion.png'),
            ('Address', 'Tbilisi'),
            ('State and City', 'NCR Delhi')
        ],
    )