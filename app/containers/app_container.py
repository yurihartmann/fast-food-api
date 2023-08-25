from dependency_injector import containers, providers

from app.containers.drivers_container import DriversContainer


class AppContainer(containers.DeclarativeContainer):
    # Drivers
    drivers: DriversContainer = providers.Container(
        DriversContainer
    )
