"""Test template tags."""
from django.template import Context, Template
from django.test import SimpleTestCase, override_settings


class TestDropdownMenu(SimpleTestCase):
    """Test lang_switch_dropdown template tag."""

    def render_template(self, template, context=None):
        context = context or {}
        context = Context(context)
        return Template(template).render(context)

    @override_settings(
        LANGUAGES=[('en', 'English'), ('cs', 'Czech'), ('ko', 'Korean')],
        LANGUAGE_CODE='cs')
    def test_simple_dropdown(self):
        rendered = self.render_template(
            '{% load lang_switch %}{% lang_switch_dropdown %}'
        )
        self.assertInHTML('<option value="en">English (en)</option>', rendered)
        self.assertInHTML('<option value="cs" selected>Česky (cs)</option>', rendered)
        self.assertInHTML('<option value="ko">한국어 (ko)</option>', rendered)

    @override_settings(
        LANGUAGES=[('en', 'English'), ('cs', 'Czech'), ('ko', 'Korean')],
        LANGUAGE_CODE='cs')
    def test_redirect_to(self):
        rendered = self.render_template(
            '{% load lang_switch %}{% lang_switch_dropdown redirect_to="hogwarts" %}'
        )
        self.assertInHTML('<option value="en">English (en)</option>', rendered)
        self.assertInHTML('<option value="cs" selected>Česky (cs)</option>', rendered)
        self.assertInHTML('<option value="ko">한국어 (ko)</option>', rendered)
        self.assertInHTML('<input name="next" type="hidden" value="hogwarts">', rendered)
