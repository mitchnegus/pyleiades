from pyleiades.visuals import Visual
from matplotlib import pyplot as plt

visual = Visual()
visual.include_energy('nuclear','coal')
visual.linegraph('totals')
#visual.linegraph('totals', freq='monthly')
plt.show()
