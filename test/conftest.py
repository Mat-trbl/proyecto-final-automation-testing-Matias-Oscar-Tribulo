import pytest
from utils.helpers import get_driver
import logging
import pathlib

path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)


logging.basicConfig(
    filename= path_dir/ "historial.log",
    level= logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s - %(message)s',
    datefmt='%H:%M:%S'
)

logger = logging.getLogger()


@pytest.fixture
def driver():
   # configuracion para consultar a selenium web driver
   driver = get_driver()
   yield driver
   driver.quit()