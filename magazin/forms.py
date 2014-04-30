from models import Property
from eav.forms import BaseDynamicEntityForm


class PropertyForm(BaseDynamicEntityForm):
    model = Property
