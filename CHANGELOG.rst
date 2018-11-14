===========
 Changelog
===========

0.3
===
* Fix MANIFEST.in
  * Include templates and other files outside of ``static`` directory

0.2
===
* Fix homepage url in setup.py
* Fix static links in MANIFEST.in

0.1
===
* Setup CI
* Add ``lang_switch_dropdown`` template tag
  * Renders select box with available language choices
  * Not-required ``redirect_to`` argument affects where to redirect after the language change
* Override django admin site template ``admin/base_site.html``
  * Style select box to fit into django admin site
