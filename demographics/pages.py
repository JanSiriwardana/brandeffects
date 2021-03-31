from ._builtin import Page


class Introduction(Page):
    template_name = "demographics/Introduction.html"

    def vars_for_template(self):
        return {'title': "A bit about you...",
                'button_text': "Next"}


class QuestionPage(Page):
    form_model = 'player'
    template_name = "ledr/SimplePage.html"

    def vars_for_template(self):
        return {'title': "A bit about you..."}


class Page1(QuestionPage):
    form_fields = ['gender']


class Page2(QuestionPage):
    form_fields = ['age']


class Page3(QuestionPage):
    form_fields = ['countryborn']


class Page4(QuestionPage):
    form_fields = ['countrynow']


class Page5(QuestionPage):
    form_fields = ['degree']


class Page6(QuestionPage):
    form_fields = ['department']

    def is_displayed(self):
        # Only display if participant responded and gave a degree course
        return self.player.degree is not None and self.player.degree <= 5


class Page7(QuestionPage):
    form_fields = ['timeuea']


page_sequence = [
    Introduction,
    Page1,
    Page2,
    Page3,
    Page4,
    Page5,
    Page6,
    Page7,
]
