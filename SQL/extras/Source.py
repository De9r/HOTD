import re
import time
from datetime import datetime
from Arab import StartTime, iqthon
from Arab.Config import Config
from Arab.plugins import mention
help1 = ("**♛ ⦙ كيفيه التنصيب :**")
help2 = ("**- اوامر الاونلاين تشتغل فقط في المجموعات**")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**♛ : version 7.6  𓇡.** \n♛ : me  {mention}  𓇡. \n**♛ : time  {TM}  𓇡.**\n**♛ : My Bot {TG_BOT} 𓇡.**\n**♛ : Source : @cn_world  𓇡.**"
