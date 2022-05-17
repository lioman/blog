"""i18n_templates plugin provides access to gettext without a complex i18n subsite

This plugin is designed for Pelican 3.4 and later
"""


import os
import logging


import gettext

from pelican import signals


# Global vars
_GENERATOR_DB = {}
_LOGGER = logging.getLogger(__name__)


def save_generator(generator):
    """Save the generator for later use

    initialize the removed content list
    """
    _GENERATOR_DB[generator] = []


def install_templates_translations(generator, pelican_obj):
    """Install gettext translations in the jinja2.Environment

    Only if the 'jinja2.ext.i18n' jinja2 extension is enabled
    the translations for the current DEFAULT_LANG are installed.
    """
    if "JINJA_ENVIRONMENT" in generator.settings:  # pelican 3.7+
        jinja_extensions = generator.settings["JINJA_ENVIRONMENT"].get("extensions", [])
    else:
        jinja_extensions = generator.settings["JINJA_EXTENSIONS"]

    if "jinja2.ext.i18n" in jinja_extensions:
        domain = generator.settings.get("I18N_GETTEXT_DOMAIN", "messages")
        localedir = generator.settings.get("I18N_GETTEXT_LOCALEDIR")
        if localedir is None:
            localedir = os.path.join(generator.theme, "translations")
        current_lang = generator.settings["DEFAULT_LANG"]
        if current_lang == generator.settings.get(
            "I18N_TEMPLATES_LANG", pelican_obj.settings["DEFAULT_LANG"]
        ):
            translations = gettext.NullTranslations()
        else:
            langs = [current_lang]
            try:
                translations = gettext.translation(domain, localedir, langs)
            except (IOError, OSError):
                _LOGGER.error(
                    (
                        "Cannot find translations for language '{}' in '{}' with "
                        "domain '{}'. Installing NullTranslations."
                    ).format(langs[0], localedir, domain)
                )
                translations = gettext.NullTranslations()
        newstyle = generator.settings.get("I18N_GETTEXT_NEWSTYLE", True)
        generator.env.install_gettext_translations(translations, newstyle)


def update_generators(pelican_obj):
    """Update the context of all generators

    Ads useful variables and translations into the template context
    and interlink translations
    """
    for generator in _GENERATOR_DB.keys():
        install_templates_translations(generator, pelican_obj)


# map: signal name -> function name
_SIGNAL_HANDLERS_DB = {
    "get_writer": update_generators,
    "generator_init": save_generator,
}


def register():
    """Register the plugin only if required signals are available"""
    for sig_name in _SIGNAL_HANDLERS_DB.keys():
        if not hasattr(signals, sig_name):
            _LOGGER.error(
                (
                    "The i18n_templates plugin requires the {} "
                    "signal available for sure in Pelican 3.4.0 and later, "
                    "plugin will not be used."
                ).format(sig_name)
            )
            return

    for sig_name, handler in _SIGNAL_HANDLERS_DB.items():
        sig = getattr(signals, sig_name)
        sig.connect(handler)
