from typing import Optional

from dynaconf import Dynaconf, LazySettings


def get_settings(env_for_dynaconf: Optional[str] = None) -> LazySettings:
    return Dynaconf(
        envvar_prefix='DE',
        settings_files=['settings/settings.toml', 'settings/.secrets.toml'],
        environments=True,
        env=env_for_dynaconf,
        load_dotenv=True,
    )
