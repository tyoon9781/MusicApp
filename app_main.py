#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

CMD = ["runserver", "0.0.0.0:8008"]
DJANGO_SETTING_PATH = 'config.settings.dev'
sys_argv = [sys.argv[0], *CMD]

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTING_PATH)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # execute_from_command_line(sys.argv)
    execute_from_command_line(sys_argv)


if __name__ == '__main__':
    main()
