from models import Goods
from eav.forms import BaseDynamicEntityForm


class GoodsForm(BaseDynamicEntityForm):
    model = Goods
