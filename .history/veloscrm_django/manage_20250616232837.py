#!/usr/bin/env python
"""Django’s command-line utility voor administratieve taken."""

import os    # omgevingsvariabelen instellen voor Django
import sys   # toegang tot command-line argumenten

def main():
    """Voer admin-taken uit via de command-line."""
    # zorg dat Django weet welke settings geladen moeten worden
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veloscrm_django.settings')
    try:
        # importeer de execute-from-command-line helper van Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # geef een duidelijke foutmelding als Django niet geïnstalleerd is
        raise ImportError(
            "Kon Django niet importeren. Zeker weten dat het geïnstalleerd is "
            "en beschikbaar op je PYTHONPATH? Virtualenv actief?"
        ) from exc
    # verwerk de command-line arguments (runserver, migrate, etc.)
    execute_from_command_line(sys.argv)

# startpunt van het script: roep main() aan als dit bestand direct wordt uitgevoerd
if __name__ == '__main__':
    main()
