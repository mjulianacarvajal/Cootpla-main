import contextlib



from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.core.management import call_command


#calibrar despues de entregarlo a 24h   // 'interval', **hours=24**, l19

# def db_copia():
#     with contextlib.suppress(Exception):
#         call_command('dbbackup')
#
# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_jobstore(DjangoJobStore(),'default')
#     scheduler.add_job(db_copia, 'interval', minutes=1, replace_existing=True)
#
#     scheduler.start()


