===========
 Changelog
===========

0.1
===
* Setup CI
* Add ``lang_switch_dropdown`` template tag
  * Renders select box with available language choices
  * Not-required ``redirect_to`` argument affects where to redirect after the language change
* Override django admin site template ``admin/base_site.html``
  * Style select box to fit into django admin site
