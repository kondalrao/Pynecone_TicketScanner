#!/Users/kkomaragiri/.local/share/virtualenvs/TicketScanner-D3VHANZ3/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from pynecone.pc import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())