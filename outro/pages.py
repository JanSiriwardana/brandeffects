from ._builtin import Page


class ThankYou(Page):
    pass


class JanThankYou(Page):
    def vars_for_template(self):
        return {'button_text': "Return to Prolific"}


class Redirect(Page):
    @staticmethod
    def js_vars():
        return dict(redirect_url='https://app.prolific.co/submissions/complete?cc=35A44904')

page_sequence = [
    #ThankYou,
    JanThankYou,
    Redirect
]
