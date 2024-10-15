from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_alter_process_time'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
            ALTER TABLE "process_process" ALTER COLUMN "time" TYPE numeric(5,1)
            USING (EXTRACT(EPOCH FROM "time") / 86400.0);
            ''',
            reverse_sql='''
            ALTER TABLE "process_process" ALTER COLUMN "time" TYPE interval
            USING (make_interval(secs => "time" * 86400));
            ''',
        ),
        migrations.AlterField(
            model_name='process',
            name='time',
            field=models.DecimalField(max_digits=5, decimal_places=1),
        ),
    ]
