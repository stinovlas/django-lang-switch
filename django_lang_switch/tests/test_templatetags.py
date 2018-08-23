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
        self.assertRegex(rendered, r'<option value="en">\s*English \(en\)\s*</option>')
        self.assertRegex(rendered, r'<option value="cs" selected>\s*Česky \(cs\)\s*</option>')
        self.assertRegex(rendered, r'<option value="ko">\s*한국어 \(ko\)\s*</option>')
