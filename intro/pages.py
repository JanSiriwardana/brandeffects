from ._builtin import Page


class Welcome(Page):
    def vars_for_template(self):
        return {'button_text': "Next"}


page_sequence = [
    Welcome,
]
