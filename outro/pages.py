from ._builtin import Page


class ThankYou(Page):
    pass


class Feedback(Page):
    form_model = 'player'
    form_fields = ['instructions', 'if_no', 'browser', 'technical', 'if_yes', 'comments']

    def vars_for_template(self):
        return {'button_text': "Next"}


class JanThankYou(Page):
    def vars_for_template(self):
        return {'button_text': "Return to Prolific"}


class Redirect(Page):
    @staticmethod
    def js_vars():
        return dict(redirect_url='https://app.prolific.co/submissions/complete?cc=C1AMB8Y8')

page_sequence = [
    #ThankYou,
    #Feedback,
    JanThankYou,
    Redirect
]
